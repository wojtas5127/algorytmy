def z2(imie, nazwisko):
    return (imie[0].upper() + '.' + nazwisko[0].upper() + nazwisko[1:])


def z4(f,imie,nazwisko):
    return print(f(imie,nazwisko))

z4(z2,'jan','kowalski')
