def get_text(path):
    with open(path) as p:
        return p.read()
    
def write_file(file, path):
    with open(path, "w") as p:
        return p.write(file)