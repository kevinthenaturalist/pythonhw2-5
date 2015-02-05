from __future__ import division # need this in python 2.X
def get_at_content(dna, sigfigs): # second argument, sigfigs, works with the round() function
    length = len(dna)
    n_count = dna.upper().count('N')
    a_count = dna.upper().count('A') + n_count / 4 # I have no idea how to factor N's into this calculation actually
    t_count = dna.upper().count('T') + n_count / 4 # I probably would have just ignored the N's for calculating AT content
    at_content = (a_count + t_count) / length
    return round(at_content, sigfigs)
