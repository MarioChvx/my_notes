from logging import raiseExceptions


def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def is_prime(num: int) -> bool:
    try:
        if num == 1 or num == 0:
            raise ValueError("Not valid numeric value")
    except ValueError as ve:
        print(ve)
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
        return True

def run():
    # print(is_palindrome(2000)) # TypeError
    # Use mypy to detect TypeErrors
    # mypy python_file.py --check-untyped-defs
    for i in range(10):
        print(i,is_prime(i))

if __name__ == '__main__':
    run()