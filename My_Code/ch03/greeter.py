from datetime import datetime


def day():
        return datetime.now().strftime('%A')

def part_of_day():
    current_hour = datetime.now().hour

    if current_hour < 12:
        part_of_day = 'morning'
    elif 12 <= current_hour < 17:
        part_of_day = 'afternoon'
    else:
        part_of_day = 'evening'
    
    return part_of_day


class Greeter():
    
    def __init__(self, name):
        self.name = name 
    
    def greet(self, store):
        print(f'Hi my name is {self.name}, welcome to {store}!')
        print(f"How's your {day()} {part_of_day()} going?")
        print(f"Here's a coupon for 20% off!")

today = Greeter('Dean')
today.greet('Coles')
