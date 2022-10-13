# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from sa import search_array


def test_search_tree_simple():
    '''Test the search_tree function with simple strings and patterns'''

    string = 'abcdeabcdeabced'
    pattern = 'ab'
    expectations = [0,5,10]
    results = search_array(string, pattern)
    assert(sorted(results)==sorted(expectations))

    pattern = 'cde'
    expectations = [2,7]
    results = search_array(string, pattern)
    assert(sorted(results)==sorted(expectations))

    pattern = ''
    expectations = []
    results = search_array(string, pattern)
    assert(sorted(results)==sorted(expectations))

