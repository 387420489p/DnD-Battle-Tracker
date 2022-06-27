initiative = []
fighters = []

def get_character(name, hp, ini):
    fighters.append({"Name": name,
                    "HP": hp,
                    "Initiative": ini
                    })


def get_started():
    global fighters
    while True:
        nev = input("Add meg a karakter nevét! Type FIGHT for fight! ")
        if nev == "fight" or nev == "FIGHT":
            build_initiative()
            break
        else:
            hp = int(input("HP: "))
            ini = int(input("Initiative: "))
            get_character(nev, hp, ini)


def build_initiative():
    global fighters, initiative
    for fighter in fighters:
        initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"]])
    initiative.sort(reverse=True)
    for char in initiative:
        char.pop(0)
    fight()

def get_new_ini():
    global initiative
    initiative = []
    for fighter in fighters:
        if fighter["HP"] > 0:
            initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"]])
    initiative.sort(reverse=True)
    for char in initiative:
        char.pop(0)
    fight()

def fight():
    global initiative, fighters
    print("Initiative: ", end=" ")
    for i in initiative:
        print(f"Név: {i[0]}, HP: {i[1]} ||", end=" ")
    print()
    name = input("Ki kapott sebzést/healt? ")
    dmg = int(input("Mennyi sebzést kapott? (Healhez negatív számot írj!)"))
    for fighter in fighters:
        if fighter["Name"] == name:
            fighter["HP"] = fighter["HP"] - dmg
    print("        /")
    print(f"*//////[<>==================- {name} - {dmg}")
    print(r"""        \ """)
    get_new_ini()


get_started()