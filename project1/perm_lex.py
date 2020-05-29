def perm_gen_lex(a): 
    """ Returns a list of strings that represent every 
    permutation of input sting. """
    # Resultant list
    res = []
    # Check empty input sting
    if len(a) == 0:
        return res
    # Check input string with single character
    elif len(a) == 1:
        res.append(a)
        return res
    else:
        # For each character in input string
        for char in a:
            # Attain simple string by removing character
            # from input string
            simple_string = a.replace(char, '')
            # Generate permuations recursively
            permutations = perm_gen_lex(simple_string)
            # Add removed character to beginning of each permutation
            for word in permutations:
                word = char + word 
                res.append(word)
        return res
