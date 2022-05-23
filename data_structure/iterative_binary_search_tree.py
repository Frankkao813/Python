class TreeNode:
    def __init__(self, val='A', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def search(self, val):
        curr_node = self.root
        while(curr_node != None and val != curr_node.val):
            if(val < curr_node.val):
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
        if(curr_node != None):
            return True # we have found the node
        else:
            return False # we failed to find the node

    def insert(self, val):
        # https://www.adamsmith.haus/python/answers/how-to-call-an-instance-method-in-the-same-class-in-python
        if(self.search(val) == True):
            return False # There are already the same nodes
        
        y = None # new parents
        x = self.root # soldiers
        z = TreeNode(val) # establish a new treenode
        while(x != None):
            y = x
            if(z.val < x.val):
                x = x.left
            else:
                x = x.right

        if(y == None):
            self.root = z
        elif(z.val < y.val):
            y.left = z
        else:
            y.right = z

        return True
    
    # https://cloud.tencent.com/developer/article/1794041
    def delete(self, val):
        if(self.root == None or self.search(val) == False):
            return False

         # the parent will not be none unless the node is at the root
        curr_parent, curr_node = self.ReturnNodes(val)
        self._delete(curr_parent, curr_node)
        return True


    def _delete(self, curr_parent, curr_node):
        # print("We have found the node! The node is {} and the parent is {}".format(curr_node.val, curr_parent))
        # start to separate the cases
        if(curr_node.left == None and curr_node.right == None): # no children
            self.delete_no_child(curr_parent, curr_node)
        elif(curr_node.left == None or curr_node.right == None): # only one children
            self.delete_one_child(curr_parent, curr_node)
        else: # there are two children
            rear_parent, rear_curr = self.inorderSuccessor(curr_node.right, curr_node)
            curr_node.val = rear_curr.val
            self._delete(rear_parent, rear_curr)
        

    
    # Feel free to add any function here.
    # ===============================================================
    def ReturnNodes(self, val):
        '''
        The method that will return the node we want to search and its parent
        '''
        if(self.root ==  None):
            return False # It shouldn;t be achieved...
        curr_node = self.root
        curr_parent = None # the parent will be none unless the node is at the root
        while(curr_node != None and val != curr_node.val):
            if(val < curr_node.val):
                curr_parent = curr_node
                curr_node = curr_node.left
            else:
                curr_parent = curr_node
                curr_node = curr_node.right
        return (curr_parent, curr_node)

    def inorderSuccessor(self, node, curr_node):
        '''
        return the inorder successor and its parent
        '''
        curr_successor = node
        curr_successor_parent = None
        while(curr_successor.left != None):
            curr_successor_parent = curr_successor
            curr_successor = curr_successor.left
        
        if(curr_successor_parent == None):
            curr_successor_parent = curr_node


        return (curr_successor_parent, curr_successor)

    def delete_no_child(self, curr_parent, curr_node):
        if(curr_parent == None): # there is only one node  # if other two scenarios on the top - will cause error
            self.root = None
        elif(curr_parent.left == curr_node):
            curr_parent.left = None
        else: # curr_parent.right == curr_node
            curr_parent.right = None

    def delete_one_child(self, curr_parent, curr_node):
        if(curr_node.left != None): # children at the left node
            if(curr_parent != None and curr_parent.right == curr_node):
                curr_parent.right = curr_node.left
            elif(curr_parent != None and curr_parent.left == curr_node):
                curr_parent.left = curr_node.left
            else: # we delete the root node
                self.root = curr_node.left
                curr_node.left = None
        else: # children at the right node
            if(curr_parent != None and curr_parent.right == curr_node):
                curr_parent.right = curr_node.right
            elif(curr_parent != None and curr_parent.left == curr_node):
                curr_parent.left = curr_node.right
            else:
                self.root = curr_node.right
                curr_node.right = None

    # ===============================================================
    
    def print_tree(self):
        '''
        Print the nodes in BST by preorder traversal.
        '''
        def helper(node):
            print(node.val, end=' ')
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        if self.root is None:
            print('Tree is empty.')
        else:
            helper(self.root)
            print()
        
myBST = BST()
# myBST.print_tree()
myBST.insert('C')
myBST.insert('O')
myBST.insert('M')
myBST.insert('P')
myBST.insert('U')
myBST.insert('T')
myBST.insert('E')
myBST.insert('R')


#myBST.print_tree()
