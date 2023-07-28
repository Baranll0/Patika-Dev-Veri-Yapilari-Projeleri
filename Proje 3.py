"""
    Binary Search Tree, her düğümde özgün bir değer bulunan ve aşağıdaki özellikleri taşıyan ikili bir ağaç veri yapısıdır:

    -Bir düğümün sol alt ağacındaki tüm düğümlerin değerleri, düğümün değerinden küçüktür.
    -Bir düğümün sağ alt ağacındaki tüm düğümlerin değerleri, düğümün değerinden büyüktür.

    [7,5,1,8,3,6,0,9,4,2] listesi için BST oluşturma adımları:

    1-İlk öğe 7 root düğümü olur.
    2-5,root düğümünün değerinden küçük olduğu için root'un sol çocuğu olur.
    3-1,root'un sol çocuğunun değerinden küçük olduğu için 5'in sol çocuğu olur.
    4-8,root düğümünün değerinden büyük olduğu için root'un sağ çocuğu olur.
    5-3,root'un sol çocuğunuun değerinden küçük ama 1'den büyük olduğu için 1'in sağ çocuğu olur.
    6-6,root'un değerinden küçük ama 5'ten büyük olduğu için 5'in sağ çocuğu olur.
    7-0,1'in değerinden küçük olduğu için 1'in sol çocuğu olur.
    8-9,8'den büyük olduğu için 8'in sağ çocuğu olur.
    9-4,5'ten küçük ama 3'ten büyük olduğu için 3'ün sağ çocuğu olur.
    10-2,3'ten küçük olduğu için 3'ün sol çocuğu olur.
"""
from graphviz import Digraph
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root

def add_edges(graph, node):
    if node is not None:
        if node.left is not None:
            graph.edge(str(node.val), str(node.left.val))
            add_edges(graph, node.left)
        if node.right is not None:
            graph.edge(str(node.val), str(node.right.val))
            add_edges(graph, node.right)

def plot_tree(root):
    dot = Digraph()
    add_edges(dot, root)
    return dot

r = Node(7)
for i in [5, 1, 8, 3, 6, 0, 9, 4, 2]:
    r = insert(r, i)

dot = plot_tree(r)
dot.view()