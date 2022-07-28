from cgi import print_directory
import json
from pprint import pprint
import random
Class = "Bard"
Level = 3

KnownSpells = []
spells = []
with open("spells2.json", encoding='utf-8') as r:
    spells = json.load(r)

SpellLevel0 = []
SpellLevel1 = []
SpellLevel2 = []
SpellLevel3 = []
SpellLevel4 = []
SpellLevel5 = []
SpellLevel6 = []
SpellLevel7 = []
SpellLevel8 = []
SpellLevel9 = []

for spell in spells:
    if spell["level"] == "Cantrip" and Class in spell["class"].split(", "):
        SpellLevel0.append(spell["name"])
    elif spell["level"] == "1st-level" and Class in spell["class"].split(", "):
        SpellLevel1.append(spell["name"])
    elif spell["level"] == "2nd-level" and Class in spell["class"].split(", "):
        SpellLevel2.append(spell["name"])
    elif spell["level"] == "3rd-level" and Class in spell["class"].split(", "):
        SpellLevel3.append(spell["name"])
    elif spell["level"] == "4th-level" and Class in spell["class"].split(", "):
        SpellLevel4.append(spell["name"])
    elif spell["level"] == "5th-level" and Class in spell["class"].split(", "):
        SpellLevel5.append(spell["name"])
    elif spell["level"] == "6th-level" and Class in spell["class"].split(", "):
        SpellLevel6.append(spell["name"])
    elif spell["level"] == "7th-level" and Class in spell["class"].split(", "):
        SpellLevel7.append(spell["name"])
    elif spell["level"] == "8th-level" and Class in spell["class"].split(", "):
        SpellLevel8.append(spell["name"])
    elif spell["level"] == "9th-level" and Class in spell["class"].split(", "):
        SpellLevel9.append(spell["name"])


["Barbarian", "Artificer", "Bard", "Blood Hunter", "Cleric", "Druid", "Fighter", "Monk",
 "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

if Class == "Bard":
    if Level <= 2:
        KnownSpells.extend([SpellLevel0, SpellLevel1])
    elif Level <= 4:
        KnownSpells.extend([SpellLevel0, SpellLevel1, SpellLevel2])
    elif Level <= 6:
        KnownSpells.extend(
            [SpellLevel0, SpellLevel1, SpellLevel2, SpellLevel3])
    elif Level <= 8:
        KnownSpells.extend(
            [SpellLevel0, SpellLevel1, SpellLevel2, SpellLevel3, SpellLevel4])
    elif Level <= 10:
        KnownSpells.extend(
            [SpellLevel0, SpellLevel1, SpellLevel2, SpellLevel3, SpellLevel4, SpellLevel5])
    elif Level <= 12:
        KnownSpells.extend([SpellLevel0, SpellLevel1, SpellLevel2,
                           SpellLevel3, SpellLevel4, SpellLevel5, SpellLevel6])
    elif Level <= 14:
        KnownSpells.extend([SpellLevel0, SpellLevel1, SpellLevel2, SpellLevel3,
                           SpellLevel4, SpellLevel5, SpellLevel6, SpellLevel7])
    elif Level <= 16:
        KnownSpells.extend([SpellLevel0, SpellLevel1, SpellLevel2,  SpellLevel3,
                           SpellLevel4, SpellLevel5, SpellLevel6, SpellLevel7, SpellLevel8])
    elif Level <= 20:
        KnownSpells.extend([SpellLevel0, SpellLevel1, SpellLevel2,  SpellLevel3,
                           SpellLevel4, SpellLevel5, SpellLevel6, SpellLevel7, SpellLevel8, SpellLevel9])

print(KnownSpells[0])
print()
print(KnownSpells[1])
print()
print(KnownSpells[2])
