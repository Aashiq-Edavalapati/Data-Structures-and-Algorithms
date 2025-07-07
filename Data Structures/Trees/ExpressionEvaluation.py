class BinaryTree:
    class Node:
        def __init__(self) -> None:
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None
    
    def __init__(self) -> None:
        self.sz = 0
        self.root = self.Node()

    def isExternal(self,curnode):
        if curnode.leftchild == None and curnode.rightchild == None:
            return True
        return False
    
    def buildTree(self, eltlist):
        nodelist = [None]  # Start index at 1 to simplify parent-child indexing
        for i in range(1, len(eltlist)):
            if eltlist[i] != -1:
                # Create the node and assign its element
                tempnode = self.Node()
                tempnode.element = eltlist[i]

                # Determine its parent if it's not the root
                if i != 1:
                    parent_index = i // 2

                    # Ensure the parent exists and is not None
                    if nodelist[parent_index] is not None:
                        tempnode.parent = nodelist[parent_index]

                        # Attach the node to the parent
                        if i % 2 == 0:
                            nodelist[parent_index].leftchild = tempnode
                        else:
                            nodelist[parent_index].rightchild = tempnode
                
                nodelist.append(tempnode)
                self.sz += 1
            else:
                # Append None for missing nodes to maintain proper indexing
                nodelist.append(None)
        
        # The root of the tree is the first node in the list
        self.root = nodelist[1]
        return nodelist

    def displayTree(self):
        def display(node,level):
            if not node:
                return
            
            display(node.rightchild,level + 1)

            if level != 0:
                for _ in range(level - 1):
                    print('\t\t',end='')
                print('|-------->',node.element)
            else:
                print(node.element)
            
            display(node.leftchild,level + 1)

        display(self.root,0)
    
    def printExpression(self, root):
        """
            Prints the expression represented by binary tree.
        """
        # Base Case
        if not root:
            return
        
        # If the node is internal node, then print "(" and traverse left subtree.
        if root.leftchild != None or root.rightchild != None:
            print('(',end='')
            self.printExpression(root.leftchild)
        
        # After traversing the left subtree, print the node.
        print(root.element,end='')

        # If the node is internal node, then traverse through right subtree and then print ")"
        if root.leftchild != None or root.rightchild != None:
            self.printExpression(root.rightchild)
            print(')',end='')
    
    def evaluateExpression(self, root):
        """
            Evaluates expression represented by binary tree.
        """
        # If current node is a leaf node then it will be an operand, so return it.
        if not root.leftchild and not root.rightchild:
            return root.element
        x = self.evaluateExpression(root.leftchild)
        y = self.evaluateExpression(root.rightchild)
        o = root.element # Every internal node will be an operator.
        # Perform and return the specified operation.
        if o == '+':
            return x + y
        elif o == '-':
            return x - y
        elif o == '*':
            return x * y
        elif o == '/':
            return x / y



if __name__ == '__main__':
    # arr = ['','+','*','-','3','/','17','5',-1,-1,'+','4',-1,-1,-1,-1,1,-1,-1,-1,'7','1']
    arr = ['','+','*','-',3,'/',17,5,-1,-1,'+',4,-1,-1,-1,-1,1,-1,-1,-1,7,1]

    tree = BinaryTree()
    tree.buildTree(arr)
    tree.displayTree()
    tree.printExpression(tree.root)
    print(' = ',tree.evaluateExpression(tree.root))