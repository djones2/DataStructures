from hash_quad import *
import string
import os
from os import path


class Concordance:

    def __init__(self, capacity=191):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word 
        as a key into the stop words hash table.
        If file does not exist, raise FileNotFoundError"""
        if path.exists(filename) == False:
            raise FileNotFoundError
        self.stop_table = HashTable(191)
        line_number = 0
        with open(filename, 'r') as stopwords:
            for line in stopwords:
                line_number += 1
                for word in line.split():
                    self.stop_table.insert(word, line_number)

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        If file does not exist, raise FileNotFoundError"""
        if path.exists(filename) == False:
            raise FileNotFoundError
        self.concordance_table = HashTable(191)
        line_number = 0
        with open(filename, 'r') as concordance_file:
            for line in concordance_file:
                line_number += 1
                line = line.replace("-", ' ')
                for word in line.split():
                    if word[0].isdigit() == True:
                        continue
                    word = word.replace("'", "")
                    word = word.replace('"', "")
                    word = word.replace('.', "")
                    word = word.replace(',', "")
                    word = word.replace(';', "")
                    word = word.replace(':', "")
                    word = word.lower()
                    if word.isalpha() == False:
                        continue
                    if self.stop_table.in_table(word) == False:
                        self.concordance_table.insert(word, line_number)


    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format.""" 
        output = []
        for item in self.concordance_table.hash_table:
            if item != None:
                output.append(item)
        output.sort(key=lambda x: x[0])
        with open(filename, "w", newline='') as file:
            for item in output:
                values = item[1]
                values = list(dict.fromkeys(values))
                file.write(str(item[0]) + ":")
                for val in values:
                    file.write(" " + str(val))
                if item != output[-1]:
                    file.write("\n")

