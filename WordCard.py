from fileinput import filename
from Word import Word
import random
from utils import Utils


class WordCard:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.mistake = []
        self.points = 0
        self.filenameW = ""

    def start(self, filename):
        self.gameRule()
        self.filenameW = filename
        ylist = []
        for card in self.cards:
            ylist.append(card)
        random.shuffle(ylist)
        for y in ylist:
            print(y[0])
            key = input("\033[33mAnswer: \033[0m")
            if key == y[1]:
                self.points += 1
            else:
                self.mistake.append((key,y[0],y[1]))
        self.stopGame(self.mistake, len(self.cards), )


    def stopGame(self, blist, cardnumber):
        max_points = cardnumber
        utils = Utils()
        print()
        print("\033[31m*********************************************\033[0m")
        if max_points == self.points and max_points >= 10:
            print(f"\033[31m********* The points achieved:\033[32m {max_points}/{self.points} \033[0m\033[31m********\033[0m")
        elif max_points < 10:
            print(
                f"\033[31m********* The points achieved:\033[32m {max_points}/{self.points} \033[0m\033[31m**********\033[0m")
        else:
            print(
                f"\033[31m********* The points achieved:\033[32m {max_points}/{self.points} \033[0m\033[31m*********\033[0m")
        print("\033[31m*********************************************\033[0m")
        print()
        if blist:
            mistake = blist
            print(f"\033[31mThe wrong answer(s): \033[0m")
            for i, mis in enumerate(mistake, start=1):
                print(f"{i}.\033[33mQuestion: {mis[1]}\033[0m\033[32m ->>Correct answer: {mis[2]}\033[0m")
                print(f"\033[31m**|Your answer: {mis[0]}|**\033[0m")
        utils.checkAchievement(self.filenameW, max_points, self.points)
        self.reset()

    def reset(self):
        self.points = 0
        self.mistake = []
        self.filenameW = ""

    def clearCards(self):
        self.cards = []

    def gameRule(self):
        print()
        print("\033[32m*********************************************\033[0m")
        print("\033[32m**The game has been started!\033[0m")
        print(
            "\033[32m**The game will show the front side of the card, and you have to write down the card other side!\n**If is it true, you got +1 point.\n**Good luck!\033[0m")
        print("\033[32m*********************************************\033[0m")
        print()

    def help(self):
        print()
        print("\033[32m**********************************************************************************************\033[0m")
        print("\033[32m****************************************** HELP **********************************************\033[0m")
        print("\033[32m**********************************************************************************************\033[0m")
        print("\033[32m******* You can use the following file types: .csv, .txt *************************************\033[0m")
        print("\033[32m******* Separated with semicolon(;). And make sure the file is utf-8 coded. ******************\033[0m")
        print("\033[32m**********************************************************************************************\033[0m")
        print("\033[32m*********************************** The file structure: **************************************\033[0m")
        print("\033[32m****************************** |Header and under the words| **********************************\033[0m")
        print("\033[32m******* front_side;back_side <---(Header section. This will not appear, it can be anything) **\033[0m")
        print("\033[32m******* Danke;Thank you <-----Words section. This one is German to english *******************\033[0m")
        print("\033[32m******* Nein;No <---Two rows can be used, with any length ************************************\033[0m")
        print("\033[32m**********************************************************************************************\033[0m")
        print("\033[32m**********************************************************************************************\033[0m")
        print()

    def startTen(self):
        self.gameRule()
        ten = []
        t = []
        for k in self.cards:
            t.append(k)
        random.shuffle(t)
        for i in range(10):
            ten.append(t[i])
        for y in ten:
            print(y[0])
            key = input("\033[33mAnswer: \033[0m")
            if key == y[1]:
                self.points += 1
            else:
                self.mistake.append((key, y[0], y[1]))
        self.saveList(ten)
        self.stopGame(self.mistake, len(ten))

    def startTwenty(self):
        self.gameRule()
        twenty = []
        t = []
        for k in self.cards:
            t.append(k)
        random.shuffle(t)
        for i in range(20):
            twenty.append(t[i])
        for y in twenty:
            print(y[0])
            key = input("\033[33mAnswer: \033[0m")
            if key == y[1]:
                self.points += 1
            else:
                self.mistake.append((key,y[0],y[1]))
        self.saveList(twenty)
        self.stopGame(self.mistake, len(twenty))

    def startThirty(self):
        self.gameRule()
        thirty = []
        t = []
        for k in self.cards:
            t.append(k)
        random.shuffle(t)
        for i in range(30):
            thirty.append(t[i])
        for y in thirty:
            print(y[0])
            key = input("\033[33mAnswer: \033[0m")
            if key == y[1]:
                self.points += 1
            else:
                self.mistake.append((key, y[0], y[1]))
        self.saveList(thirty)
        self.stopGame(self.mistake, len(thirty))

    def startFifty(self):
        self.gameRule()
        fifty = []
        t = []
        for k in self.cards:
            t.append(k)
        random.shuffle(t)
        for i in range(50):
            fifty.append(t[i])
        for y in fifty:
            print(y[0])
            key = input("\033[33mAnswer: \033[0m")
            if key == y[1]:
                self.points += 1
            else:
                self.mistake.append((key, y[0], y[1]))
        self.saveList(fifty)
        self.stopGame(self.mistake, len(fifty))

    def saveList(self, sufflelist):
        path = "files/"
        print("\033[32m*******************You can save this shuffle, if you want. And use in normal game*******************\033[0m")
        choice = input("Do you want to save this list?(Y/n)")
        if choice == "Y" or choice == "y":
            filename = input("Please add a name for it: ")
            headerfront = input("Give a header name for the front: ")
            headerback = input("Give a header name for the back: ")
            Utils.writeShuffle(sufflelist,path+filename+".txt",headerfront,headerback)
            self.filenameW = filename+".txt"
        if choice == "N" or choice == "n":
            pass




