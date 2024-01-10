# Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start".
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way:
# the value of the current key is the key for the next value, until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
#     will return ['a', '6', 'z', '2']
def function(mapping):
    loop = 0
    drum = []
    prima_valoare = mapping.get("start")
    element_cautare = prima_valoare
    drum.append(prima_valoare)
    while loop == 0:
        for key, value in mapping.items():
            if key == element_cautare:
                if value in drum:
                    loop = 1
                    break
                drum.append(value)
                element_cautare = value
    return drum


if __name__ == '__main__':
    print(function(({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})))
