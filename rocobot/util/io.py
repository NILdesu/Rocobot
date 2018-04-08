import os, json

def write_text(path, text):
    if len(path) <= 0:
        # TODO: raise an exception instead?
        return

    path_parts = path.split('/')
    if len(path_parts) > 1:
        cur_path_parts = []
        for i in range(0, len(path_parts) - 1):
            cur_path_parts.append(path_parts[i])
            cur_path = '/'.join(cur_path_parts)
            if not os.path.exists(cur_path):
                os.makedirs(cur_path)

    with open(path, 'w') as file:
        file.write(text)
        file.close()


def write_json(path, data):
    write_text(path, json.dumps(data))

def read_text(path):
    if not os.path.exists(path):
        return None

    text = ''
    with open(path, 'r') as file:
        text = file.read()
        file.close()

    return text

def read_json(path):
    text = read_text(path)
    if (text == None):
        return None
    return json.loads(text)
