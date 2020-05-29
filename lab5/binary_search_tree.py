class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): 
        # Returns empty BST
        self.root = None

    def is_empty(self): 
        #returns True if tree is empty, else False
        if self.root == None:
            return True
        else:
            return False

    def search(self, key): 
    # returns True if key is in a node of the tree, else False
        if self.is_empty() == True:
            return False
        else:
            return self.search_2(self.root, key)

    # Recursive insert function 
    def search_2(self, current_node, key):
        if current_node.key == key:
            return True
        elif current_node.key > key:
            if current_node.left == None:
                return False
            else:
                return self.search_2(current_node.left, key)
        else:
            if current_node.right == None:
                return False
            else:
                return self.search_2(current_node.right, key)

    def insert(self, key, data=None): 
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        temp = TreeNode(key, data)
        if self.is_empty():
            self.root = temp
        else:
            self.insert_2(self.root, temp)

    # Recursive insert function 
    def insert_2(self, current_node, node):
        if current_node.key == node.key:
            current_node.data = node.data
        elif current_node.key > node.key:
            if current_node.left == None:
                current_node.left = node
            else:
                self.insert_2(current_node.left, node)
        else:
            if current_node.right == None:
                current_node.right = node
            else:
                self.insert_2(current_node.right, node)
    
    
    def find_min(self): 
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return current.key, current.data

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return current.key, current.data
    
    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        else:
            return self.height_calc(self.root) - 1

    def height_calc(self, current):
        if current == None:
            return 0
        else:
            left = self.height_calc(current.left)
            right = self.height_calc(current.right)
            if left > right:
                return left + 1
            else:
                return right + 1

    def inorder_list(self): 
        # return Python list of BST keys representing in-order traversal of BST
        return self.inorder(self.root)

    def inorder(self, current):
        res = []
        if current:
            res = res + self.inorder(current.left)
            res.append(current.key)
            res = res + self.inorder(current.right)
        return res
    
    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.preorder(self.root)

    def preorder(self, current):
        res = []
        if current:
            res.append(current.key)
            res = res + self.preorder(current.left)
            res = res + self.preorder(current.right)
        return res
    
    def delete(self, key): 
        # deletes node containing key
        # Will need to consider all cases 
        # This is the most difficult method - save it for last, so that
        # if you cannot get it to work, you can still get credit for 
        # the other methods
        # Returns True if the item was deleted, False otherwise
        # Empty tree
        if self.is_empty() == True:
            return False
        # Node doesn't exist
        elif self.search(key) == False:
            return False
        # Recurse through all options
        return self.delete_item(self.root, key)

    def delete_item(self, current, key):
        # Delete root node
        if current.key == key and current == self.root:
            # Root node has no children
            if self.tree_height() == 0:
                self.root = None
                return True
            # Root node has two children
            elif current.left != None and current.right != None:
                min = current.right
                while min.left is not None:
                    min = min.left
                self.delete(min.key)
                current.key = min.key
                current.data = min.data
                return True
            # Root node has one child
            else:
                if current.left == None:
                    self.root = current.right
                    return True
                else:
                    self.root = current.left
                    return True
        # Delete left child
        elif current.key > key:
            if current.left.key == key:
                # Left child has no children
                if current.left.left == None and current.left.right == None:
                    current.left = None
                    return True
                # Left child has two children
                elif current.left.left != None and current.left.right != None:
                    min = current.left.right
                    while min.left is not None:
                        min = min.left
                    self.delete(min.key)
                    current.left.key = min.key
                    current.left.data = min.data
                    return True
                # Left child has one child
                else:
                    if current.left.left == None:
                        current.left = current.left.right
                        return True
                    else:
                        current.left = current.left.left
                        return True
            else:
                return self.delete_item(current.left, key)
        # Delete right child
        else:
            if current.right.key == key:
                # Right child has no children
                if current.right.left == None and current.right.right == None:
                    current.right = None
                    return True
                # Right child has two children
                elif current.right.left != None and current.right.right != None:
                    min = current.right.right
                    while min.left is not None:
                        min = min.left
                    self.delete(min.key)
                    current.right.key = min.key
                    current.right.data = min.data
                    return True
                # Right child has one child
                else:
                    if current.right.left == None:
                        current.right = current.right.right
                        return True
                    else:
                        current.right = current.right.left
                        return True
            else:
                return self.delete_item(current.right, key)
    
    def postorder(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.postorder_list(self.root)

    def postorder_list(self, current):
        # return Python list of BST keys representing post-order traversal of BST
        res = []
        if current:
            res = res + self.postorder_list(current.left)
            res = res + self.postorder_list(current.right)
            res.append(current.key)
        return res

    def levelorder(self):
    # return Python list of BST keys representing level-order traversal of BST (use your queue
    # implementation for it)
        q = Queue(30)
        temp = self.root
        res = []
        while temp is not None:
            res.append(temp.key)
            if temp.left is not None:
                q.enqueue(temp.left)
            if temp.right is not None:
                q.enqueue(temp.right)
            if q.is_empty() is False:     
                temp = q.dequeue()
            else:
                temp = None
        return res

    def changeTreeRoot(self, key):
    # changes the current tree and make 
    # the node with the key (argument) the new root node. If
    # the key is not present in the Tree, leave the tree unchanged.
        if self.search(key) is False:
            return
        new = self.preorder_node_list()
        for item in new:
            if item.key == key:
                self.delete(item.key)
            if item.key is key:
                new_root = item
                new.remove(item)
        self.root = new_root
        for i in new:
            self.insert(i.key)

    def preorder_node_list(self):
        return self.preorder_nodes(self.root)

    def preorder_nodes(self, current):
        res = []
        if current:
            res.append(current)
            res = res + self.preorder_nodes(current.left)
            res = res + self.preorder_nodes(current.right)
        return res
    
    def mirror(self):
        new = self.preorder_node_list()
        to_insert = []
        for item in new:
            if item.key is self.root.key:
                print(item.key)
                continue
            else:
                to_insert.append(item)
                self.delete(item.key)
        for i in to_insert:
             self.insert_reverse(i.key, i.data)

    def insert_reverse(self, node, data=None): 
        temp = TreeNode(node, data)
        return self.insert_reverse_help(self.root, temp)

    # Recursive insert function 
    def insert_reverse_help(self, current_node, node):
        if current_node.key == node.key:
            current_node.data = node.data
        elif current_node.key < node.key:
            if current_node.left == None:
                current_node.left = node
            else:
                self.insert_reverse_help(current_node.left, node)
        else:
            if current_node.right == None:
                current_node.right = node
            else:
                self.insert_reverse_help(current_node.right, node)
    
    
if __name__ == '__main__': 
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(5)
    bst.insert(18)
    bst.insert(30)
    bst.insert(33)
    bst.insert(19)
    bst.insert(17)
    print(bst.inorder_list())
    bst.mirror()
    print(bst.inorder_list())