#!/usr/bin/env python


notatki = {
    'testowa1': 'testowa tresc 1',
    'testowa2': 'testowa tresc 2',
}


def menu():
    print('\n')
    print('1. dodaj notatkę')
    print('2. odczytaj notatkę')
    print('3. pokaź listę')
    print('4. zapisz do pliku')
    print('5. wyjdź')
    print('\n')

    opcja = input('Wybierz opcję: ')

    if opcja == '1':
        dodaj()
    elif opcja == '2':
        czytaj()
    elif opcja == '3':
        lista()
    elif opcja == '4':
        do_pliku()
    elif opcja == '5':
        exit(0)
    else:
        menu()


def dodaj():
    tytul = input('Podaj tytuł: ')
    tresc = input('Podaj tresc: ')
    notatki[tytul] = tresc
    print('Notatka "%s" zapisana!' % tytul)
    menu()


def czytaj():
    tytul = input('Podaj tytuł notatki: ')
    print(notatki.get(tytul, 'Brak takiego tytułu :('))
    menu()


def lista():
    print('\n')
    for notatka in notatki:
        print(notatka)
    menu()


def do_pliku():
    tytul = input('Podaj tytuł notatki: ')
    tresc = notatki.get(tytul)
    if not tresc:
        print('Brak takiego tytułu :(')
    else:
        nazwa_pliku = '%s.txt' % tytul
        with open(nazwa_pliku, 'w+') as plik:
            plik.write(tresc)
        print('Plik %s zapisany' % nazwa_pliku)
    menu()


if __name__ == '__main__':
    menu()
