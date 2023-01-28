"""wordlist.py

"""
import os
import sys
import logging
from collections import defaultdict
import colorlog


# basic logging configuration
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('my_log_info.log')
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s'
                              ' [%(filename)s.%(funcName)s:'
                              '%(lineno)d] %(message)s',
                              datefmt='%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(colorlog.ColoredFormatter('%(log_color)s '
                                          '[%(asctime)s] '
                                          '%(levelname)s '
                                          '[%(filename)s.'
                                          '%(funcName)s:'
                                          '%(lineno)d] '
                                          '%(message)s',
                                          datefmt='%a, %d'
                                          ' %b %Y %H:%M:%S'))
logger.addHandler(fh)
logger.addHandler(sh)


class WordList:
    """WordList - class to do work on with a wordlist 
    """
    def __init__(self, filename=None):
        """__init__ - initializer

        Params:
        filename (str): name of the file to acquire wordlist from
        """
        self.filename = filename
        logger.info(f'Initializing {self=} {self.filename=}')        
        self.word_list = []
        self.first_letter = defaultdict(list)

    def load_file(self):
        """
        """
        logger.info(f'Loading file {self.filename=}')
        if os.path.exists(self.filename):
            logger.debug(f'File exists: {self.filename}')
            with open(self.filename, 'r') as fp:
                for line in fp:
                    line = line.strip()
                    self.word_list.append(line)
        else:
            logger.error(f'Problem reading: {self.filename}')
            raise FileNotFoundError(f"No such luck with:"
                                    f" {self.filename}")

    def build_first_letter_list(self):
        """build_first_letter_list - build dictionary here
        """
        logger.info(f'Building first letter list'
                    f' {len(self.word_list)=}')
        if self.word_list:
            for word in self.word_list:
                first = word[0]
                remainder = word[1:]
                self.first_letter[first].append(remainder)
        else:
            logger.error('self.wordlist is empty')
            raise ValueError('self.wordlist is empty')


if __name__ == "__main__":
    x = WordList(sys.argv[1])
    x.load_file()
    x.build_first_letter_list()
    for letter in x.first_letter.keys():
        logger.debug(f'{letter} -> {len(x.first_letter[letter])}')
    logger.debug(f"{x.first_letter['گ']=}")
