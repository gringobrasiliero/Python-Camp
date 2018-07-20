from random import randint
from time import sleep

cHp = 100
hHp= 100



def intro():
    name = input("Hey, what is your name?")
    print(" Well, " + name + "I hope you are ready.")


def hMove():
    global cHp
    global hHp
    print("Human HP:" + str(hHp))
    print("CPU HP:" + str(cHp))
    print("========================================================")
    print(" Scratch                          Leer")
    print(" Ember                            FlameThrower")
    print("========================================================")
    move = input("")
    if move == "s":
        print("You used Scratch")
        cHp = cHp - randint(20,30)
    elif move == "e":
        print("You used Ember")
        cHp = cHp - randint(20,30)
    elif move == "l":
        print("You used Leer")
        cHp = cHp - randint(20,30)
    elif move == "f":
        print("You used Flamethrower")
        cHp = cHp - randint(20,30)
    else:
        hMove()


def cMove():
    global hHp
    move = randint(1,4)
    if move == 1:
        print("Enemy used Scratch")
        hHp = hHp - randint(20, 30)
    elif move == 2:
        print("Enemy used Ember")
        hHp = hHp - randint(20, 30)
    elif move == 3:
        print("Enemy used Leer")
        hHp = hHp - randint(20, 30)
    elif move == 4:
        print("Enemy used Flamethrower")
        hHp = hHp - randint(20, 30)
    else:
        cMove()

def game_end():
    if hHp <= 0:
        print("RIP")
        again = input("Would you like to try again?")
        if again == "yes":
            game()
    if cHp <= 0:
        print("Victorious!")
        again = input("Would you like to try again?")
        if again == "yes":
            game()



def enemy():
    print("""
      ,'``.._   ,'``.
     :,--._:)\,:,._,.:       
     :`--,''   :`...';\      
      `,'       `---'  `.
      /                 :
     /                   \,
   ,'                     :\.___,-.
  `...,---'``````-..._    |:       \.
    (                 )   ;:    )   \  _,-.
     `.              (   //          `'    \,
      :               `.//  )      )     , ;
    ,-|`.            _,'/       )    ) ,' ,'
   (  :`.`-..____..=:.-':     .     _,' ,'
    `,'\ ``--....-)='    `._,  \  ,') _ '``._
 _.-/ _ `.       (_)      /     )' ; / \ \`-.'
`--(   `-:`.     `' ___..'  _,-'   |/   `.)
    `-. `.`.``-----``--,  .'
      |/`.\`'        ,','); SSt
          `         (/  (/    """)

def hero():
    print("""
              ,.,_,.
           ,.''     \,
          '          '          
        /'           |
      /_-            |    
    .'__      _-_    :
   /__        _-_    :
  ,_,._     ,_,._~   |___
.'-_ '.'.-.'-_ '.'._-^_  '.
|  -_ |.| |  -_ | | / |
 ',_,' /  _',_,'_'  /|/
  .  .|    ',. ._-^  |'
   ' '.   .'  '.    '/|
 ,'    '''    __'.  \/ -_
'_=-..--..--'^  '', : \. '.
     ',    .  ,   ,' \/ |  |-_
     / ',.. '. '. ,../  |  |  '-_
   ,'  . \ .:.''''    .''. '.    \.
 ,'    | |\       ,../   |  |      ',
 |     ' ''.,.''''       ', ',       |""")

def game():
    intro()
    enemy()
    hero()


game()