# Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other
# containers, such as dictionaries, lists, sets, etc.)

def compare_dicts(d1, d2):
    # Daca sunt dictionare
    if isinstance(d1, dict) and isinstance(d2, dict):
        # Verificam daca au aceleasi chei
        if d1.keys() != d2.keys():
            return False
        # Comparam recursiv valorile
        for k in d1:
            if not compare_dicts(d1[k], d2[k]):
                return False
        return True
    # Daca sunt liste sau tuple
    elif isinstance(d1, (list, tuple)) and isinstance(d2, (list, tuple)):
        if len(d1) != len(d2):
            return False
        return all(compare_dicts(v1, v2) for v1, v2 in zip(d1, d2))
    # Daca sunt seturi
    elif isinstance(d1, set) and isinstance(d2, set):
        if len(d1) != len(d2):
            return False
        return all(compare_dicts(v1, v2) for v1, v2 in zip(sorted(d1), sorted(d2)))
    # Daca sunt alte tipuri de date comparam direct
    else:
        return d1 == d2


if __name__ == '__main__':
    d1 = {'key1': 1, 'key2': {'subkey1': 2, 'subkey2': [1, 2, 3], 'subkey3': {3, 2}}}
    d2 = {'key1': 1, 'key2': {'subkey1': 2, 'subkey2': [1, 2, 3], 'subkey3': {2, 3}}}

    print(compare_dicts(d1, d2))
