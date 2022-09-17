
import time

def gen_fibo(max):
    n1 = 0
    n2 = 1
    counter = 0
    temp = 0
    while temp <= max:
        if counter == 0:
            counter += 1
            temp = 0
            yield temp
        elif counter == 1:
            counter += 1
            temp = 1
            yield temp
        else:
            temp = n1 + n2
            n1, n2 = n2, temp
            yield temp

if __name__ == '__main__':
    fibo = gen_fibo(50)
    for i in fibo:
        print(i)
        time.sleep(1)