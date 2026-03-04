import os
from idlelib.iomenu import encoding
from utils import Utils
from WordCard import WordCard
from os import walk

def read(cardGame,filename):
    with open(filename, encoding="utf-8") as f:
        next(f) #A fejlécet skippeljük
        for sor in f:
            sor = sor.strip()
            if not sor:
                continue
            adatok = sor.split(";")
            cardGame.cards.append(adatok)
        print(f"\033[31mThe new pack is loaded\033[0m")

def filesFolder():
    global wlist
    wlist = []
    mypath = "files"
    for (root, dirs, files) in walk(mypath):
        files
    for f in files:
        wlist.append(f)

def deleteModes():
    filesFolder()
    for index, y in enumerate(wlist, start=0):
        print(f"{index}. {y}")
    choice = input("Selected list(number): ")
    confirm = input("Are you sure? (y/n): ")
    if confirm == "y" or confirm == "Y":
        for y in range(len(wlist)):
            if int(choice) == y:
                os.remove("files/"+wlist[y])
                print(f"The file has been deleted!")
    else:
        return



def loadAchivement():
    utils = Utils()
    utils.readAchievement()
    print()
    print("\033[32m*******************************************\033[0m")
    print("\033[32m************** Achievements ***************\033[0m")
    print("\033[32m*******************************************\033[0m")
    for index,i in enumerate(utils.achievement,start=1):
        print(f"\033[32m----------\033[0m\033[31m {index}. {i[0]}: {i[1]}/{i[2]}\033[0m")
    print("\033[32m*******************************************\033[0m")


def loadLists(cardGame):
    filesFolder()
    for index,y in enumerate(wlist, start=0):
        print(f"{index}. {y}")
    changeList(cardGame,wlist)

def changeList(cardGame, alist):
    mypath = "files/"
    global loadedList
    choice = input("Selected list(number): ")
    for y in range(len(alist)):
        if int(choice) == y:
            cardGame.clearCards()
            loadedList = alist[y]
            read(cardGame, mypath + alist[y])

def startDiffGame(cardGame):
    print()
    print("\033[32m*******************************************\033[0m")
    print("\033[32m*************Other Game modes**************\033[0m")
    print("\033[32m*******************************************\033[0m")
    print("\033[32m-----------1. start 10 words game----------\033[0m")
    print("\033[32m-----------2. start 20 words game----------\033[0m")
    print("\033[32m-----------3. start 30 words game----------\033[0m")
    print("\033[32m-----------4. start 50 words game----------\033[0m")
    print("\033[32m------------------5. Back------------------\033[0m")
    choice = input("Selected menu(number): ")
    if choice == "1":
        cardGame.startTen()
    if choice == "2":
        cardGame.startTwenty()
    if choice == "3":
        cardGame.startThirty()
    if choice == "4":
        cardGame.startFifty()
    if choice == "5":
        user_interface(cardGame)

def user_interface(cardGame):
    run = True
    while run:
        print()
        print("\033[32m*******************************************\033[0m")
        print("\033[32m*****************Main Menu*****************\033[0m")
        print("\033[32m*******************************************\033[0m")
        print("\033[32m---------------1. Start Game---------------\033[0m")
        print("\033[32m------------2. Other game modes------------\033[0m")
        print("\033[32m------------3. Change word list------------\033[0m")
        print("\033[32m------------4. Delete game mode------------\033[0m")
        print("\033[32m--------------5. Achievement---------------\033[0m")
        print("\033[32m------------------6. Help------------------\033[0m")
        print("\033[32m------------------7. Exit------------------\033[0m")
        print()
        choice = input("Selected menu(number): ")
        if choice == "1":
            cardGame.start(loadedList)
        if choice == "2":
            startDiffGame(cardGame)
        if choice == "3":
            loadLists(cardGame)
        if choice == "4":
            deleteModes()
        if choice == "5":
            loadAchivement()
        if choice == "6":
            cardGame.help()
        if choice == "7":
            run = False

def main():
    cardGame = WordCard("Test")
    print("\033[32m****************************************\033[0m")
    print("\033[32m********Welcome to the Word Card********\033[0m")
    print("\033[32m****************************************\033[0m")
    print("\033[31mIn the first step please, choose the word list!\033[0m")
    print("")
    loadLists(cardGame)
    user_interface(cardGame)

if __name__ == "__main__":
    main()