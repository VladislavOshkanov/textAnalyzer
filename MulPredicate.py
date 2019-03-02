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
                two_pos_predicates.append(TwoPosPredicate('Что делает', self.roles['constant_situation'], value))
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
