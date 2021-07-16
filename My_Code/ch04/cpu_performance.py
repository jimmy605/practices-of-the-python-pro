import random 
import time

# def an_expensive_function():
#     execution_time = random.random() / 100
#     time.sleep(execution_time)

# if __name__ == '__main__':
#     for _ in range(1000):
#         an_expensive_function()


def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    the_list.sort()

def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort()

if __name__ == '__main__':
    sort_expensive()
    for i in range(1_000):
        sort_cheap()

def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(2.5 == calculate_mean([1,2,3,4]))
print(5.5 == calculate_mean([5,5,5,6,6,6]))