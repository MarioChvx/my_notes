def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict= {"fristname": "facundo", "lastname": "Garcia"}

    super_list = [
        {"fristname": "Facundo", "lastname": "Garcia"},
        {"fristname": "Miguel", "lastname": "Torres"},
        {"fristname": "Pepe", "lastname": "Rodelo"},
        {"fristname": "Susana", "lastname": "Martinez"},
        {"fristname": "Jose", "lastname": "Garcia"}
    ]

    super_dic = {
        "natural_nums": [1,2,3,4],
        "integer_nums": [-1,0,1,2],
        "natural_nums": [1.3,2.4,3.8,4.6]
    }

    for key, value in super_dic.items():
        print(key, "-", value)

    for item in super_list:
        print(item["fristname"], "", item["lastname"])

if __name__ == '__main__':
    run()