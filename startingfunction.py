from __future__ import division # need this in python 2.X
def get_at_content(dna):
    length = len(dna) #dna variable must be a string
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content
