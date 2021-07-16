def has_duplicates(seq):
    for index1, item1 in enumerate(seq):
        for index2, item2, in enumerate(seq):
            if item1 == item2 and index1 != index2:
                return True 
    return False 


color_counts = {}

with open('all-favourite-colors.txt') as favourite_colors_file:
    for color in favourite_colors_file:
        color = color.strip()
        
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1


all_colors = set()

with open('all-favourite-colors.txt') as favourite_colors_file:
    for line in favourite_colors_file:
        all_colors.add(line.strip())


def range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]
    
    current = start
    
    while current < stop:
        yield current 
        current += 1


def squares(lyst):
    for num in lyst:
        yield num ** 2

new_list = [1,2,3,4]
check = squares(new_list)

for num in check:
    print(num)