class Treenode:
    def __init__(self,root):
        self.root=root
        self.left=None
        self.right=None
    
    def morris_inorder(self):
        curr=root
        while curr!=None:
            if curr.left==None:
                print(curr.root)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if prev.right==None:
                    prev.right=curr
                    curr=curr.left
                else:
                    prev.right=None
                    print(curr.root)
                    curr=curr.right




        
root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.left = Treenode(4)
root.left.right = Treenode(5)

root.morris_inorder()
