class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
       
        if value < self.value:
           
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
           
            if self.right:
               self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
       
        if self.value == target:
            return True
       
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target) 
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)