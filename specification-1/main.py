from operator import itemgetter

import matplotlib.pyplot as plt

def read_file_content(filepath):
    with open(filepath, 'r') as fp:
        return fp.read()

def cleanword(part):
    r = ''
    for c in part:
        if c.isalpha():
            r+=c
    return r

def split_words(content):
    parts = content.split()
    words = []
    for part in parts:
        part = part.strip()
        word = cleanword(part)
        if word=='':
            continue
        words.append(word.lower())
    return words

def character_freq_analysis(words):
    freq_dict = dict()
    alphatable = 'abcdefghijklmnopqrstuvwxyz'
    for c in alphatable:
        freq_dict[c] = 0

    for word in words:
        for c in word:
            if c in alphatable:
                freq_dict[c] += 1

    return freq_dict

def word_freq_analysis(words):
    freq_dict = dict()
    for word in words:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    return freq_dict

def plot_character_freq(freq_dict):
    alphatable = list('abcdefghijklmnopqrstuvwxyz')
    freq = []
    for c in alphatable:
        freq.append(freq_dict[c])

    plt.bar(x=alphatable, height=freq)
    plt.title('Character Frequency Analysis')
    plt.xlabel('Character')
    plt.ylabel('Total Appears Count')
    plt.show()


def most_freq_words(freq_dict, outfile, count):
    with open(outfile, 'w', encoding='utf-8') as fp:
        words_tup = [(word, count) for word, count in freq_dict.items()]
        words_tup.sort(key=itemgetter(1), reverse=True)
        fp.write('Word,Frequency\n')
        for word, count in words_tup[:count]:
            fp.write('{},{}\n'.format(word, count))

if __name__ == '__main__':
    content = read_file_content('book.txt')
    words = split_words(content)
    character_freq = character_freq_analysis(words)
    word_freq = word_freq_analysis(words)
    plot_character_freq(character_freq)
    most_freq_words(word_freq, 'out.csv', 100)
