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

    def getChildren(self,curnode): 
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self,curnode):
        if curnode.leftchild == None and curnode.rightchild == None:
            return True
        return False
    
    def getRoot(self):
        return self.root.element

    def isRoot(self,curnode):
        if curnode.parent == None:
            return True
        return False
    
    def isEmpty(self):
        return self.sz == 0

    def findDepth(self):
        def depth(node):
            if not node:
                return 0
            
            return 1 + max(depth(node.leftchild), depth(node.rightchild))

        return depth(self.root)

    def findDepthofNode(self,root, x, depth):
        if not root:
            return -1
        
        if root == x:
            return depth
        
        left = self.findDepthofNode(root.leftchild,x, depth + 1)
        if left != -1:
            return left
        return self.findDepthofNode(root.rightchild,x, depth + 1)

    def findHeightOfNode(self,node):
        def findHeight(root):
            if not root:
                return -1
            
            return 1 + max(findHeight(root.leftchild),findHeight(root.rightchild))
        return findHeight(node)

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

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if i != 0:
                if eltlist[i] != -1:
                    tempnode = self.Node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if i % 2 == 0:
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                    self.sz += 1
                else:
                    nodelist.append(None)
        self.root = nodelist[1]
        return nodelist


    def insertNode(self,data):
        newNode = self.Node()
        newNode.element = data
        if not self.root:
            self.root = newNode
        else:
            queue = [self.root]
            while queue:
                temp = queue.pop(0)
                if not temp.leftchild:
                    temp.leftchild = newNode
                    newNode.parent = temp
                    break
                else:
                    queue.append(temp.leftchild)
                if not temp.rightchild:
                    temp.rightchild = newNode
                    newNode.parent = temp
                    break
                else:
                    queue.append(temp.rightchild)
        
        level = 0
        nlist = [None]
        while True:
            curNodes = self.getNodesAtALevel(level)
            if not curNodes:
                return nlist
            nlist.extend(curNodes)
            level += 1


    def inorderTraverse(self):
        traversal = []
        def inorder(node):
            if node:
                inorder(node.leftchild)
                traversal.append(node.element)
                inorder(node.rightchild)
            return traversal
        return inorder(self.root)
    
    def preorderTraverse(self):
        traversal = []
        def preorder(node):
            if node:
                traversal.append(node.element)
                preorder(node.leftchild)
                preorder(node.rightchild)
            return traversal
        return preorder(self.root)
    
    def postorderTraverse(self):
        traversal = []
        def postorder(node):
            if node:
                postorder(node.leftchild)
                postorder(node.rightchild)
                traversal.append(node.element)
            return traversal
        return postorder(self.root)
    
    def eulerTourTraversal(self):
        walk = []
        def traversal(node):
            if not node:
                return
            
            if node.leftchild != None and node.rightchild != None:
                walk.append(node.element)
            if node.leftchild != None:
                traversal(node.leftchild)
            
            # if node.leftchild != None and node.rightchild != None:
            #     walk.append(node.element)

            if node.rightchild != None:
                traversal(node.rightchild)
            
            walk.append(node.element)
        
        traversal(self.root)
        return walk

    def getNodesAtALevel(self,level: int):
        nodesList = []
        def nodesAtLevel(node, level):
            if not node:
                return
            if level == 0:
                nodesList.append(node)
            else:
                nodesAtLevel(node.leftchild,level - 1)
                nodesAtLevel(node.rightchild,level - 1)
        nodesAtLevel(self.root,level)
        return nodesList

    def getLeaves(self):
        leaves_ = []
        def leaves(node):
            if not node:
                return
            if not node.leftchild and not node.rightchild:
                leaves_.append(node.element)
            leaves(node.leftchild)
            leaves(node.rightchild)

        leaves(self.root)
        return leaves_

    def findSibling(self,node):
        if not node or not node.parent:
            return None
        if node.parent.leftchild == node:
            return node.parent.rightchild
        return node.parent.leftchild
    

    def findCousins(self,node):
        # def findLevel(currnode,level):
        #     if not currnode:
        #         return -1
        #     if currnode == node:
        #         return level
        #     left = findLevel(currnode.leftchild,level + 1)
        #     if left != -1:
        #         return left
        #     return findLevel(currnode.rightchild,level + 1)
        # level = findLevel(self.root,0)
        level = self.findDepth(self.root,node,0)
        if level == -1:
            return []
        return [x.element for x in self.getNodesAtALevel(level) if x != node]
    
    def deleteLeaves(self):
        def delete(node):
            if not node:
                return
            if not node.leftchild and not node.rightchild:
                if not node.parent:
                    return []
                if node.parent.leftchild == node:
                    temp = node
                    node.parent.leftchild = None
                    del temp
                else:
                    temp = node
                    node.parent.rightchild = None
                    del temp
                self.sz -= 1
            delete(node.leftchild)
            delete(node.rightchild)
        delete(self.root)
        newNodes = [None]
        level = 0
        while True:
            nodes = self.getNodesAtALevel(level)
            level += 1
            if nodes:
                newNodes.extend(nodes)
            else:
                return newNodes
    
    # def deleteNode(self,node):
    #     def delete(currnode):
    #         if currnode is None:
    #             return
    #         if currnode == node:
    #             if currnode.parent:
    #                 if currnode.leftchild and currnode.rightchild:
    #                     print("Cannot delete a node with 2 children!!")
    #                     return
    #                 if currnode.leftchild:
    #                     temp = currnode
    #                     currnode.parent.leftchild = currnode.leftchild
    #                     del temp
    #                 else:
    #                     temp = currnode
    #                     currnode.parent.rightchild = currnode.rightchild
    #                     del temp
    #         delete(currnode.leftchild)
    #         delete(currnode.rightchild)
    #     delete(self.root)
    #     newNodes = [None]
    #     level = 0
    #     while True:
    #         nodes = self.getNodesAtALevel(level)
    #         level += 1
    #         if nodes:
    #             newNodes.extend(nodes)
    #         else:
    #             return newNodes

    def deleteNode(self,node):
        if not node.parent:
            print("Root of the tree cannot be deleted!!")
            return
        if node.leftchild != None and node.rightchild != None:
            print("A node with 2 children cannot be deleted!!")
            return
        if node.parent.leftchild == node:
            if node.leftchild != None:
                node.parent.leftchild = node.leftchild
            else:
                node.parent.leftchild = node.rightchild
        elif node.leftchild != None:
            node.parent.rightchild = node.leftchild
        else:
            node.parent.rightchild = node.rightchild
        newNodes = []
        level = 0
        while True:
            nodes = self.getNodesAtALevel(level)
            level += 1
            if nodes:
                newNodes.extend(nodes)
            else:
                return newNodes
    
    def findAncestors(self,node,ancestors):
            if not node or not node.parent:
                return ancestors
            
            ancestors.append(node.parent)
            return self.findAncestors(node.parent,ancestors)

    def findCommonAncestors(self,val1,val2):
        def findNode(root,val):
            if not root:
                return None
            if root.element == val:
                return root
            left = findNode(root.leftchild,val)
            if left != None:
                return left
            return findNode(root.rightchild,val)
        
        node1 = findNode(self.root,val1)
        node2 = findNode(self.root,val2)

        if not node1 or not node2:
            return False

        if node1 == node2:
            return node1.parent if node1.parent else False
        
        ancestors1 = []
        ancestors2 = []
        self.findAncestors(node1,ancestors1)
        self.findAncestors(node2,ancestors2)
        if not ancestors1 or not ancestors2:
            print("No common ancestor!!")
            return
        for ancestor in ancestors1:
            if ancestor in ancestors2:
                return ancestor
        
        return self.root

    def swapSubtrees(self):
        def swap(node):
            node.leftchild, node.rightchild = node.rightchild, node.leftchild
            
            swap(node.left)
            swap(node.right)

        swap(self.root)


    
if __name__ == '__main__':
    tree = BinaryTree()
    # arr = list(map(int,input().split()))
    arr = [None,1,2,3,4,5,6,7,8,9]
    nlist = tree.buildTree(arr)
    # print(tree.inorderTraverse())
    # print(tree.preorderTraverse())
    # print(tree.postorderTraverse())
    # print(tree.findSibling(nlist[4]))
    # print(tree.findCousins(nlist[5]))
    # tree.displayTree()
    # print(tree.getLeaves())
    # print('\n',tree.getNodesAtALevel(3))
    # nlist = tree.deleteLeaves()
    # print(arr)
    # print(tree.calculateHeight())
    # print(tree.findDepthofNode(nlist[1],nlist[9],0))
    # print(tree.findDepth())
    # print(tree.findHeightOfNode(nlist[5]))

    # for i in range(23,38):
    #     nlist = tree.insertNode(i)
    # tree.displayTree()
    # for node in nlist:
    #     if node:
    #         print(node.element,end=' ')
    print(tree.eulerTourTraversal())
    # print(tree.findCommonAncestors(13,12).element)
    # print(tree.findDepthofNode(tree.root,nlist[11],0))