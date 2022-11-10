class binarytree( ):
    def __init__(self,pContent = None ,pLefttree = None,pRighttree = None):
        self.content = pContent
        self.lefttree = pLefttree
        self.righttree = pRighttree

    def empty(self):
        if self.content :
            return False 
        else:
            return True


    def setcontent(self,tempcon):   
        if self.epmty():
            self.content = tempcon

        else:
            self.content = tempcon
            self.lefttree = binarytree()
            self.righttree = binarytree()

    def getcon(self):
        print(self.content)

    def setlefttree(self,temptree):
        if temptree != None:
            if self.empty():
                return None
            else:
                self.lefttree = temptree
        else:
            return None

    def setrighttree(self,temptree):
        if temptree != None:
            if self.empty():
              return None
            else:
                self.righttree = temptree
        else:
            return None


    def getlefttree(self):
        if self.lefttree is None:
            return None
        else:
            return self.lefttree

    def getrighttree(self):
        if self.righttree is None:
            return None
        else:
            return self.righttree

    def preorder(self):
        self.getcon()
        if self.lefttree != None :
            self.lefttree.preorder()
        
        if self.righttree != None:
            self.righttree.preorder()
    

    def inorder(self):
        
        if self.lefttree != None:
            self.lefttree.inorder()

        self.getcon()
        

        if self.righttree != None:
            self.righttree.inorder()
    
        
    def postorder(self):
        if self.lefttree != None:
            self.lefttree.postorder()

        if self.righttree != None:
            self.righttree.postorder()

        self.getcon()
        
    def getpreorder(self) :
        print("Preorder:      ")
        self.preorder()
        

    def getinorder(self) :
        print("Inorder:      ")
        self.inorder()
    

    def getpostorder(self) :
        print("Postorder:      ")
        self.postorder()
      
    def getallorders(self):   
        self.getpreorder() 
        print("\n")
        self.getinorder()
        print("\n")
        self.getpostorder()

    def remove(self, searchcon):
        if self.content == searchcon:
            print("true")
        


  
baum_1= binarytree(5)
baum_1.setlefttree(binarytree(3))
baum_1.lefttree.setlefttree(binarytree(2))
baum_1.lefttree.setrighttree(binarytree(1))
baum_1.setrighttree(binarytree(7))
baum_1.righttree.setlefttree(binarytree(4))
            
baum_1.remove(5)