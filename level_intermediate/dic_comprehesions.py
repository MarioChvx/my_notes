def run():
    reto = {x : x**3 for x in range(1,101) if x % 3 != 0}
    print(reto)

if __name__ == '__main__':
    run()