from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, pos):
        self.pos = pos
        self.left = None
        self.right = None

class Tree:
    def __init__(self, pos):
        self.root = Node(pos)

    def add_node(self, pos):
        current = self.root
        while current:
            if pos[0] < current.pos[0]:
                if current.left == None:
                    current.left = Node(pos)
                    return
                current = current.left
                    
            else:
                if current.right == None:
                    current.right = Node(pos)
                    return
                current = current.right
        current = Node(pos)

def solution(nodeinfo):
    answer = [[], []]
    index_from = {tuple(node): i+1 for i, node in enumerate(nodeinfo)}
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    
    tree = Tree(nodeinfo[0])
    for node in nodeinfo[1:]:
        tree.add_node(node)
    
    def order(node):
        if node == None:
            return
        answer[0].append(index_from[tuple(node.pos)])
        order(node.left)
        order(node.right)
        answer[1].append(index_from[tuple(node.pos)])
        
    order(tree.root)
    
    return answer