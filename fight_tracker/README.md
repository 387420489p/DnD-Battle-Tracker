# D&D Fight Tracker
This is a command-line tool to track fights in Dungeons and Dragons. It allows you to create characters (both PCs and NPCs) with their stats, including HP, armor class, and initiative, and then track their combat during a fight.

## Installation
This tool requires **Python 3** and the **random** module. No additional installation is required.

## Adding PCs
To add player characters to the tool, you can simply add their stats to the `players.py` file. 
This allows you to easily add characters and track their stats without having to enter them manually each time you start a new fight.

## Usage
To start tracking a fight, simply run the `fight_tracker.py` script in your command-line interface. The script will prompt you to enter the names and stats of the characters you want to track. You can enter both player characters (PCs) and non-player characters (NPCs) by specifying their type when prompted.

Once you have entered all the characters you want to track, type FIGHT to begin the combat. During the combat, the tool will prompt you to enter the name of the character that has taken damage and the amount of damage taken. You can also enter negative numbers to heal the character.

After each turn, the tool will display the updated HP and status of all characters in order of initiative. The combat will continue until all characters on one side have been defeated.
## Known issues
1. There is currently no exception handling in the code, which can cause the program to crash if invalid inputs are entered.
2. The tool does not currently handle ties in initiative order.
3. The tool does not currently handle multi-sided combat.