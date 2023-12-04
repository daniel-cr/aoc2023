

def read_file(filename: str):
    file = []
    with open(filename, 'r') as data:
        for line in data:
            file.append(line.strip())
    return file