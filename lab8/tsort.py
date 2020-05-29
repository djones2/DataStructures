from sys import argv
from stack_array import *


def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.'''
    # No connecting vertices
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    # Odd number of vertices
    elif len(vertices) % 2 == 1:
        raise ValueError("input contains an odd number of tokens")
    res = []
    # Stack
    stack = Stack(len(vertices))
    # Dictionary of adjacency list 
    (adjacency_list, ordered_list) = get_adj_list(vertices)
    # Initail in-degree of 0
    for vertex in ordered_list:
        if adjacency_list[vertex]["in-degree"] == 0:
            stack.push(vertex)
    # Push and pop to get resulting topological sort
    while stack.is_empty() is False:
        vertex1 = stack.pop()
        res.append(vertex1)
        # Reduce in-degree for adjacent vertices
        for vertex2 in adjacency_list[vertex1]["adjacency-list"]:
            adjacency_list[vertex2]["in-degree"] -= 1
            # Push to stack if in-degree results in 0
            if adjacency_list[vertex2]["in-degree"] == 0:
                stack.push(vertex2)
    # If resulting list is differenct length, 
    # cycle exists and not DAG
    if len(ordered_list) != len(res):
        raise ValueError("input contains a cycle")
    # Return formatted output
    return '\n'.join(res)

# Get the vertex, in-degree, and adjacency list in 
# a dictionary tuple
def get_adj_list(vertices):
    adj_dict = {}
    ordered_list = []
    for vert in range(0, len(vertices), 2):
        from_vert = vertices[vert]
        to_vert = vertices[vert + 1]
        if from_vert not in adj_dict:
            adj_dict[from_vert] = {"in-degree": 0, "adjacency-list": [to_vert]}
            ordered_list.append(from_vert)
        else:
            adj_dict[from_vert]["adjacency-list"].append(to_vert)
        if to_vert not in adj_dict:
            adj_dict[to_vert] = {"in-degree": 1, "adjacency-list": []}
            ordered_list.append(to_vert)
        else:
            adj_dict[to_vert]["in-degree"] += 1
    return (adj_dict, ordered_list)


# def main():
#     '''Entry point for the tsort utility allowing the user to specify
#        a file containing the edge of the DAG'''
#     if len(argv) != 2:
#         print("Usage: python3 tsort.py <filename>")
#         exit()
#     try:
#         f = open(argv[1], 'r')
#     except FileNotFoundError as e:
#         print(argv[1], 'could not be found or opened')
#         exit()

#     vertices = []
#     for line in f:
#         vertices += line.split()

#     try:
#         result = tsort(vertices)
#         print(result)
#     except Exception as e:
#         print(e)


# if __name__ == '__main__':
#     main()
