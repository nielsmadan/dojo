import anagrams

from nose.tools import eq_


def test_is_anagram():
    eq_(anagrams.is_anagram("abc", "cba"), True)

def test_is_anagram_false():
    eq_(anagrams.is_anagram("a", "b"), False)

def test_is_anagram_false_different_capitalization():
    eq_(anagrams.is_anagram("A", "a"), False)

def test_is_anagram_multiple_letter_the_same():
    eq_(anagrams.is_anagram("aa", "aaa"), False)

def test_find_anagrams_of_word():
    eq_(anagrams.find_anagrams("cba", ("aaa", "abc")), ["abc"])

def test_find_anagrams_of_word_word_itself():
    eq_(anagrams.find_anagrams("cba", ("cba", "abc")), ["cba", "abc"])

def test_find_anagrams_of_word_multiple():
    eq_(anagrams.find_anagrams("cba", ("aaa", "abc", "bca")), ["abc", "bca"])

def test_find_anagrams_of_word_does_not_exist():
    eq_(anagrams.find_anagrams("cba", ("aaa", "asc")), [])

def test_find_all_anagrams():
    word_list = ["abc", "dqa", "bca"]

    eq_(anagrams.find_all_anagrams(word_list), set([frozenset(("abc", "bca"))]))

def test_find_all_anagrams_three_anagrams():
    word_list = ["abc", "dqa", "bca", "cba"]

    eq_(anagrams.find_all_anagrams(word_list), set([frozenset(("abc", "bca", "cba"))]))

def test_find_all_anagrams_same_word_multiple():
    word_list = ["abc", "abc", "abc", "abc"]

    eq_(anagrams.find_all_anagrams(word_list), set())

def test_find_all_anagrams_two_sets_of_two():
    word_list = ["abc", "dqa", "bca", "qad"]

    eq_(anagrams.find_all_anagrams(word_list), set([frozenset(("abc", "bca")), frozenset(("dqa", "qad"))]))
