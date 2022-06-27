#TODO csata lekezelése
#TODO aktuális állás kiprintelése


initiative = []
fighters = []

def get_character(name, ac, hp, ini):
    fighters.append({"Name": name,
                    "AC": ac,
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
            ac = int(input("AC: "))
            hp = int(input("HP: "))
            ini = int(input("Initiative: "))
            get_character(nev, ac, hp, ini)


def build_initiative():
    global fighters, initiative
    for fighter in fighters:
        initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"]])
    initiative.sort(reverse=True)
    print(initiative)
    fight()

def get_new_ini():
    global initiative
    initiative = []
    for fighter in fighters:
        if fighter["HP"] > 0:
            initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"]])
            initiative.sort(reverse=True)
    fight()

def fight():
    global initiative, fighters
    print(f"Initiative: {initiative}")
    name = input("Ki kapott sebzést? ")
    dmg = int(input("Mennyi sebzést kapott?"))
    for fighter in fighters:
        if fighter["Name"] == name:
            fighter["HP"] = fighter["HP"] - dmg
    get_new_ini()


get_started()