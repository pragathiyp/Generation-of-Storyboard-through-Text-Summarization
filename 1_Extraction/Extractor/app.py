import deepdoctection as dd
import os

analyzer = dd.get_dd_analyzer()  # instantiate the built-in analyzer similar to the Hugging Face space demo

comp=analyzer.pipe_component_list
comp[7]=(dd.TextOrderService(text_container="word",
                                 text_block_categories= [dd.LayoutType.text,
                                                         dd.LayoutType.title,
                                                         dd.LayoutType.list,
                                                         dd.LayoutType.table],
                                 floating_text_block_categories=[dd.LayoutType.text,
                                                         dd.LayoutType.title,
                                                         dd.LayoutType.list,
                                                         dd.LayoutType.table],
                                 include_residual_text_container=True))

page_parsing = dd.PageParsingService(text_container="word",
                                     floating_text_block_categories=[dd.LayoutType.text,
                                                                     dd.LayoutType.title,
                                                                     dd.LayoutType.list,
                                                                     dd.LayoutType.table],
                                     include_residual_text_container=True)

pipe = dd.DoctectionPipe(pipeline_component_list=comp,
                         page_parsing_service=page_parsing)




path = "./sample/image.pdf"
df = pipe.analyze(path=path)
df.reset_state() 

# Create a directory to save the pages if it doesn't exist
output_dir = "./sample/pages"
os.makedirs(output_dir, exist_ok=True)
dpts = []


import json


data = {}
current_index = 0
mainTitleFlag = False
prev = None

def extractor_main():
    global mainTitleFlag  # declare mainTitleFlag as global
    global current_index   # declare current_index as global
    global prev            # declare prev as global
    for dp in df:
        layout_items = [layout for layout in dp.layouts if layout.reading_order is not None]
        layout_items.sort(key=lambda x: x.reading_order)
        
        for item in layout_items:
            if item.category_name == "title":
                if mainTitleFlag:
                    data[current_index-1] = {"mainTitle": prev.text}
                data[current_index] = {"title": item.text}
                current_index += 1
                mainTitleFlag = True
                prev = item

            elif item.category_name in ["text", "list"]:
                if mainTitleFlag:
                    mainTitleFlag = False
                data[current_index] = {"text": item.text}
                current_index += 1 

    with open("output.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
extractor_main()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get')
def hello():
    extractor_main();
    print("done!");
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")