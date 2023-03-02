"""derakht.py

Tree representations of words in a given language.
"""


class Node:
    """Node
    """
    def __init__(self, value, index):
        """__init__ - initializer for a Node class
        """
        self.value = value
        self.index = index
        self.children = {}

    def add_child(self, char, node):
        self.children[char] = node


class Derakht:
    """Derakht
    """
    def __init__(self):
        """__init__ - intializer
        """
        self.root = Node("", 0)
        self.current_index = 1
        self.null_counter = 0

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char, self.current_index)
                self.current_index += 1
            current = current.children[char]
        current.children[f"NULL{self.null_counter}"] = Node(f"NULL{self.null_counter}", self.current_index)
        self.current_index += 1
        self.null_counter += 1

    def follow(self):
        dot_notation = "digraph {\n"
        stack = [self.root]
        while stack:
            node = stack.pop()
            for child in node.children.values():
                dot_notation += f"\t{node.index} -> {child.index} [label={child.value}];\n"
                stack.append(child)
        dot_notation += "}"
        return dot_notation

    def dump_first_letter(self, file_name, letter):
        with open(file_name, 'r') as fp:
            for line in fp:
                word = line.strip()
                if word.startswith(letter):
                    x.insert(word)
        print(x.follow())


if __name__ == "__main__":
    x = Derakht()
    x.dump_first_letter('../data/5000-Persian.txt', 'ط')
