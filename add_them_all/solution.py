def add_them_all(array: [int]) -> int:
    if not array:
        return 0
    else :
        return array[0] + add_them_all(array[1:])

