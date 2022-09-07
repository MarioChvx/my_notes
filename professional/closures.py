
def repeter(num: int):
    def final(string: str) -> str:
        print(string*num)
    return final

def run():
    hello = repeter(3)
    hello('Hola')

if __name__ == '__main__':
    run()