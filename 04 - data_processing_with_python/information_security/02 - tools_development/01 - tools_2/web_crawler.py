"""
    Programa que utiliza as bibliotecas 'requests', 'BeautifulSoup', operator' e 'colletions' para implementar
    um web crawler que conta as palavras mais frequentes em uma página da web específica.
"""
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('div', {'class': 'wrapper single-page'}):
        content = each_text.text
        words = content.lower().split()
        wordlist.extend(words)

    clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []
    symbols = '!@#$%¨&*^()_-+={}[]|;:"<>?/.,\\'

    for word in wordlist:
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print("%s : %s" % (key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language-tutorial/")
