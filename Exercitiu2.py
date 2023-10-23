def is_prime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def return_prime_list(lista):
    x = list()
    for i in lista:
        if is_prime(i):
            x.append(i)
    return x


if __name__ == '__main__':
    lista = [11, 42, 51, 512, 23, 15, 7]
    print(return_prime_list(lista))
