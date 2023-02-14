from collections import defaultdict


FILE_PATH = '../data/5000-Persian.txt'


class Miangin:
    """
    """
    def __init__(self, filename):
        self.filename = filename
        self.organized = defaultdict()

    def read(self):
        with open(self.filename, 'r') as fp:
            for word in fp:
                word = fp.readline().strip()
                first = word[0]
                if first in self.organized:
                    self.organized[first].append(word)
                else:
                    self.organized[first] = list(word)

    def histogram(self):
        for letter in self.organized:
            print(f'{letter=} ==> {len(self.organized[letter])}')

    def average_len(self):
        for letter in self.organized:
            n = len(self.organized[letter])
            counter = 0
            for word in self.organized[letter]:
                counter += len(word)
            print(f'{letter=} ==> {counter/n}')

    def biggest(self):
        for letter in self.organized:
            res = max(self.organized[letter], key=len)
            print(f'{letter=} ==> {res} ==> {len(res)}')


if __name__ == "__main__":
    x = Miangin(FILE_PATH)
    x.read()
    x.biggest()
