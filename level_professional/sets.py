
if __name__ == '__main__':

    # Declare sets
    set_1 = {1, 'hola', True, 5.35, (1, 2)}

    # It can be void
    void_set = set()
        # Empty dictionary
    void_dic = {}

    # Typecast list and tuple to sets
    list_1 = [1,2,2,3,4,5,3]
    print(set(list_1))

    tuple_1 = (1,2,2,3,4,5,3)
    print(set(tuple_1))

    # Add elements to sets
    my_set = {1, 2, 3}
    my_set.add(4)
    
    my_set.update([1, 2, 5])

    my_set.update((6, 7), {1, 8, 9})

    # Remove elements from sets
    ## Just discar the element from the set
    my_set.discard(1)
    ## Just remove the element from the set but it can 
    #   raise an error if the element does not exist
    my_set.remove(1)
    # Remove a random element from the set
    my_set.pop()
    # Remove all elements from the set
    my_set.clear()

    ## Just as math set can be operated
    