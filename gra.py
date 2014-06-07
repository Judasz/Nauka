from random import randint, choice


def generate():
    strength = randint(1, 5)
    health = randint(20, 100)
    monster = {
        'strength': strength,
        'health': health,
    }

    return monster


def show(monster):
    print("Siła:", monster['strength'], "Życie", monster['health'])


def fight(monster1, monster2):
    monsters = [monster1, monster2]
    first = choice(monsters)
    monsters.remove(first)
    second = monsters[0]
    print("Pierwszy:")
    show(first)
    print("Drugi:")
    show(second)

    while first['health'] > 0 and second['health'] > 0:
        # if first['zywiol'] == 'ogien' and second['zywiol'] == 'woda':
        #     first_multipler = randint(1, 2)
        # else:
        #     first_multipler = 1
        # first_damage = first['strength'] * randint(1, 3) * first_multipler
        first_damage = first['strength'] * randint(1, 3)
        second_damage = second['strength'] * randint(1, 3)
        second['health'] = second['health'] - first_damage
        first['health'] = first['health'] - second_damage
        print("potwór1 zadał", first_damage, "obrażeń, przeciwnikowi zostało", second['health'])
        print("potwór2 zadał", second_damage, "obrażeń, przeciwnikowi zostało", first['health'], '\n')



monster1 = generate()
monster2 = generate()
fight(monster1, monster2)
