
def parse_digrams(string):
   return map(''.join, zip(string[:-1], string[1:]))

from collections import defaultdict
def build_index(digrams):
    index = defaultdict(list)
    for k,v in enumerate(digrams):
        index[v].append(k)
    return index

def get_repeated_digram_distances(index):
    return ((k, v[-1] - v[0]) for k,v in index.items() if len(v) > 1)

def get_max_distance_digram(string):
   dig_dist = list(get_repeated_digram_distances(build_index(parse_digrams(string))))
   if len(dig_dist) == 0:
       return -1
   return max(dig_dist, key= lambda d: d[1])
