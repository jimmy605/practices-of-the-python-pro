import time
import datetime

now = time.time()
midnight = datetime.time()

def join_names(names):
    name_string = ''
    
    for i, name in enumerate(names):
        if i > 0:
            name_string += ', '
        if i == len(names) - 1:
            name_string += 'and '
        name_string += name
    return name_string


def introduce(title, names):
    print(f'{title}: {join_names(names)}')


introduce('The Three Stooges', ['Moe', 'Larry', 'Shemp'])
introduce('The Three Stooges', ['Larry', 'Curly', 'Moe'])
introduce('Teenage Mutant Ninja Turtles',['Donatello', 'Raphael','Michelangelo', 'Leonardo'])