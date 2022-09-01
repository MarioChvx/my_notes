import functools

def run():
    nums = [num for num in range(1,101)]
    print(list(map(lambda num: num**2, nums)))
    print(list(filter(lambda num: num % 3 == 0, nums)))
    print(functools.reduce(lambda x, y: x + y, nums))


if __name__ == '__main__':
    run()