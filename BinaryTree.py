class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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
        if self.left:
            self.left.preorder()
        print( self.data)
        if self.right:
            self.right.preorder()

    def inorder(self):
        pass



    



root = BinarySearchTree(27)

root.insert(5)
root.insert(3)
root.insert(7)
root.insert(10)
root.insert(19)
root.preorder()
print("\n")
root.inorder()



