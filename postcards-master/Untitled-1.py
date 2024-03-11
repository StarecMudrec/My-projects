class Node:
    def __init__ (self, value, children):
        self.children = children
        self.value = value
def print_tree(root, n):
    print("       "*n + str(root) + root.value)
    for child in root.children:
        print_tree(child, n + 1)


a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
a1 = [b, c]
c1 = [d, e, f]
a = Node(a, a1)
c = Node(c, c1)
print_tree(a, 0)