import time
import random
from blessed import Terminal

player = '\033[32m⚉ \033[0m'
head = '\033[32m❂ \033[0m'
fruit = ['⊞ ']#['🍒', '🍎', '🥝', '🍇', '🍉', '🍊', '🍋', '🍌', '🍍', '🥭', '🍐', '🍑', '🍓']
star = '\033[93m✯ \033[0m'
starPos = [-1, -1]
bad = '\033[31m⊠ \033[0m'
badPos = [-1, -1]
nF = 1
plX = 9
plY = 9
lenPl = 1
plLX = [9]
plLY = [9]
frX = [random.randint(0, 19)]
frY = [random.randint(0, 19)]
frT = [fruit[random.randint(0, len(fruit)-1)]]
score = 0
WARNING = 0

term = Terminal()

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[31m' #RED
    AQUA = '\033[96m' #TEXT
    RESET = '\033[0m' #RESET COLOR
    GRAS = '\033[7m\033[4m'


def clear() :
    print("\033c",end = "")

def reset() :
    clear()
    print(f"{bcolors.AQUA}")
    print('###########################################')
    print('#                 SNAKE                   #')
    print('###########################################')
    print('#                By : Me                  #')
    print('###########################################')
    print('#            With : Python 3              #')
    print('###########################################')
    print('#             Press [ENTER]               #')
    print('###########################################')
    print(f"{bcolors.RESET}")
    input()
    clear()

def actualise() :
    r = ''
    clear()
    for i in grille :
        r = r + ''.join(i)
    print(r)

def NOTanStar() :
    clear()
    print('✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅')
    print('✅✅✅💎💎✅💎💎💎✅✅✅💎✅✅💎💎✅✅✅')
    print('✅✅💎💎✅✅✅💎✅✅✅💎✅💎✅💎✅💎✅✅')
    print('✅✅✅💎💎✅✅💎✅✅✅💎💎💎✅💎💎✅✅✅')
    print('✅✅💎💎✅✅✅💎✅✅✅💎✅💎✅💎✅💎✅✅')
    print('✅✅✅✅✅✅✅✅✅⭐⭐✅✅✅✅✅✅✅✅✅')
    print('✅✅✅✅✅✅✅✅✅⭐⭐✅✅✅✅✅✅✅✅✅')
    print('✅✅✅✅✅✅✅✅⭐⭐⭐⭐✅✅✅✅✅✅✅✅')
    print('✅✅✅✅✅⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐✅✅✅✅✅')
    print('✅✅✅✅✅✅⭐⭐⭐⭐⭐⭐⭐⭐✅✅✅✅✅✅')
    print('✅✅✅✅✅✅✅⭐⭐⭐⭐⭐⭐✅✅✅✅✅✅✅')
    print('✅✅✅✅✅✅✅⭐⭐⭐⭐⭐⭐✅✅✅✅✅✅✅')
    print('✅✅✅✅✅✅⭐⭐⭐⭐⭐⭐⭐⭐✅✅✅✅✅✅')
    print('✅✅✅✅✅✅⭐⭐⭐✅✅⭐⭐⭐✅✅✅✅✅✅')
    print('✅✅✅✅✅✅⭐✅✅✅✅✅✅⭐✅✅✅✅✅✅')
    print('✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅')
    print('✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅')
    print('✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅')
    print('✅✅✅✅➕1️⃣ 0️⃣ 🟢✅✅✅✅➕1️⃣ 0️⃣ 💲✅✅✅✅')
    print('✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅')
    time.sleep(1)

def anStar() :
    clear()

def addFruit() :
    global nF
    if nF < 11 :
        addFr()


def addFr() :
    global nF
    global frX
    global frY
    global frT
    global score
    global WARNING
    x = random.randint(0, 19)
    y = random.randint(0, 19)

    if not (x in frX and y in frY) :
        frX = frX + [x]
        frY = frY + [y]
        frT = frT + [fruit[random.randint(0, len(fruit)-1)]]
        nF += 1

    else :
        j = 0
        while x in frX and y in frY :
            j += 1
            x = random.randint(0, 19)
            y = random.randint(0, 19)

            if not (x in frX and y in frY) :
                frX = frX + [x]
                frY = frY + [y]
                frT = frT + [fruit[random.randint(0, len(fruit)-1)]]
                nF += 1
                break

            if j > 20 :
                print(f'{bcolors.WARNING}{bcolors.GRAS}Warnign:{bcolors.RESET}{bcolors.WARNING}\nCan\'t add a fruit. {bcolors.OK}Score = ' + str(score) + f'{bcolors.RESET}\n')
                WARNING += 1
                time.sleep(1)
                break

def debug() :
    global frT
    global frX
    global frY
    if not len(frT) == len(frX) and len(frX) == len(frY) :
        if len(frT) == len(frX) :
            addFr()
#if len(frT) == len(frY) :
#  addFrX()


i = 0
grille = []
while i < 20 :
    j = 0
    grTemp = []
    while j < 20 :
        j += 1
        grTemp = grTemp + ['▩ ']

    grille = grille + [grTemp + ['\n']]
    i += 1

#print(grille)
#input()


reset()

grille[plY][plX] = player
actualise()

while True :
    addFruit()

    if badPos == [-1, -1] :
        badPos = [random.randint(0, 19), random.randint(0, 19)]

    if starPos == [-1, -1] :
        starPos = [random.randint(0, 19), random.randint(0, 19)]

    #joueur

    #grille[plY][plX] = player

    with term.cbreak(), term.hidden_cursor():
        inp = term.inkey()

    #print('You pressed ' + repr(inp))

    direc = inp

    if direc.lower() in ('z', 'd', 's', 'q', 'a', 'w') :

        if direc == 'z' or direc == 'w' :
            plY -= 1

        elif direc == 's':
            plY += 1

        elif direc == 'd' :
           plX += 1

        elif direc == 'q' or direc == 'a' :
            plX -= 1

        else :
            print('Impossible')
            time.sleep(0.5)
    else :
        print('Invalid direction')
        time.sleep(0.5)

    plX = plX % 20
    plY = plY % 20

    if plLX[len(plLX)-1] != plX or plLY[len(plLY)-1] != plY :
        if len(plLX) < lenPl :
            plLX = plLX + [plX]
            plLY = plLY + [plY]
        else :
            del plLX[0]
            del plLY[0]
            plLX = plLX + [plX]
            plLY = plLY + [plY]

    i = 0
    grille = []
    while i < 20 :
        j = 0
        grTemp = []
        while j < 20 :
            j += 1
            grTemp = grTemp + ['▩ ']

        grille = grille + [grTemp + ['\n']]
        i += 1



    for i in range(len(frY)) :
        if i < len(frX) :
            grille[frY[i]][frX[i]] = frT[i]

    for i in range(len(frY)) :
        if i < len(frX) :
            if plX == frX[i] and plY == frY[i] :
                del frX[i]
                del frY[i]
                del frT[i]
                score += 1
                lenPl += 1
                nF -= 1

    if badPos != [-1, -1] :
        grille[badPos[1]][badPos[0]] = bad

    if starPos != [-1, -1] :
        grille[starPos[1]][starPos[0]] = star

    for i in range(len(plLX)-1) :
        grille[plLY[i]][plLX[i]] = player

    if player == grille[plY][plX] :
        break

    if bad == grille[plY][plX] :
        score -= 1
        lenPl -= 1
        del plLX[len(plLX)-1]
        del plLY[len(plLY)-1]
        badPos = [-1, -1]
        if lenPl < 1 :
            break

    if star == grille[plY][plX] :
        score += 10
        lenPl += 10
        starPos = [-1, -1]
        anStar()


    grille[plY][plX] = head #pour éviter des bugs liés à la ligne du dessus (ou pas)

    actualise()

    print('\rScore =', score)

    if WARNING > 10 :
        print(f'{bcolors.FAIL}{bcolors.GRAS}Error:\n{bcolors.RESET}{bcolors.FAIL}Too much {bcolors.WARNING}Warning{bcolors.FAIL}:\nRestart the game.\n{bcolors.RESET}{bcolors.OK}Score = ', score, f'{bcolors.RESET}')
        time.sleep(1)

    #print('LX =', plLX, 'LY =', plLY, 'X =', plX, 'Y = ', plY, 'L =', lenPl)
    #print(frT, frX, frY, len(frT))

    time.sleep(0.05)

clear()
esp = ''
for i in range(18-len(str(score))) :
    esp = esp + ' '
esp = esp + '#'

com = '#          Not really good...             #'
if score > 10 :
    com='#          You can progress !             #'
if score > 20 :
    com='#          It\'s not so bad !              #'
if score > 30 :
    com='#        You are a good player !          #'
if score > 40 :
    com='#            Really good !                #' 
if score > 100 :
    com='#             Well done !                 #'
if score > 200 :
    com='#          Are you an hacker ?            #'
if score > 1000 :
    com='#                  🏅                     #'
if score > 2000 :
    com='#                  🥉                     #'
if score > 3000 :
    com='#                  🥈                     #'
if score > 5000 :
    com='#                  🥇                     #'

print(f'{bcolors.OK}###########################################')
print('#              Game Over...               #')
print('###########################################')
print(com)
print('###########################################')
print('#              Score =', score, esp)
print('###########################################')
print('#🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫 #')
print('#🟢🟫🟢🟢🟢🟫🟢🟢🟢🟫🟢🟢🟢🟫🟢🟢🟢🟫🟢🐸 #')
print('#🟢🟫🟢🟫🟢🟫🟢🟫🟢🟫🟢🟫🟢🟫🟢🟫🟢🟫🟢🟫 #')
print('#🟢🟢🟢🟫🟢🟢🟢🟫🟢🟢🟢🟫🟢🟢🟢🟫🟢🟢🟢🟫 #')
print('#🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫 #')
print('###########################################')
print('#              Enter your name :          #')
inp = input('# ')
esp = ''
for i in range(39-len(str(inp))) :
    esp = esp + ' '
esp = esp + '#'
print(f'\033[1A{bcolors.OK}#', inp, esp) # https://archive.wikiwix.com/cache/index2.php?url=http%3A%2F%2Fascii-table.com%2Fansi-escape-sequences.php# --> use \033[
print('###########################################')