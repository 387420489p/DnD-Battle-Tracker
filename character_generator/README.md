# D&D Character Generator
This script generates a Dungeons and Dragons character based on user inputs. The user can input their desired character level, race, and class, or choose to have them randomly generated. The script then generates a name, calculates hit points, and assigns ability scores based on the character's race and class.


## User Inputs
**Level**: The desired character level. If left blank, a random level will be generated.
**Race**: The desired character race. If left blank, a random race will be generated.
**Class**: The desired character class. If left blank, a random class will be generated.


## Character Generator
The script uses the user inputs to generate the following aspects of the character:

- Name
- Level
- Class
- Subclass
- Background
- Alignment
- Ability Scores
- Proficiencies
- Equipment
- Hit Points
- AC
- Initiative
- Proficiency Bonus
- Speed
- Passive Perception
- Languages
- Height, Weight, Eye Color, Skin Color, Hair Color
- Traits

## Supported Races and Classes

**Races**: 
```
Aasimar, Bugbear, Dragonborn, Dryad, Dwarf, Elf, Firbolg, Genasi, Gith, Gnome, Goblin, Goliath, Hobgoblin, Half-Elf, Halfling, Half-Orc, Human, Juiblexian, Kender, Kenku, Kobold, Lizardfolk, Mousefolk, Orc, Succubus, Tabaxi, Tiefling, Tortle, Triton, Yuan-Ti Pureblood
```

**Classes**: 
```
Barbarian, Artificer, Bard, Blood Hunter, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
```


## How to Use
1. Install dependencies.
```sh
pip install pprint random collections
```
2. Clone `dnd_character_genetaror.py` and `names.txt`
3. Open the script in a Python environment and run it.
4. Input the desired level, race, and class when prompted. Leave blank for a random selection.
5. The script will output a character with randomly generated stats, hit points, and languages.
6. Enjoy your new character!


## Notes
The script currently does not have a separate category for currency as the authors are unsure how to account for adding from multiple sources.
Certain races and classes (Alchemist, Blood, Cardcaster, Diabolist, Feywalker, Morph, Occultist) have been temporarily removed from the script.
