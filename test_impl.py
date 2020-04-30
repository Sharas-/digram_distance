from impl import *

def test_0_digrams_when_one():
    res = parse_digrams("s")
    assert list(res) == [] 

def test_0_digrams_when_empty():
    res = parse_digrams("")
    assert list(res) == []
 
def test_1_digrams():
    res = parse_digrams("we")
    assert list(res) == ["we"]

def test_2_digrams():
    res = parse_digrams("abs")
    assert list(res) == ["ab", "bs"]

def test_3_digrams():
    res = parse_digrams("absd")
    assert list(res) == ["ab", "bs", "sd"]

def test_index_3_same_separated_digrams():
    s = "xaafwsaathwlaa"
    res = build_index(parse_digrams(s))
    expected = {'aa': [1, 6, 12], 'af': [2], 'at': [7], 'fw': [3], 'hw': [9], 'la': [11], 'sa': [5], 'th': [8], 'wl': [10], 'ws': [4], 'xa': [0]}
    assert res == expected

def test_index_2_same_adjacent_digrams():
    s = "aaa"
    res = build_index(parse_digrams(s))
    expected = {'aa': [0, 1]}
    assert res == expected

def test_index_2_digrams():
    s = "digrasgrfkas"
    res = build_index(parse_digrams(s))
    expected = {'di': [0], 'ig': [1], 'gr': [2, 6], 'ra': [3], 'as': [4, 10], 'sg': [5], 'rf': [7], 'fk': [8], 'ka': [9]}
    assert res == expected

def test_index_3_pairs_same_dist_digrams():
    s = "aaxxaaxx"
    res = build_index(parse_digrams(s))
    expected = {'aa': [0, 4], 'xx': [2, 6], 'ax': [1,5], 'xa': [3]} 
    assert res == expected

def test_index_0_digrams():
    s = "abcd"
    res = build_index(parse_digrams(s))
    expected = {'ab': [0], 'bc': [1], 'cd': [2]}
    assert res == expected

def test_distances_2_digrams():
    s = "digrasgrfkas"
    res = get_repeated_digram_distances(build_index(parse_digrams(s)))
    expected = [('gr', 4), ('as', 6)]
    assert set(res) == set(expected)

def test_distances_0_digrams():
    s = "abcdef"
    res = list(get_repeated_digram_distances(build_index(parse_digrams(s))))
    expected = []
    assert res == expected

def test_max_2_digrams():
    assert get_max_distance_digram("digrasgrfkas") == ('as', 6)

def test_max_0_digrams():
    assert get_max_distance_digram("abcdef") == -1

def test_max_2_same_separated_digrams():
    assert get_max_distance_digram("aabcaabcabda") == ('ab', 7)

def test_max_2_same_overlaping_digrams():
    assert get_max_distance_digram("aaa") == ('aa', 1)

def test_max_2_pairs_same_distance_digrams():
    (_, dist) = get_max_distance_digram("aaxxaaxx")
    assert dist == 4

