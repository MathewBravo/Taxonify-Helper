import file_operations
import graphviz

from typing import List

def build_tree(lines:List[str], output_filename:str):
    tree = make_tree_graph(lines)

    dot_code = tree_to_dot(tree)


    if output_filename is not None:
        create_svg(dot_code, output_filename)
    else:
        create_svg(dot_code)

def make_tree_graph(config_lines: List[str]) -> dict:
    tree = {}
    stack = []

    for line in config_lines:
        indent_level = file_operations.get_indent_level(line)
        node = line.strip()
        stack = stack[:indent_level]
        add_to_tree(tree, stack, node)
        stack.append(node)

    return tree


def add_to_tree(tree, path, value):
    for node in path:
        tree = tree.setdefault(node, {})
    tree[value] = {}


def tree_to_dot(tree: dict) -> str:
    dot = "digraph G {\n"
    dot += "    graph [nodesep=0.3, ranksep=0.5];\n"  # Set node shape to box
    dot += "    node [shape=box];\n"  # Set node shape to box
    dot += "    splines=ortho;\n"     # Set splines to orthogonal

    def add_edges(tree, parent=None):
        nonlocal dot
        for node, children in tree.items():
            if parent:
                dot += f'    "{parent}"-> "{node}";\n'
            add_edges(children, node)

    add_edges(tree)
    dot += "}"
    return dot

def create_svg(dot_code, filename="tree"):
    graph = graphviz.Source(dot_code)
    graph.render(filename, format="svg", cleanup=False)