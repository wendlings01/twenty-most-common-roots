from sys import argv
from os import path
from collections import defaultdict
from nltk.stem.porter import PorterStemmer

def convert_file_to_stemmed_word_count_dict(file_path, stop_words=defaultdict(int)):
    word_counts = defaultdict(int)
    stemmer = PorterStemmer()
    
    # extract all words at once to minimize time with the file open
    if not path.exists(file_path):
        return word_counts
    
    lines = None
    # read the target file line by line
    with open(file_path, 'r') as reader:
        lines = reader.readlines()
    

    for line in lines:
        # clean off whitespace, drop all non-alphabetical characters
        for word in line.split():
            # I checked the performance of this vs using a replacement regex. It seems similar when the regex
            # engine caches(?) the expression, but before that this is around 100-1000x faster on my machine
            alpha_word = ''.join([i for i in word if i.isalpha()]).lower()
            stemmed_word = stemmer.stem(alpha_word)
            if stemmed_word and not stop_words[stemmed_word]:
                word_counts[stemmed_word] += 1

    return word_counts

def main():
    stop_words_file = argv[1]
    text_file = argv[2]

    stop_words = convert_file_to_stemmed_word_count_dict(stop_words_file)
    

if __name__ == "__main__":
    main()