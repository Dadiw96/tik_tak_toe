class Node:
    def __init__(self, value=None, myparent = None):
        self.value = value
        self.children = []
        self.myparent = myparent
class Tree:
    def __init__(self,value):
        self.root = (Node(value))
    def add_child(self,value,parent = None):
        if not parent :
            parent=self.root
        
        child_node = Node(value,parent)
        parent.children.append(child_node)
        return child_node
    def dfs_preorder(self,node,result = None) :
        if result is None:
            result=[]
        if node:
            result.append(node) 
        for child in node.children:
            self.dfs_preorder(child, result)
        return result
    def r_val(self,node):
        re = []
        result = self.dfs_preorder(node)
        for r in result:
            re.append(r.value)
        return re
    def display(self, node=None, level=0, prefix=""):
        if node is None:
            node = self.root
        
        # Wydrukuj bieżący węzeł
        print(prefix + str(node.value))

        # Dodaj linie dla dzieci
        for i, child in enumerate(node.children):
            next_prefix = prefix + ("|   " if i < len(node.children) - 1 else "    ")
            branch = "|-- " if i < len(node.children) - 1 else "`-- "
            self.display(child, level + 1, prefix + branch)       
    
    
        
        
        
def main():
 
# Tworzenie drzewa z 10 elementami
    t = Tree(1)

# Poziom 1
    child1 = t.add_child(2)
    child2 = t.add_child(3)

# Poziom 2
    child3 = t.add_child(4, child1)
    child4 = t.add_child(5, child1)

    child5 = t.add_child(6, child2)
    child6 = t.add_child(7, child2)

# Poziom 3
    child7 = t.add_child(8, child3)
    child8 = t.add_child(9, child4)
    child9 = t.add_child(10, child5)

# Drzewo wygląda teraz tak:
#            1
#          /   \
#         2     3
#        / \   / \
#       4   5 6   7
#      /   /   \
#     8   9     10

# Testowanie
    values = t.r_val(t.root)
    print(" Wynik: [1, 2, 4, 8, 5, 9, 3, 6, 10, 7]->",values)  
# Wynik: [1, 2, 4, 8, 5, 9, 3, 6, 10, 7]
    t.display()

if __name__ == "__main__":
    main()
