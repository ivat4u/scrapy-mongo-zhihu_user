class Node:
    def __init__(self,number):
        self.number=number
        self.lchild=None
        self.rchild=None
class Tree:
    lis=[]
    def __init__(self):
        self.root=None

    def add(self,number):
        node=Node(number)
        if self.root==None:
            self.root=node
            self.lis.append(node)
        else:
            point = self.lis[0]
            if (point.lchild==None):
                point.lchild=node
                self.lis.append(node)
            elif(point.rchild==None):
                point.rchild=node
                self.lis.append(node)
                self.lis.pop(0)
if __name__=='__main__':
    t=Tree()
    L = [1,2,3,4,5,6,7]
    for x in L:
        t.add(x)
        print ('success')
