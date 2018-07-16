
import time
from random import randint
hHp = 100
cHp = 100

def intro():
    name = input("What is your name? ")
    ready = input(name + "Climb leg plays league of legends howl uncontrollably for no reason")
    if ready == "yes":
        print("eat half my food and ask for more but nya nya nyan.")
    else:
        print("I cry and cry and cry unless you pet me, and then maybe i cry just for fun")

def enemy():
    print('''
                       _
                       "-._ _.--"~~"--._
                        \   "            ^.    ___
                        /                  \.-~_.-~
                 .-----'     /\/"\ /~-._      /
                /  __      _/\-.__\L_.-/\     "-.
               /.-"  \    ( ` \_o>"<o_/  \  .--._\,
              /'      \    \:     "     :/_/     "`
                      /  /\ "\    ~    /~"
                      \ I  \/]"-._ _.-"[
                   ___ \|___/ ./    l   \___   ___
              .--v~   "v` ( `-.__   __.-' ) ~v"   ~v--.
           .-{   |     :   \_    "~"    _/   :     |   }-.
          /   \  |           ~-.,___,.-~           |  /   \,
         ]     \ |                                 | /     [
         /\     \|     :                     :     |/     /\,
        /  ^._  _K.___,^                     ^.___,K_  _.^  \,
       /   /  "~/  "\                           /"  \~"  \   \,
      /   /    /     \ _          :          _ /     \    \   \,
    .^--./    /       Y___________l___________Y       \    \.--^.
    [    \   /        |        [/    ]        |        \   /    ]
    |     "v"         l________[____/]________j         }r"     /
    }------t          /                       \       /`-.     /
    |      |         Y                         Y     /    "-._/
    }-----v'         |         :               |     7-.     /
    |   |_|          |         l               |    / . "-._/
    l  .[_]          :          \              :  r[]/_.  /
     \_____]                     "--.             "-.____/

''')

def h_move():
    global hHP
    global hMp
    global cHp

    print("==========================================================================================")
    print("  Scratch                          Heal    ")
    print("   Magic                           Yarn Ball")
    print("==========================================================================================")
    attack = input("")
    if attack == "s":
        print("Cat used Scratch")
        cHp -= randint(10,25)
    elif attack == "m":
        print("Cat used Magic")
        cHp -= randint(10, 25)

def cpu_move():
    time.sleep(2)
    move = randint(1,3)
    if move == 1:
        print("Lore ipsum dolor")
    elif move == 2:
        print("Howdy")
    elif move == 3:
        print("Como estas amigo!")





def game():
    global hHP
    global hMp
    global cHp
    intro()
    enemy()
    h_move()
game()

