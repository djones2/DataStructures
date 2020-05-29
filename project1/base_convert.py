def convert(num, b):
    """Recursive function that returns a string 
    representing num in the base b"""
    # Quotient and remainder calculations
    quotient = num // b
    remainder = num % b
    # Indexing to symbol list for bases larger than 10
    if remainder >= 10:
        index = remainder % 10
        symbols = ['A', 'B', 'C', 'D', 'E', 'F']
        remainder = symbols[index]
    # Check if at end of recursion
    if quotient == 0:
        return str(remainder)
    else:
        # Format return value 
        return str(convert(quotient, b)) + str(remainder)
