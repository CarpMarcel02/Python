def note_muzicale(lista_note, lista_pozitii, start):
    result = []
    result.append(lista_note[start])
    index=0
    while index < len(lista_pozitii):
        start += lista_pozitii.pop(0)
        if start > len(lista_note):
            start = start % len(lista_note)
        result.append(lista_note[start])


if __name__ == '__main__':
    print(note_muzicale(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

