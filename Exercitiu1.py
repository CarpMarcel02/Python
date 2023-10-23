def fibonacci(n):

    counter=2
    x = list()
    if n==1:
        x.append(1)
        return x
    elif n==2:
        x.append(1)
        x.append(1)
        return x
    a = 1
    b = 2
    x.append(1)
    x.append(1)
    while(counter!=n):
        c=a+b
        counter+=1
        x.append(c)
        a=b
        b=c
    return x


if __name__ == '__main__':
    print(fibonacci(9))