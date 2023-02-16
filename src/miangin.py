from collections import defaultdict


FILE_PATH = '../data/5000-Persian.txt'


class Miangin:
    """
    """
    def __init__(self, filename):
        self.filename = filename
        self.organized = defaultdict()
        self.words = []

    def read(self):
        with open(self.filename, 'r') as fp:
            for word in fp:
                word = fp.readline().strip()
                self.words.append(word)
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

    def find_subwords(self):
        words = self.words
        subwords = {}
        for word in words:
            for i in range(len(word)):
                for j in range(i+1, len(word)+1):
                    subword = word[i:j]
                    if subword != word and subword in words\
                       and subword not in subwords:
                        subwords[subword] = set()
                        for w in words:
                            if subword in w:
                                subwords[subword].add(w)
        return subwords


if __name__ == "__main__":
    x = Miangin(FILE_PATH)
    x.read()
    x.biggest()
    print(x.find_subwords())
