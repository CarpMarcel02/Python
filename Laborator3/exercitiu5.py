# The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.
# Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} and
# d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False
# because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.
import string


def validate_dict(tuple_set, dictionary):
    for key, value in dictionary.items():
        am_gasit_cheia = 0
        print(key, value)
        if am_gasit_cheia == 0:
            for cheie, prefix, middle, suffix in tuple_set:
                gasit_cuvant_mijloc = 0
                print(key, cheie)
                if key == cheie:
                    am_gasit_cheia = 1
                    cuvinte = value.split()
                    cuvinte = [word.strip(string.punctuation) for word in cuvinte]
                    print(cuvinte[0], cuvinte[len(cuvinte)-1])
                    if prefix != "":
                        if cuvinte[0] != prefix or cuvinte[0] == middle:
                            print("primu cuvant nu este preifxul necesar de la regula")
                            return False
                    if suffix != "":
                        if cuvinte[len(cuvinte)-1] != suffix or cuvinte[len(cuvinte)-1] == middle:
                            print("ultimul cuvant nu este sufixul necesar")
                            return False
                    for cuvant in cuvinte:
                        print(cuvant, middle)
                        if cuvant == middle:
                            gasit_cuvant_mijloc = 1
                    if gasit_cuvant_mijloc == 0:
                        print(f"nu am gasit cuvantul de la mijloc {middle}")
                        return False
        if am_gasit_cheia == 0:
            print(f"nu am gasit cheia {key}")
            return False
    return True




if __name__ == '__main__':
    print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},{"key1": "come inside, it's too cold out", "key2": "start this middle is not valid winter"}))
