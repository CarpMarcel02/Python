def tuple(tuple_list):
    for i in range(len(tuple_list)):
        for j in range(i + 1, len(tuple_list)):
            first_element = tuple_list[i][1]
            second_element = tuple_list[j][1]
            if first_element[2] > second_element[2]:
                aux=tuple_list[i][1]
                tuple_list[i] = (tuple_list[i][0], tuple_list[j][1])
                tuple_list[j] = (tuple_list[j][0], aux)
    return tuple_list

if __name__ == '__main__':
    print(tuple([('abc', 'bcd'), ('abc', 'zza')]))
