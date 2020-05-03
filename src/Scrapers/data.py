import json
import codecs

def read_json(path):
    with codecs.open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return json.load(f)

def write_json(path, data:dict):
    with codecs.open(path, 'w', encoding='utf-8', errors='ignore') as f:
        return json.dump(data, f, indent=4, ensure_ascii=False)

def get_item(dict_body, keys:list):
    for key in keys:
        if isinstance(dict_body, dict):
            dict_body = dict_body.get(key)

        elif isinstance(key, int) and \
              isinstance(dict_body, list) and \
                  len(dict_body) > key:

            dict_body = dict_body[key]

        else:
            return dict_body

    return dict_body