import pdfplumber

def is_heading(element):
    # Check font size and style to identify headings
    font_size = element.get("font_size")
    font_name = element.get("fontname")
    if font_size is not None and font_size > 10:
        if font_name is not None and "bold" in font_name.lower():
            return True
    return False

def extract_headings_and_paragraphs(file_path):
    with pdfplumber.open(file_path) as pdf:
        headings = []
        paragraphs = []
        for page in pdf.pages:
            words = page.extract_words(x_tolerance=2, y_tolerance=2)
            heading_text = ""
            for i, word in enumerate(words):
                if is_heading(word):
                    if heading_text:
                        headings.append(heading_text.strip())
                        heading_text = ""
                    headings.append(word["text"])
                else:
                    heading_text += " " + word["text"]
            if heading_text:
                headings.append(heading_text.strip())
            
            # Extract paragraphs
            paragraphs.append(page.extract_text())
    
    return headings, paragraphs

# Example usage
pdf_file = "1.pdf"
headings, paragraphs = extract_headings_and_paragraphs(pdf_file)

# Print headings
print("Headings:")
for heading in headings:
    print(heading)
    
# Print paragraphs
print("\nParagraphs:")
for paragraph in paragraphs:
    print(paragraph)
