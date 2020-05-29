from os import path
import time

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def __lt__(self, other):
        return comes_before(self, other)

def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq == b.freq:
        return a.char < b.char
    else:
        return a.freq < b.freq

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

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    array = [0]*256
    with open(filename) as f:
        for character in f.read():
            array[ord(character)] += 1
    return array

def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    nodes = []
    for i in range(256):
        if char_freq[i] != 0:
            nodes.append(HuffmanNode(i, char_freq[i]))
    return create_huff_tree_helper(nodes)

def create_huff_tree_helper(nodes):
    if len(nodes) == 1:
        return nodes[0]
    else:
        nodes.sort()
        first = nodes.pop(0)
        second = nodes.pop(0)
        new_node = combine(first, second)
        nodes.insert(0, new_node)
        return create_huff_tree_helper(nodes)

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

def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    header = []
    for i in range(256):
        if freqs[i] != 0:
            header.append(str(i) + ' ' + str(freqs[i]))
    return ' '.join(header)


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
