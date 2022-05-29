# Some examples how to use NLTK with the Wordnet synsets
# NLTK homepage: https://www.nltk.org/
# import nltk

from nltk.corpus import wordnet
from nltk.corpus import names
import random

# Downloading either with interactive downloader or directly by stating the module,
# has to be only done once and can be commented out after the download


#nltk.download()  # using the interactive downloader
#nltk.download('wordnet')  # downloading the specific package without interactive downloader
#nltk.download('names')


# Task1
def generate_names(char, num):
    if type(char) != str or len(char) != 1:
        raise TypeError("first argument must be a string of length 1 -->  a single character")
    if type(num) != int or num < 1:
        raise TypeError("second argument must be an integer and greater than 0")
    female_names = [(name, 'female') for name in names.words('female.txt') if name.startswith(char)]
    male_names = [(name, 'male') for name in names.words('male.txt') if name.startswith(char)]
    random.shuffle(female_names)
    random.shuffle(male_names)
    female_names = female_names[0:num]
    male_names = male_names[0:num]
    print(female_names)
    print(male_names)

    # Task2
    with open('female_names.txt', 'w') as f_female_names:
        for ele in female_names:
            f_female_names.write(ele[0] + "\n")
    with open('male_names.txt', 'w') as f_male_names:
        for ele in male_names:
            f_male_names.write(ele[0] + "\n")


generate_names('D', 5)


# Task3

class SynAnt:
    def __init__(self, word_list):
        self.word_list = word_list
        self.synonyms = dict()
        self.antonyms = dict()

    def find_synonyms(self):
        print("Getting Synonyms")
        for index, word in enumerate(self.word_list):
            syns = wordnet.synsets(word)
            syns_list = []
            if len(syns) == 0:
                self.synonyms[word] = "No synonyms found in wordnet"
            else:
                for syn in syns:
                    for l in syn.lemmas():
                        syns_list.append((l.name()))
                self.synonyms[word] = syns_list
            print("Word: {0} | Synonyms: {1}".format(word, self.synonyms[word]))

    def find_antonyms(self):
        print("Getting Antonyms")
        for index, word in enumerate(self.word_list):
            syns = wordnet.synsets(word)
            antonyms_list: list = []
            for syn in syns:
                for l in syn.lemmas():
                    if l.antonyms():
                        antonyms_list.append((l.antonyms()[0].name()))
            if len(antonyms_list) == 0:
                self.antonyms[word] = "No antonyms found in wordnet"
            else:
                self.antonyms[word] = antonyms_list
            print("Word: {0} | Antonyms: {1}".format(word, self.antonyms[word]))


syn_ant = SynAnt(["home", "magic", "cat", "human"])
syn_ant.find_synonyms()
syn_ant2 = SynAnt(["always", "colorful", "joyful", "short"])
syn_ant2.find_antonyms()



