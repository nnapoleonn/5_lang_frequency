import re
from string import punctuation
from collections import Counter
import sys


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    the_processed_text = re.sub('[0-9{0}]'.format(punctuation), '', text.lower())
    words_list = the_processed_text.split()
    words = Counter(words_list)
    top_words_limit = 10
    return words.most_common(top_words_limit)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Path to file is not found!')
    file_path = sys.argv[1]
    try:
        text = load_data(file_path)
        most_frequent_words = get_most_frequent_words(text)
        print('Top 10 words in text: ')
        for word, amount in most_frequent_words:
            print('{0}-{1}'.format(word, amount))
    except FileNotFoundError:
        sys.exit('File not found')
