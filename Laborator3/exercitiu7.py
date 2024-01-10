# Write a function that receives a variable number of sets
# and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a.
# The key will have the following form: "a op b", where a and b are two sets,
# and op is the applied operator: |, &, -.
# Ex:{1,2}, {2, 3} =>
# {
#     "{1, 2} | {2, 3}":  {1, 2, 3},
#     "{1, 2} & {2, 3}":  { 2 },
#     "{1, 2} - {2, 3}":  { 1 },
#     ...
# }
def function(*sets):
    dictionary = {}
    seturi_facute = set()
    for primu_set in sets[0]:
        for al_doilea_set in sets[0]:
            if primu_set != al_doilea_set:

                string_exemplu = f"{al_doilea_set} | {primu_set}"
                if string_exemplu not in dictionary:
                    string_reunire = f"{primu_set} | {al_doilea_set}"
                    setul_reunire = set()
                    setul_reunire.update(primu_set, al_doilea_set)

                    string_intersectie = f"{primu_set} & {al_doilea_set}"
                    setul_intersectie = set(primu_set)
                    setul_intersectie = setul_intersectie.intersection(al_doilea_set)

                    string_minus1 = f"{primu_set} - {al_doilea_set}"
                    setul_a_minus_b = set()
                    setul_a_minus_b.update(primu_set)
                    setul_a_minus_b = setul_a_minus_b.difference(al_doilea_set)

                    string_minus2 = f"{al_doilea_set} - {primu_set}"
                    setul_b_minus_a = set()
                    setul_b_minus_a.update(al_doilea_set)
                    setul_b_minus_a = setul_b_minus_a.difference(primu_set)

                    dictionary[string_reunire] = setul_reunire
                    dictionary[string_intersectie] = setul_intersectie
                    dictionary[string_minus1] = setul_a_minus_b
                    dictionary[string_minus2] = setul_b_minus_a

    return dictionary


if __name__ == '__main__':
    result = function(({1, 2}, {2, 3}, {3, 4}))
    for key, value in result.items():
        print(f"{key} = {value}")
