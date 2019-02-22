class TwoPosPredicate:
    name = None
    constant_situation = None
    value = None
    def __init__(self, name, constant_situation, value):
        self.name = name
        self.constant_situation = constant_situation
        self.value = value
    def print(self):
        print('{self.name}(A{self.constant_situation}, {self.value})')