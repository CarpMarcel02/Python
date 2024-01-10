# Write a function that receives a variable number of positional arguments
# and a variable number of keyword arguments adn will return
# the number of positional arguments whose values can be found among keyword arguments values.
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

def function(*args, **kwargs):
    dictionary = {}
    for element in args:
        if element in kwargs.values():
            dictionary[element] = 1

    return len(dictionary)

if __name__ == '__main__':
    print(function(1, 2, 3, 4, x=1, y=2, z=3, w=5))