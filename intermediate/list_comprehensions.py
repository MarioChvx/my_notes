def run():
    squares = [i**2 for i in range(1,100) if i % 3 != 0]
    # for i in range(1, 100):
    #     if i**2 % 3 != 0:
    #         squares.append(i*i)
    print(squares)

if __name__ =='__main__':
    run()
    reto = [i for i in range(1,100000) if i % 9 == 0 and i % 4 == 0 and i % 6 == 0]
    print(reto)