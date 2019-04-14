# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # python set for no duplication
    s = set()
    
    # find and add substrings from two string
    for sub in s1:
        if sub in s2:
            s.add(sub)

    if len(s) > 0:
        return 'YES'
    else:
        return 'NO'
