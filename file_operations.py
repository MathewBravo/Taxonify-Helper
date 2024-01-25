import make_graphs


def open_config(type: str, filename: str, output_filename: str):
    if type == "tree":
        with open(filename, 'r') as file:
            lines = file.readlines()
            make_graphs.build_tree(lines, output_filename)


def get_indent_level(line: str) -> int:
    normalize_line = line.replace("\t", "    ")

    indent_count = 0
    while normalize_line.startswith('    '):
        indent_count += 1
        normalize_line = normalize_line[4:]
    return indent_count
