from __future__ import division # need this in python 2.X
def get_at_content(dna, sigfigs): # second argument, sigfigs, works with the round() function
    length = len(dna) 
    n_count = dna.upper().count('N')
    a_count = dna.upper().count('A') + n_count / 4 # I have no idea how to factor N's into this calculation actually
    t_count = dna.upper().count('T') + n_count / 4 # I probably would have just ignored the N's for calculating AT content
    at_content = (a_count + t_count) / length
    return round(at_content, sigfigs) # round() only means a max number of 
#decimal places; it will still print e.g. 0.5 when it should print 0.500 if
#we have 3 sigfigs

#oh, we should remove N's entirely
#could let length = the count of A's, T's, C's, and G's, or remove the N's from the sequence
