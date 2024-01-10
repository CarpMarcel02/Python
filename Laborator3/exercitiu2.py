# Write a function that receives a string as a parameter
# and returns a dictionary in which the keys are the characters
# in the character string and the values are the number of occurrences
# of that character in the given text. Example: For string "Ana has apples."
# given as a parameter the function will return the dictionary:

def functie(cuvant):
    dictionar = {}
    for i in cuvant:
        if i in dictionar:
            dictionar[i] += 1
        else:
            dictionar[i] = 1
    return dictionar


if __name__ == '__main__':
    print(functie("Ana has apples."))
