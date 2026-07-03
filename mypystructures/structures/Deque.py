class Node:
    def __init__(self, value=None) -> None:
        self.value = value

        self.left = None
        self.right = None    

    def __repr__(self):
        return str(self.value)

class Deque:
    def __init__(self, node_class = Node):
        self.root = None
        self.last_r = None
        self.last_l = None

        self.node_class = node_class
    
    def r_append(self, value):
        if not self.root:
            self.root = self.node_class(value)
            self.last_l = self.root
            self.last_r = self.root
            return

        self.last_r.right = self.node_class(value)
        self.last_r.right.left = self.last_r
        self.last_r = self.last_r.right
        return self.node_class(value)
    
    def l_append(self, value):
        if not self.root:
            self.root = self.node_class(value)
            self.last_l = self.root
            self.last_r = self.root
            return
        
        self.last_l.left = self.node_class(value)
        self.last_l.left.right = self.last_l
        self.last_l = self.last_l.left
        return self.node_class(value)
    
    def r_pop(self):
        if not self.root:
            raise IndexError('pop from empty Deque')

        return
    
    def l_pop(self):
        return
    
    def __repr__(self):
        if self.root is None:
            return ''

        current_l = self.last_l
        printable = []

        while current_l:
            printable.append(current_l)
            current_l = current_l.right

        return str(printable)
