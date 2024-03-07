import fitz
from operator import itemgetter
import json
import re

def fonts(doc, granularity=False):
    """Extracts fonts and their usage in PDF documents.

    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param granularity: also use 'font', 'flags' and 'color' to discriminate text
    :type granularity: bool

    :rtype: (List[Tuple[float, int]], dict)
    :return: most used fonts sorted by count, font style information
    """
    styles = {}
    font_counts = {}

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b['type'] == 0:  # block contains text
                for l in b["lines"]:  # iterate through the text lines
                    for s in l["spans"]:  # iterate through the text spans
                        if granularity:
                            identifier = "{0}_{1}_{2}_{3}".format(s['size'], s['flags'], s['font'], s['color'])
                            styles[identifier] = {'size': s['size'], 'flags': s['flags'], 'font': s['font'],
                                                  'color': s['color']}
                        else:
                            identifier = "{0}".format(s['size'])
                            styles[identifier] = {'size': s['size'], 'font': s['font']}

                        font_counts[identifier] = font_counts.get(identifier, 0) + 1  # count the fonts usage

    font_counts = sorted(font_counts.items(), key=itemgetter(1), reverse=True)

    if len(font_counts) < 1:
        raise ValueError("Zero discriminating fonts found!")

    return font_counts, styles

def font_tags(font_counts, styles):
    """Returns dictionary with font sizes as keys and tags as value.

    :param font_counts: (font_size, count) for all fonts occuring in document
    :type font_counts: list
    :param styles: all styles found in the document
    :type styles: dict

    :rtype: dict
    :return: all element tags based on font-sizes
    """
    p_style = styles[font_counts[0][0]]  # get style for most used font by count (paragraph)
    p_size = p_style['size']  # get the paragraph's size

    # sorting the font sizes high to low, so that we can append the right integer to each tag 
    font_sizes = []
    for (font_size, count) in font_counts:
        font_sizes.append(float(font_size))
    font_sizes.sort(reverse=True)

    # aggregating the tags for each font size
    idx = 0
    size_tag = {}
    for size in font_sizes:
        idx += 1
        if size == p_size:
            idx = 0
            size_tag[size] = '<p>'
        if size > p_size:
            size_tag[size] = '<h{0}>'.format(idx)
        elif size < p_size:
            size_tag[size] = '<s{0}>'.format(idx)

    return size_tag

def headers_para(doc, size_tag):
    """
    Scrapes headers & paragraphs from PDF and return texts with element tags.

    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param size_tag: textual element tags for each size
    :type size_tag: dict
    :return: texts with pre-prended element tags
    :rtype: list
    """
    header_para = []  # list with headers and paragraphs
    previous_s = None  # previous span

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b['type'] == 0:  # this block contains text

                # REMEMBER: multiple fonts and sizes are possible IN one block

                block_string = ""  # text found in block
                for l in b["lines"]:  # iterate through the text lines
                    for s in l["spans"]:  # iterate through the text spans
                        if s['text'].strip():  # removing whitespaces:

                            if not previous_s:
                                block_string = size_tag[s['size']] + s['text']
                            elif s['size'] == previous_s['size']:
                                if block_string and all((c == "") for c in block_string):
                                    # block_string only contains pipes
                                    block_string = size_tag[s['size']] + s['text']
                                elif not block_string:
                                    # new block has started, so append size tag
                                    block_string = size_tag[s['size']] + s['text']
                                else:  # in the same block, so concatenate strings
                                    block_string += " " + s['text']
                            else:
                                header_para.append(block_string)
                                block_string = size_tag[s['size']] + s['text']

                            previous_s = s

                    # new block started, indicating with a pipe
                    block_string += ""

                header_para.append(block_string)

    return header_para


def clean_empty_values(json_data):

    if isinstance(json_data, str):
        json_data = json.loads(json_data)

    def _clean_data(data):
        if isinstance(data, dict):
            return {
                key: _clean_data(value)
                for key, value in data.items()
                if _clean_data(value)  # Recursively clean nested values
            }
        elif isinstance(data, list):
            return [_clean_data(item) for item in data if _clean_data(item)]
        else:
            return data

    cleaned_data = _clean_data(json_data)
    return json.dumps(cleaned_data)

def process_json(json_list):
    # Initialize the JSON structure
    output = {
        "heading": "",
        "subheadings": []
    }

    current_subheading = None

    # Process each tag in the JSON list
    for tag in json_list:
        if tag.startswith("<h1>") or tag.startswith("<h2>"):
            # Extract the heading or subheading from the tag
            heading = re.sub(r"<.*?>", "", tag).strip()

            if tag.startswith("<h1>"):
                # Update the heading in the JSON structure
                output['heading'] = heading
            else:
                # Add a new subheading to the JSON structure
                current_subheading = {
                    "subheading": heading,
                    "content": ""
                }
                output['subheadings'].append(current_subheading)

        elif tag.startswith("<p>"):
            # Extract the paragraph content from the tag
            paragraph = re.sub(r"<.*?>", "", tag).strip()

            if current_subheading:
                # If there is a current subheading, add the paragraph to its content
                current_subheading['content'] += " " + paragraph
            else:
                # If there is no current subheading, add the paragraph as a subheading with empty content
                output['subheadings'].append({
                    "subheading": paragraph,
                    "content": ""
                })

    return output



def process_content(json_data):
    data = json.loads(json_data)
    subheadings = data["subheadings"]

    for subheading in subheadings:
        text = subheading["content"]
        points = re.split(r'\d+\.|\s●\s', text)
        points = [point.strip() for point in points if point.strip()]
        subheading["content"] = points
#         content_function(subheading["content"])

    return data


doc = fitz.open("static/file.pdf")
font_counts,styles=fonts(doc)
size_tag=font_tags(font_counts,styles)
text=headers_para(doc,size_tag)
json_output = process_json(text)
json_string = json.dumps(json_output, indent=4)
new_json = process_content(json_string)

with open('./static/1.json', 'w') as f:
    f.write(json.dumps(new_json, indent=4))
