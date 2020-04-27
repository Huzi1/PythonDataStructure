class Node(object):

    def __init__(self, value):
        self.value = value
        # self.adjacentList = []
        # self.isUni = False
        self.left = None
        self.right = None
        # self.visited = False;
        # self.pred = None;

class CountUnival(object):

    def __init__(self):
        self.count = 0 

    def boolHelper(self, node):

        if node is None:
            return True

        left = self.boolHelper(node.left);
        right = self.boolHelper(node.right);

        if right == left:
            if ((node.left != None) and (node.left.value != node.value)) or ((node.right != None) and (node.right.value != node.value)):

                return False

            self.count +=1;
            return True;

        else:

            return False
        


    def main(self,node):

        self.boolHelper(node);
        print(self.count)  

        
             

root = Node("5")
node1 = Node("1") 
node2 = Node("5") 
node3 = Node("5") 
node4 = Node("5")
node5 = Node("5")

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5

chk = CountUnival().main(root)