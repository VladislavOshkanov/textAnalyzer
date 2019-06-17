from TwoPosPredicate import TwoPosPredicate
class MulPredicate:
    name = None
    roles = None
    two_pos_predicates = None    
    
    def __init__(self, name, roles):
        self.name = name
        self.roles = roles

    def to_special_form(self):
        if (self.roles.get('act') == None):
            self.roles['какой'] = self.name
            self.roles['act'] = 'являться_0'
            self.name = 'являться'
        return self

    def assign_constant_situation(self, number):
        self.roles['constant_situation'] = number
        return self
    
    def to_two_positional(self):
        two_pos_predicates = []
        for key, value in self.roles.items():
            if (key == 'constant_situation'):
                next
            if (key == 'act'):
                two_pos_predicates.append(TwoPosPredicate('что делает', self.roles['constant_situation'], value))
            elif (key == 'obj'):
                two_pos_predicates.append(TwoPosPredicate('объект', self.roles['constant_situation'], value))
            elif (key == 'constant_situation'):
                print('skip')
            else:
                two_pos_predicates.append(TwoPosPredicate(key, self.roles['constant_situation'], value))

        # for predicate in two_pos_predicates:
            # predicate.print()
        self.two_pos_predicates = two_pos_predicates
        return self

    def print(self):
        print (f'{self.name} (', sep=' ', end='', flush=True)
        for key, value in self.roles.items():
            if (key != 'constant_situation'):
                print (f'{key}?: {value}, ', sep=' ', end='', flush=True)
        print (')')
    def to_string(self):
        string = "[color=5b46c7]{}[color=000000](".format(self.name)
        for key, value in self.roles.items():
            string = string + '{}, '.format(value)
        string=string + ')'
        return string