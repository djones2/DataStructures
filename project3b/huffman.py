from os import path
import time

# Huffman node class.
class HuffmanNode:
    # Initialize with the character, its frequency, and its child nodes.
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    # Helper function to set left child.
    def set_left(self, node):
        self.left = node

    # Helper function to set right child.
    def set_right(self, node):
        self.right = node

    # Comparison function, returns less than operation between nodes.
    def __lt__(self, other):
        return comes_before(self, other)

# Determines which nodes comes before the other.
def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq == b.freq:
        return a.char < b.char
    else:
        return a.freq < b.freq

# Combines two nodes.
def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    if a.char < b.char:
        ch = a.char
    else: 
        ch = b.char
    node = HuffmanNode(ch, a.freq + b.freq)
    node.set_left(a)
    node.set_right(b)
    return node

# Counts the frequency of characters in a given input file.
def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    array = [0]*256
    with open(filename) as f:
        for character in f.read():
            array[ord(character)] += 1
    return array

# Creates huffman tree based on characters and their frequencies.
def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    nodes = []
    for i in range(256):
        if char_freq[i] != 0:
            nodes.append(HuffmanNode(i, char_freq[i]))
    return create_huff_tree_helper(nodes)

# Helps create tree recursively. 
def create_huff_tree_helper(nodes):
    if len(nodes) == 1:
        return nodes[0]
    elif len(nodes) == 0:
        return [0]
    else:
        nodes.sort()
        first = nodes.pop(0)
        second = nodes.pop(0)
        new_node = combine(first, second)
        nodes.insert(0, new_node)
        return create_huff_tree_helper(nodes)

# Create huffman codes based on the huffman tree.
def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    codes = ['']*256
    for i in range(256):
        codes[i] = create_code_helper(node, i)
    for j in range(256):
        if codes[j] == None:
            codes[j] = ''
    return codes

# Helps create codes recursively.
def create_code_helper(node, i):
    if node == None:
        return ''
    else:
        if node.char == i and (node.left == None and node.right == None):
            return ''
        else:
            left = create_code_helper(node.left, i)
            right = create_code_helper(node.right, i)
            if left == None and right == None:
                return None
            elif left == None:
                return '1' + right
            elif right == None:
                return '0' + left

# Create header for output text file that maps huffman encoding.
def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header = []
    for i in range(256):
        if freqs[i] != 0:
            header.append(str(i) + ' ' + str(freqs[i]))
    return ' '.join(header)

# Creates encoded file from input file.
def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    if path.exists(in_file) == False:
        raise FileNotFoundError
    file_in = open(in_file, 'r')
    data = file_in.read()
    file_out = open(out_file, "w", newline='')
    if (data == ''):
        file_out.write('')
    else:
        freqs = cnt_freq(in_file)
        tree = create_huff_tree(freqs)
        encoding = create_code(tree)
        header = create_header(freqs)
        results = []
        file_out.write(header + '\n')
        for character in data:
            results.append(encoding[ord(character)])
        file_out.write(''.join(results))
    file_out.close()
    file_in.close()

# Decodes encoded input file, outputs initial file.
def huffman_decode(encoded_file, decode_file):
    """ Decodes encoded file, writes it to decode file """
    if path.exists(encoded_file) == False:
        raise FileNotFoundError
    with open(encoded_file, 'r') as to_decode:
        line = to_decode.readline()
        header = line.strip()
    freq_list = parse_header(header)
    huff_tree = create_huff_tree(freq_list)
    with open(decode_file, "w", newline='') as decoded_file:
        with open(encoded_file, 'r') as to_decode:
            code = to_decode.readlines()[1:]
            if code == []:
                code.append('')
            code = code[0]
        if code == '':
            if huff_tree == [0]:
                decoded_file.write('')
            else:
                freq = 0
                while freq < huff_tree.freq:
                    decoded_file.write(chr(huff_tree.char))
                    freq += 1
        else:
            i = 0
            current = huff_tree
            while i < len(code):
                if current.left == None and current.right == None:
                    decoded_file.write(chr(current.char))
                    current = huff_tree
                if code[i] == '1':
                    current = current.right
                else:
                    current = current.left
                i += 1
                if i == len(code) and (current.left == None and current.right == None):
                    decoded_file.write(chr(current.char))
                
# Parses header of encoded file, outputs frequency list.
def parse_header(header_string):
    """ Takes in input header string and returns Python list (array)
    of frequencies (256 entry list, indexed by ASCII value of character) """
    freq_list = header_string.split()
    list_of_freqs = [0] * 256
    i = 0
    while i < len(freq_list):
        if i % 2 == 0:
            index = int(freq_list[i])
        else:
            list_of_freqs.insert(index, int(freq_list[i]))
        i += 1
    return list_of_freqs

