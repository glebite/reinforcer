import os
import sys
from collections import defaultdict


class WordList:
    """
    """
    def __init__(self, filename=None):
        self.filename = filename
        self.word_list = []
        self.first_letter = defaultdict(list)

    def load_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as fp:
                for line in fp:
                    line = line.strip()
                    self.word_list.append(line)
        else:
            raise FileNotFoundError(f"No such luck with: {self.filename}")

    def build_first_letter_list(self):
        if self.word_list:
            for word in self.word_list:
                first = word[0]
                remainder = word[1:]
                self.first_letter[first].append(remainder)


if __name__ == "__main__":
    x = WordList(sys.argv[1])
    x.load_file()
    x.build_first_letter_list()
    for letter in x.first_letter.keys():
        print(f'{letter} -> {len(x.first_letter[letter])}')
