
import random

def lineal_search(list, n):
    match = False

    for item in list:
        if item == n:
            match = True
            break

    return match

def binary_search(list, n):

    if len(list) == 0:
        return False

    half = len(list) // 2
    
    if list[half] == n:
        return True
    elif n > list[half]:
        return binary_search(list[half + 1: len(list)], n)
    else:
        return binary_search(list[0: half - 1], n)

def run():
    size = 10
    n = random.randint(0, size)
    list = sorted([random.randint(0, size) for i in range(1, size + 1)])

    # founded = lineal_search(list, n)
    founded = binary_search(list, n)
    print(list)
    print(f'The element {n} {"its" if founded else "it isnt"} in the list')

if __name__ == '__main__':
    run()