pole = list(range(1, 10))
nabor_pobed = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]


def show_pole():
    print('\n')
    for i in range(3):
        print('|', pole[0 + i * 3], '|', pole[1 + i * 3], '|', pole[2 + i * 3], '|')
    print('\n')


def hod(player):
    while True:
        a = int(input('Куда поставить ' + player + '?'+' '))
        pole[a - 1] = player
        break


def proverka_pobed():
    for i in nabor_pobed:
        if pole[i[0] - 1] == pole[i[1] - 1] == pole[i[2] - 1]:
            return pole[i[0] - 1]
    else:
        return False


def main():
    chetnost_hoda = 0
    while True:
        show_pole()
        if chetnost_hoda % 2 == 0:
            hod('X')
        else:
            hod('O')
        resultat = proverka_pobed()
        if resultat:
            show_pole()
            print(resultat, 'won!')
            break
        chetnost_hoda += 1
        if chetnost_hoda == 8:
            show_pole()
            print('Draw')
            break


main()
