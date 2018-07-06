from time import sleep
from random import randint

enemyHp = 100
linkHp = 100
linkMp = 100


def intro():
    global name
    name = input("I am grateful you are willing to go on this epic adventure. What is your name? ")
    print("======================================================================")
    print("Well " + name + " , take this. It is dangerous to go alone. ")
    print("======================================================================")
    print("======================================================================")
    print("""
              _______
         ..-'`       ````---.
       .'          ___ .'````.'SS'.
      /        ..-SS####'.  /SSHH##'.
     |       .'SSSHHHH##|/#/#HH#H####'.
    /      .'SSHHHHH####/||#/: \SHH#####\.
   /      /SSHHHHH#####/!||;`___|SSHH###\.
-..__    /SSSHHH######.         \SSSHH###\.
`.'-.''--._SHHH#####.'           '.SH####/
  '. ``'-  '/SH####`/_             `|H##/
  | '.     /SSHH###|`'==.       .=='/\H|
  |   `'-.|SHHHH##/\__\/        /\//|~|/
  |    |S#|/HHH##/             |``  |
  |    \H' |H#.'`              \    |
  |        ''`|               -     /
  |          /H\          .----    /
  |         |H#/'.           `    /
  |          \| | '..            /
  |    ^~DLF   /|    ''..______.'
   \          //\__    _..-. | 
    \         ||   ````     \ |_
     \    _.-|               \| |_
     _\_.-'   `'''''-.        |   `--.
 ''``    \            `''-;    \ /
          \      .-'|     ````.' -
          |    .'  `--'''''-.. |/
          |  .'               \|
          |.'
    """)


def enemy():
    print("A wild Arbok Appeared")
    print("""                    =HHH=                          
                =HH=     =HH=                      
            =HH=             =HH=                  
         =H=       =HHHHH=       =H=               
       =H       =H=       =H=       =H             
      H        =             =        =            
     =                                 H           
     H           H          H          =           
    H   HH==      H        H       HH   H          
   H   H==HH= =   H=      =H  =  HH==H   H         
  =   H=====H=   HHH      HHH  =H=====H   H        
  H  H=======H    =H      H=   H=======H  =        
 =  H========H==             = H========H  =       
 H H==========H=H    H   H  H H==========H H       
=  ====HH======H=H         H H======HH====  =      
H  =====HH=====H===HHHHHHH=  H=====HH=====  H      
H  =====HHHH====H==         H====HHHH=====  H      
H   ====HH=HHH==HH===     =HH==HHH=HH====   H      
H   ====HH= =HHH=HHHHHHHHHHH=HHH= =HH====   H      
=    ===HH== ==HH=HHHHHHHHH=HH== ==HH===    =      
 H   ====HH=  ==HH=HHHHHHH=HH==  =HH====   H       
 =     ==HH==  =HH===HHH===HH=  ==HH==     =       
  H     ==HH====HH=========HH====HH==     H        
   H     ==HHHHHH===========HHHHHH==     H         
    H     ====HHH===HHHHH===HHH====     H          
     =H=== =========HHHHH========H    =H           
       =H====H=====HHHHHHH=====HH=  =H             
         =H===HHHHHHHHHHHHHHHHHH===H          =H   
           H====HHHHHHHHHHHHHH===H           =  H  
            =H====HHHHHHHHHH===HH           H  =   
              HH====HHHHHH====H             =  H   
                H====HHH=====H             =HH=H   
                 H===== =====H             H   H   
                 H====   ====H             H   H   
                 H===    ====H             H  ==H  
              =HHH===HH   ===H             HH=  =  
           =H=   HH=   ==HH==H             =H    H 
         =H H   ===        =HH              =   HH 
       =H   H  =H=          ===             HHH=  =
      H      H===            =HH            =     H
     =      =H==             =H =H         H H    H
    =      ===HHHHHHH=H      =H   =H      H   HH  =
    H     ====H=       =H    =H=   HH   H= H    HH 
   ==    ====H           HH  ==== H  =H=   H     = 
   H==  HHH=H              H=====H     H    H  =H  
   H===  H   =H=            HH===H==   H     =HH   
   ===== H      =H         ==H==HH==   H    ==H    
    H===H         HH       ==H==H======H=====H     
     H=H=           H     ==H===H=======H===H      
      H====          =   ==H  =HH========H=        
       =H=====       =====H       =HHHH=           
         =H===========HH=                          
           =HHHHHHHH=
""")


def human_move():
    global enemyHp
    global name
    global linkHp
    print("======================================================================")
    print(" Strike       Heal")
    print(" Magic              ")
    print("======================================================================")
    move = input("")
    if move == "s":
        damage = randint(10,20)
        print(name + " used Strike")
        sleep(1)
        print( name + " did " + str(damage) + " damage.")
        enemyHp -= damage
    elif move == "m":
        damage = randint(10, 20)
        print(name + " used magic")
        sleep(1)
        print(name + " did " + str(damage) + " damage.")
        enemyHp -= damage
    elif move == "h":
        damage = randint(30,50)
        print(name + " used magic")
        sleep(1)
        print(name + " healed himself.")
        linkHp += damage
    if enemyHp <= 0:
        print("You killed Arbok")
        game()

def enemy_attack():
    global linkHp
    attack = randint(1,3)
    if attack == 1:
        damage = randint(10, 20)
        print("Arbok used bite")
        sleep(1)
        print("Arbok did " + str(damage) + " damage.")
        linkHp -= damage
    elif attack == 2:
        damage = randint(30, 50)
        print("Arbok used poison.")
        sleep(1)
        print("Arbok did " + str(damage) + " damage.")
        linkHp -= damage
    elif attack == 3:
        damage = randint(10, 20)
        print("Arbok used Heal.")
        sleep(1)
        print("Arbok Healed.")
        enemyHp += damage
    if linkHp <= 0:
        print("You were killed by Arbok. Game over.")
        game()

def game():
    enemyHp = 100
    linkHp = 100
    linkMp = 100


    intro()
    enemy()
    while True:
        human_move()
        enemy_attack()

game()