class Hypothesis:
    name = None
    first_cs = None
    second_cs = None

    def __init__(self, name, first_cs, second_cs):
        self.name = name
        self.first_cs = first_cs
        self.second_cs = second_cs
    def print(self):
        print("{}(A{}, {})".format(self.name, self.first_cs, self.second_cs))
    def to_string(self):
        return "{}(A{}, A{})".format(self.name, self.first_cs, self.second_cs)