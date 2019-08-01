from TwoPosPredicate import TwoPosPredicate
class MulPredicate:
    name = None
    roles = None
    two_pos_predicates = None    
    
    def __init__(self, name, roles):
        self.name = name
        self.roles = roles

    def to_special_form(self):
        """
            Преобразует производные от прилагательного предикаты в преидкаты с именем Являться и аргументом
            - прилагательным
        """
        if self.roles.get('act') is None:
            self.roles['какой'] = self.name
            self.roles['act'] = 'являться_0'
            self.name = 'являться'
        return self

    def assign_constant_situation(self, number):
        """
            Ставит в соответствие предикату константу-ситуацию
        """
        self.roles['constant_situation'] = number
        return self

    def get_word_list(self):
        """
            Возвращает список всех аргументов предиката.
        """
        words = []
        for key, value in self.roles.items():
            if key == 'constant_situation':
                next
            else:
                words.append(value)
        return words

    def to_two_positional(self):
        """
            Преобразует предикат в список двухместных предикатов.
        """

        two_pos_predicates = []
        for key, value in self.roles.items():
            if (key == 'constant_situation'):
                next
            if (key == 'act'):
                two_pos_predicates.append(TwoPosPredicate('что делает', self.roles['constant_situation'], value))
            elif (key == 'obj'):
                two_pos_predicates.append(TwoPosPredicate('объект', self.roles['constant_situation'], value))
            elif (key == 'constant_situation'):
                pass
            else:
                two_pos_predicates.append(TwoPosPredicate(key, self.roles['constant_situation'], value))

        self.two_pos_predicates = two_pos_predicates
        return self

    def print(self):

        print (f'{self.name} (', sep=' ', end='', flush=True)
        for key, value in self.roles.items():
            if (key != 'constant_situation'):
                print (f'{key}?: {value}, ', sep=' ', end='', flush=True)
        print (')')
