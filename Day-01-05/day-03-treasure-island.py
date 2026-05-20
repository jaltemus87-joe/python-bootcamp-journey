# Day 3 - Treasure Island - My Version

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Get user choices and make them case-insensitive with .capitalize()
Direction = input("You're at a cross road. Which direction would you like to take? Type 'Left' or 'Right'.\n").capitalize()

if Direction == "Left":
    Lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").capitalize()
    
    if Lake == "Wait":
        Door_Prize = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").capitalize()
        
        if Door_Prize == "Red":
            print("You were overcome with fire! Game Over!")
            print('''

                                               (  .      )
                                           )           (              )
                                                 .  '   .   '  .  '  .
                                        (    , )       (.   )  (   ',    )
                                         .' ) ( . )    ,  ( ,     )   ( .
                                      ). , ( .   (  ) ( , ')  .' (  ,    )
                                     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
        elif Door_Prize == "Blue":
            print("You were attacked by an alien. Game Over!")
            print('''
                                     \.   \.      __,-"-.__      ./   ./
                       \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
                        \`.  \_`-''      _,="=._      ``-'_/  .'/
                         \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
                      \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
                       \`-'  /    `-._  "       "  _.-'    \  `-'/
                       /)   (         \    ,-.    /         )   (\
                    ,-'"     `-.       \  /   \  /       .-'     "`-,
                  ,'_._         `-.____/ /  _  \ \____.-'         _._`,
                 /,'   `.                \_/ \_/                .'   `,\
                /'       )                  _                  (       `\
                        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \
                       / ,-'        \/|`|`|`|'|'|'|\/        `-, \
                      /,'             | | | | | | |             `,\
                     /'               ` | | | | | '               `\
                                        ` | | | '
                                          ` | '                                     ''')
        else:
            print("You found the treasure! You win the game!")
            print('''
                                          _.--.
                                _.-'_:-'||
                            _.-'_.-::::'||
                       _.-:'_.-::::::'  ||
                     .'`-.-:::::::'     ||
                    /.'`;|:::::::'      ||_
                   ||   ||::::::'     _.;._'-._
                   ||   ||:::::'  _.-!oo @.!-._'-.
                   |'.  ||:::::.-!()oo @!()@.-'_.|
                    '.'-;|:.-'.&$@.& ()$%-'o.'|'||
                      `>'-.!@%()@'@_%-'_.-o _.|'||
                       ||-._'-.@.-'_.-' _.-o  |'||
                       ||=[ '-._.-|'|.-'    o |'||
                       || '-.]=|| |'|      o  |'||
                       ||      || |'|        _| ';
                       ||      || |'|    _.-'_.-'
                       |'-._   || |'|_.-'_.-'
                        '-._'-.|| |' `_.-'
                            '-.||_/.-'                   ''')
    else:
        print("While swimming you were attacked by a Shark! Game Over!")
        print('''
                                                                     ,-
                                           ,'::|
                                          /::::|
                                        ,'::::o\                                      _..
                     ____........-------,..::?88b                                  ,-' /
             _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
            <. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
             `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
                 """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
                     ""--.__     P(       \               ` ``:`:``:::: .   .;'
                            "\""--.:-.     `.                             .:/
                              \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                               `P         `-._ \          `-:\          `. `:\
                                               ""            "            `-._) ''')
else:
    print("You were killed by a rhino, Game Over!")
    print('''/))_
                 /   .\/)
        _."```'-'  \___/
       '/           |
        \          /
         | ||~~~| ||
         ^^^`   ^^^`''')


# === My Personal Notes ===
# This project was a lot of fun but also overwhelming at first because of all the if/else choices.
# I really liked adding my own ASCII art for each ending — it made it feel more like my own game.
# 
# What I changed from the course version:
# - Used .capitalize() instead of .lower() for the inputs
# - Created more dramatic and fun endings with ASCII art
# - Used clearer variable names like Direction, Lake, and Door_Prize
