class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def isEmpty(self):
        return self.data is False


    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
                return
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)
                return


    def search(self, val):
        if val==self.data:
            return str(val)+" is found"
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return str(val)+" is not found"

        else:
            if self.right:
                return self.right.search(val)
            else:
                return str(val)+" is not found" 
       

    def preorder(self):
        print( self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print( self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print( self.data)






    



root = BinarySearchTree(1)
root.insert(3)
root.insert(7)
root.insert(9)
root.preorder()
print("\n")
root.inorder()
print("\n")
root.postorder()
print(root.isEmpty())


