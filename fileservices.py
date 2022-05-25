def read_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def add_data(filepath, data):
    with open(filepath, 'a') as file:
        file.write(data)
