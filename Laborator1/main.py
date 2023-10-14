def cmmdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def vowelnumber(str):
    numberofvowels = 0
    numberofvowels += str.count("a") + str.count("e") + str.count("i") + str.count("o") + str.count("u")
    numberofvowels += str.count("A") + str.count("E") + str.count("I") + str.count("O") + str.count("U")
    return numberofvowels


def occurrenceofworld(str1, str2):
    numberofappearence = 0
    numberofappearence = str2.count(str1)
    return numberofappearence


def cameltolower(str1):
    newstring = ""
    for char in str1:
        if char.isupper():
            newstring = newstring + "_" + char.lower()
        else:
            newstring = newstring + char
    return newstring

def spiralmatrix(matrix):
    if not matrix:
        return ""

    rows, cols = len(matrix), len(matrix[0])
    newstring = []

    while matrix:
        # Traverse top row
        newstring.extend(matrix[0])
        '''print(newstring)'''
        matrix.pop(0)

        if matrix:
            # Traverse right column
            for i in range(len(matrix)):
                newstring.append(matrix[i][-1])
                matrix[i] = matrix[i][:-1]

        if matrix:
            # Traverse bottom row
            newstring.extend(matrix[-1][::-1])
            matrix.pop(-1)

        if matrix:
            # Traverse left column
            for i in range(len(matrix) - 1, -1, -1):
                newstring.append(matrix[i][0])
                matrix[i] = matrix[i][1:]

    return ''.join(newstring)

def is_palindrom(str):
        ok=0
        for i in range(len(str)):
                if(str[i]!=str[len(str)-1-i]):
                        print(str[i],str[len(str)-1-i])
                        ok=1

        return ok

def extract_number(str):
    newstring = ""
    found = False  # Flag to indicate if a number has been found
    for i in range(len(str)):
        if str[i].isdigit():
            newstring += str[i]
            found = True
        elif found:
            break  # Stop once a sequence of digits ends
    return newstring
def bit_number(number):
    n=number
    aux=""
    count=0
    while(n!=0):
        aux+=str(n%2)
        n=n//2
    for i in range(len(aux)):
        if(aux[i]=="1"):
            count+=1

    return count
def most_common_letter(str):
    newstring = ""
    arr=[0] * 26
    maxim=0;
    letter=""
    for char in str:
        if char.isupper():
            newstring = newstring + char.lower()
        else:
            newstring = newstring + char

    for char in newstring:
        if( 'a'<=char<='z'):
            index=ord(char)-ord('a')
            if ( 0 <=index<26 ):
                arr[index]+=1
    maxim=max(arr)
    letter=chr(arr.index(maxim)+ord('a'))
    return letter

def how_many_word(str):
    number_of_words=1
    for char in str:
        if (char==" "):
            number_of_words+=1
    return number_of_words



if __name__ == "__main__":
    ''' Exercitiul 1'''
    '''
    //a = int(input())
    //b = int(input())
    //print(cmmdc(a, b))
    '''

    ''' Exercitiul 2'''
    '''
    numarvocale=0
    numarvocale=vowelnumber( "Ana are mere")
    print(numarvocale)
    '''

    ''' Exercitiul 3'''
    '''
    print(occurrenceofworld("Ana", "Ana are mere, dar Ana nu are pere, Ana Ana"))
    '''

    ''' Exercitiul 4'''
    '''
    print(cameltolower("AmMersLaAnaAcasa"))
    '''

    ''' Exercitiul 5'''
    '''
    matrix = [
        ["f", "i", "r", "s"],
        ["n", "_", "l", "t"],
        ["o", "b", "a", "_"],
        ["h", "t", "y", "p"]
    ]
    print(spiralmatrix(matrix))
    '''
    ''' Exercitiul 6'''
    '''
    print(is_palindrom("racecar"))
    '''
    ''' Exercitiul 7'''
    '''
    print(extract_number("car123of21"))
    '''
    ''' Exercitiul 8'''
    '''
    print(bit_number(24))
    '''
    ''' Exercitiul 9'''
    '''
    print(most_common_letter("Ana are Multe Mere"))
    '''
    ''' Exercitiul 10'''
    '''
    print(how_many_word("Doamne ajuta-l pe roman. De ce nu"))
    '''