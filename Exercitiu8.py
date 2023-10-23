def functie(x, lista, status):
    result_adev = []
    result_fals = []

    for i in lista:
        mystring_adev = ""
        mystring_fals = ""
        for j in i:
            ascii_code = ord(j)
            if ascii_code % x == 0:
                mystring_adev += j
            else:
                mystring_fals += j
        result_adev.append(mystring_adev)
        result_fals.append(mystring_fals)

    if status:
        return result_adev
    else:
        return result_fals



if __name__ == '__main__':
    print(functie(2, ["borcan", "calculator", "ciocan"], True))
    print(functie(2, ["borcan", "calculator", "ciocan"], False))

