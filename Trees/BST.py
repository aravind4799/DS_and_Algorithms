class node:
    def __init__(self,val):
        self.l=None
        self.val=val
        self.r=None
    
    def isequal(self,val):
        if self.val==val:
            return True
        else:
            return False

class BST:
    def __init__(self):
        self.root=None
    
    def insert(self,val):
        if self.root==None:
            self.root=node(val)
        else:
            self._insert(self.root,val)
    
    def _insert(self,n,val):
        if(n.val>val):
            if(n.l!=None):
                self._insert(n.l,val)
            else:
                n.l = node(val)
        else:
            if(n.r!=None):
                self._insert(n.r,val)
            else:
                n.r = node(val)
    
    def find(self,val):
        if self.root==None:
            return
        else:
            self._find(val,self.root)
    
    def _find(self,val,node):
        if val==node.val:
            return node
        elif val<node.val and node.l!=None:
            self._find(val,node.l)
        elif val>node.val and node.r!=None:
            self._find(val,node.r)
        
    def delete_tree(self):
        self,root=None
        #garbage collector does the job

    def print_tree(self):
        if self.root==None:
            return
        else:
            self._print(self.root)
    
    #inorder_traversal
    def _print(self,node):
        if(node!=None):
            self._print(node.l)
            print( str(node.val),end=" ")
            self._print(node.r)


tree=BST()
tree.insert(6)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(9)

tree.print_tree()