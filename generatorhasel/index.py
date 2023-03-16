import random
import os

malelitery = "qwertzuiopasdfghjklyxcvbnm"
duzelitery = "QWERTZUIOPASDFGHJKLYXCVBNM"
cyfry = "1234567890"
znaki = "@#$&_-()=%*:/!?+."

kolkocyfry = "⓪①②③④⑤⑥⑦⑧⑨⑩⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾⓿❶❷❸❹❺❻❼❽❾❿➀➁➂➃➄➅➆➇➈➉➊➋➌➍➎➏➐➑➒➓"
arrows = "↖↗↘↙⇄⇅⇆⇇⇈⇉⇊↯↸↹⇱⇲⇵⇶⇤⇥☇☈↚↛↜↝↞↟↠↡↫↬↭↮⇜⇝⇞⇟⇴⇷⇸⇹⇺⇻⇼↢↣↤↥↦↧↕↨↔←→↰↱↲↳↴↩↪⤴⤵↵↶↷↺↼↽↾↿⇀⇁⇂⇃⇋⇌➩➪➫➬➭➮➯➱⍇⍈⍐⍗➡⇫⇬⇭⇮⇯⇰⇦⇧⇨⇩⇪⇳⏎⇐⇑⇒⇓⇔⇍⇎⇏⇕⇖⇗⇘⇙⇚⇛➘➙➚⇠⇡⇢⇣⇽⇾⇿⌅⌆⌤▶➔➛➜➝➞➟➠➢➣➤➥➦➧➨➲➽➾↓↑➳➴➵➶➷➸➹➺➻➼"
chess = "♔♕♖♗♘♙♚♛♜♝♞♟"
trojkaty = "▲△▶▷▼▽◀◁∇∆▴▵▸▹▾▿◂◃◭◮◸◹◺◿►▻◄◅◢◣◤◥◬"
brajl = "⣿⠿⠾⠽⠼⠻⠺⠹⠸⠷⠶⠵⠴⠳⠲⠱⠰⠯⠮⠭⠬⠫⠪⠩⠨⠧⠦⠥⠤⠣⠢⠡⠠⠟⠞⠝⠜⠛⠚⠙⠘⠗⠖⠕⠔⠓⠒⠑⠐⠏⠎⠍⠌⠋⠊⠉⠈⠇⠆⠅⠄⠃⠂⠁"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#losowe liczby
id = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))


os.system('cls')

print(f"{bcolors.OKGREEN}Witaj w generatorze hasel! {bcolors.ENDC}")
print("")


def main():
    print("Podaj dlugosc hasla:")
    dlugosc = input(f"{bcolors.OKGREEN}>>> {bcolors.ENDC}")


    print("Podaj ilosc hasel:")
    ilosc = input(f"{bcolors.OKGREEN}>>> {bcolors.ENDC}")

    if(ilosc.isdigit() == False or dlugosc.isdigit() == False):
        os.system('cls')
        print(f"{bcolors.FAIL} ! Podaj liczbe! ! {bcolors.ENDC}")
        print("")
        main()
    else:
        print("Czy chcesz dodac znaki specjalne? (tak/nie)")
        wybranie(int(dlugosc), int(ilosc))


    

def wybranie(dlugosc, ilosc):
    znaki_specjalne = input(f"{bcolors.OKGREEN}>>> {bcolors.ENDC}")

    if(znaki_specjalne == "tak"):
        os.system('cls')
        genspecjalne(dlugosc, ilosc, id)
    elif(znaki_specjalne == "nie"):
        os.system('cls')
        genbezspecjalne(dlugosc, ilosc, id)
    else:
        print(f"{bcolors.FAIL} ! Nie rozumiem, sprobuj ponownie. (tak/nie) ! {bcolors.ENDC}")
        wybranie(dlugosc, ilosc)
        return 0


def genbezspecjalne(dlugosc, ilosc, id):

    tablicazhaslami = []

    for j in range(ilosc):
        haslo = ""
        for i in range(dlugosc):
            haslo += random.choice(malelitery + duzelitery + cyfry + znaki)
        tablicazhaslami.append(haslo)
        

    print(f"{bcolors.BOLD}>> Wygenerowano {j + 1} hasel. {bcolors.ENDC}")
    print(f"{bcolors.BOLD}>> Tworzenie pliku... {bcolors.ENDC}")
    print(" ")

    with open(f'./hasla/hasla_bezspecjalnych_{id}.txt' , 'w', encoding='utf-8') as f:
        for item in tablicazhaslami:
            f.write(item)
            f.write('\n')
            
    print(f"{bcolors.OKGREEN} !!! Plik zostal utworzony! (hasla_bezspecjalnych_{id}.txt) !!! {bcolors.ENDC}")
    exit()






def genspecjalne(dlugosc, ilosc, id):

    tablicazhaslami = []

    for j in range(ilosc):
        haslo = ""
        for i in range(dlugosc):
            haslo += random.choice(malelitery + duzelitery + cyfry + znaki + kolkocyfry + arrows + chess + trojkaty + brajl)
        tablicazhaslami.append(haslo)
        

    print(f"{bcolors.BOLD}>> Wygenerowano {j + 1} hasel. {bcolors.ENDC}")
    print(f"{bcolors.BOLD}>> Tworzenie pliku... {bcolors.ENDC}")
    print(" ")
    with open(f'./hasla/hasla_specjalne_{id}.txt' , 'w', encoding='utf-8') as f:
        for item in tablicazhaslami:
            f.write(item)
            f.write('\n')
            
    print(f"{bcolors.OKGREEN} !!! Plik zostal utworzony! (hasla_bezspecjalnych_{id}.txt) !!! {bcolors.ENDC}")
    exit()
        

main()