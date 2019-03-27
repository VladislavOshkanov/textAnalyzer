class TwoPosPredicate:
    name = None
    constant_situation = None
    value = None
    def __init__(self, name, constant_situation, value):
        self.name = name
        self.constant_situation = constant_situation
        self.value = value
    def print(self):
        print("{}(A{}, {})".format(self.name, self.constant_situation, self.value))
    def to_string(self):
        return "{}(A{}, {})".format(self.name, self.constant_situation, self.value)