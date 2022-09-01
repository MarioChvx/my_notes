
def decor(function):
    def wrapper():
        print("Ultimo")
        function()
        print("Primero")
    # Tuve que agregar parentesisi por que si no
    # no funcionaba como lo explica
    return wrapper

@decor
def zumbido():
    print("Buzzz")

if __name__ == '__main__':
    # zumbido = decor(zumbido)
    zumbido()
