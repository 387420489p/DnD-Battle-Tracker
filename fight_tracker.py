#TODO exception handling
#TODO npc darabszám szorzás
from random import randint


initiative = []
fighters = []

def get_character(name, hp, ac, ini, pc):
    fighters.append({"Name": name,
                    "HP": int(hp),
                    "AC": ac,
                    "Initiative": ini,
                     "PC": pc,
                    })


def get_started():
    global fighters
    while True:
        pc = input("PC or NPC? Type FIGHT to start the fight!")
        if pc.lower() == "fight":
            build_initiative()
        elif pc.lower() == 'pc':
            pc = True
        else:
            pc = False
        nev = input("Name: ").lower()
        if nev in ["baldwin", "bob", "bog", "luna", "doni", "urist", "beni"]:
            pc_character(nev)
            break
        hp = int(input("HP: "))
        ac = int(input("AC: "))
        if pc == False:
            ini = randint(1, 20)
        else:
            ini = int(input("Initiative: "))
        get_character(nev, hp, ac, ini, pc)


def build_initiative():
    global fighters, initiative
    for fighter in fighters:
        initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"], fighter["PC"], fighter["AC"]])
    initiative.sort(reverse=True)
    for char in initiative:
        char.pop(0)
    fight()

def get_new_ini():
    global initiative
    initiative = []
    for fighter in fighters:
        if fighter["HP"] > 0:
            initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"], fighter["PC"], fighter["AC"]])
        else:
            if fighter["PC"] == True:
                initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"], fighter["PC"], fighter["AC"]])
    initiative.sort(reverse=True)
    for char in initiative:
        char.pop(0)
    fight()

def fight():
    global initiative, fighters
    print("=============================" * len(fighters))
    print("\nInitiative: ")
    for i in initiative:
        if i[2] == True and i[1] <= 0:
            print(f"{i[0].capitalize()}, PLAYER DOWN!")
        else:
            print(f"{i[0].capitalize()}: HP: {i[1]}, AC: {i[3]}")
    print("\n")
    print("==============")

    name = input("Who got dmg? ").lower()
    dmg = int(input("How much dmg? (Type negative for heal) "))
    for fighter in fighters:
        if fighter["Name"] == name:
            fighter["HP"] = fighter["HP"] - dmg
    print(r"""        /""")
    print(f"*//////[<>==================- {name.capitalize()} - {dmg}")
    print(r"""        \ """)
    if fighter["HP"] <= 0:
        fighter["HP"] = 0
        print(f"             {name.capitalize()} DIED !")
    get_new_ini()

def pc_character(name):
    if name == "baldwin":
        ac = 19
        hp = 79
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "bob":
        ac = 20
        hp = 77
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "luna":
        ac = 13
        hp = 54
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "bog":
        ac = 17
        hp = 47
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "doni":
        ac = 15
        hp = 80
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "urist":
        ac = 14
        hp = 71
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "beni":
        ac = 10
        hp = 49
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)

    get_started()

get_started()