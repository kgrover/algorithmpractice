# Longest Common Subsequence

s1 = "racecar"
s2 = "car"

def lcs(s1, s2):

    l1 = len(s1)
    l2 = len(s2)
    
    if (l1 == 0 or l2 == 0):
        return 0
    
    # chop one character off at the end
    s1_cut = s1[:l1-1]
    s2_cut = s2[:l2-1]
    
    if (s1[l1 - 1] == s2[l2 - 1]):
        return 1 + lcs(s1_cut, s2_cut)
    else:
        return max(lcs(s1_cut, s2), lcs(s1, s2_cut))

print lcs(s1, s2)
    