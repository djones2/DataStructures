from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

# Take an input postfix expression and return the evaluated result.
def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    stack = Stack(30)
    input = input_str.split()
    for item in input:
        temp = item.replace('.', '', 1)
        temp = temp.replace('-', '', 1)
        if item.isalpha():
            raise PostfixFormatException("Invalid token")
        elif temp.isdigit():
            stack.push(item)
        else:
            if stack.num_items < 2:
                raise PostfixFormatException("Insufficient operands")
            val1 = stack.pop()
            val2 = stack.pop()
            if item == '/' and val1 == '0' or val1 == '0.0':
                raise ValueError
            if (item == '>>' or item == '<<') and (val1.find('.') != -1 or val2.find('.') != -1):
                raise PostfixFormatException("Illegal bit shift operand")
            stack.push(str(eval(val2 + item + val1)))
    res = stack.pop()
    if stack.num_items > 0:
        raise PostfixFormatException("Too many operands")
    if res.find('.') is not -1:
        return float(res)
    else:
        return int(res)


# Helper functions to decide order of operations
def orderOfOperations(stack, i): 
    try: 
        orders = ['-', '+', '/', '*', '>>', '<<']
        a = orders.index(i) 
        b = orders.index(stack.peek())
        if a <= b:
            return True
        else:
            return False
    except ValueError:  
        return False

# Takes input infix expression and converts to postfix expression.
def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    output = []
    stack = Stack(30)
    input = input_str.split()
    for item in input:
        if item.isnumeric(): 
            output.append(item)
        elif item == '(':
            stack.push(item)
        elif item == ')':
            while ((not stack.is_empty()) and (stack.peek() != '(')):
                val1 = stack.pop()
                output.append(val1)
            try:
                stack.pop()
            except:
                raise PostfixFormatException("Insufficient operands")
        # an operator is encountered
        else: 
            while((not stack.is_empty()) and orderOfOperations(stack, item)): 
                output.append(stack.pop()) 
            stack.push(item) 
    # pop all the operator from the stack 
    while not stack.is_empty(): 
        output.append(stack.pop()) 
    return " ".join(output)

# Takes input prefix expression and converts to equivalent postfix expression.
def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    stack = Stack(30)
    operators = ['+', '-', '*', '/', '**']
    input = input_str.split()
    result = ""
    # Reversing the order 
    input_reverse = input[::-1]  
    # iterating through individual tokens 
    for item in input_reverse:               
        # if token is operator 
        if item in operators:           
            a = stack.pop() 
            b = stack.pop() 
            temp = a + b + item          
            stack.push(temp)  
        else:                 
            stack.push(item) 
    # printing final output 
    while not stack.is_empty():
        result = result + stack.pop()
    return " ".join(result)
