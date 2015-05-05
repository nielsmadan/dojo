from collections import defaultdict


def is_anagram(x, y):
    x = sorted(x)
    y = sorted(y)
    return x == y

def find_anagrams(search_word, word_list):
    return [word for word in word_list
                 if is_anagram(search_word, word)]

def find_all_anagrams(word_list):
    return set([frozenset(find_anagrams(word, word_list)) for word in word_list
                                                          if len(set(find_anagrams(word, word_list))) > 1])

def find_all_anagrams_b(word_list):
    d = defaultdict(set)

    for word in word_list:
        d[''.join(sorted(word))].add(word)

    return set([frozenset(value) for value in d.itervalues() if len(value) > 1])
