#!/usr/bin/python3

import time
import random


print("Üdv a kockadobó v2.1-ben! Írd be mennyi és milyen kockát szeretnél eldobni!\nPéldául: 1 db 20 oldalú: 1d20; 5 db 6 oldalú: 5d6.")

def kocka():
    while True:
        global count
        global dice
        try:
            count, dice = input("Mit szeretnél dobni? ").split("d")
        except ValueError:
            print("Rosszul formátumot adtál meg! Helyes formátum pl: 1d20")
            continue
        if not count.isdigit():
            print(f"A kockák száma nem megfelelő, mert \"{count}\" nem egy szám!")
            continue
        elif int(dice) == 387420489 or int(count) == 387420489:
            print(r"""              .---. .---.     Nice job, you found me!
             :     : o   :       Have a cookie!
         _..-:   o :     :-.._     - 387420489
     .-''  '  `---' `---' "   ``-.      /
   .'   "   '  "  .    "  . '  "  `.  
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
       `. "    '"--...--"'  . ' .'  .'  o   `.
      .'`-._'    " .     " _.-'`. :       o  :
     '      ```--.....--'''    ' `:_ o       :
 .'    "     '         "     "   ; `.;";";";'
;         '       "       '     . ; .' ; ; ;
;     '         '       '   "    .'      .-'
'  "     "   '      "           "    _.-'""")
            continue
        elif int(count) > 1000000:
            print("Ennyi kocka a világon nincs!")
            continue
        if not dice.isdigit():
            print(f"\"{dice}\" nem szám, próbáld újra!")
            continue
        elif int(dice) == 69:
            print("Nice.")
            continue
        elif int(dice) == 420:
            print("Blaze it!")
            continue
        elif int(dice) not in [2, 4, 6, 8, 10, 12, 20, 100]:
            print(f"A(z) \"{dice}\" nem egy kocka, próbáld újra!")
            continue
        roll()


def roll():
    total = 0
    number_list = []


    if dice == "2":
        print(f"\n"r"""       _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \
  /`       .-'~"-.       `\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \  TRUST '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`""")
    elif dice == "4":
        print(r"""       ^
      /|\
     / | \
    /  |  \
    '-.|.-'""")
    elif dice == "8":
        print(r"""       ^
      /|\
     / | \
    /  |  \
    '-.|.-'
    \  |  /
     \ | /
       V
    """)
    elif dice == "12":
        print(f"\n"r"""             .----------,,
           ,"__:::::::: _-:,                                         
          /....""--_--""...:\                                        
         /.........|.........\                                       
        /... 12 ...|.... 4 ...\                                      
       /.........._'_........./|                                     
       | -,... _-"..."-_... ,..|                                     
       \ 1.-_-"........."-_/.6.|                                     
        \...\..... 8 .... /.../'                                     
         \...\.........../.../                                       
          '. .\........ /../'                                        
            "-_\_______/_/'""")
    elif dice == "20":
        print(f"\n"r"""         _-_.
     _- ',^. `-_.
 ._-'  ,'   `.   `-_ 
! `-_._________`-':::
!    /\        /\::::
;   /  \      /..\:::
!  /    \    /....\::
! /      \  /......\:
; --.___. \/_.__.--;; 
 '-_     `:!;;;;;;;'
    `-_,  :!;;;''
        `- !""")
    else:
        print(f"\n"r"""              _______.
   ______    | .   . |\
  /     /\   |   .   |.\
 /  '  /  \  | .   . |.'|
/_____/. . \ |_______|.'|
\ . . \    /  \ ' .   \'|
 \ . . \  /    \____'__\|
  \_____\/""")

    print("\nDobásaid:", end=" ")
    for i in range(int(count)):
        number = random.randint(1, int(dice))
        total += number
        number_list.append(number)
        print(number, end=" ")
    if int(dice) in number_list:
        print(f"\n☆ OMG NAT {dice}! ☆")

    print(f"\nÖsszesen: {total} Átlag: {total / int(count)}\n")
    kocka()

kocka()
