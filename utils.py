class Utils:
    def __init__(self):
        self.achievement = []

    def writeShuffle(shufflelist, filename, front, back):
        with open(filename, "x", encoding="utf-8") as w:
            w.write(f"{front};{back}\n")
            for i in shufflelist:
                w.write(f"{i[0]};{i[1]}\n")
            print(f"\033[31mThe new pack is saved!\033[0m")

    def saveAchievement(self, filename, maxPoints, reachedPoints):
        with open("saves/achievement.txt", "w", encoding="utf-8") as w:
            for i in self.achievement:
                if filename == i[0]:
                    self.achievement.remove(i)
                    self.achievement.append((filename, maxPoints, reachedPoints))
                    break
            else:
                self.achievement.append((filename, maxPoints, reachedPoints))

            for y in self.achievement:
                w.write(f"{y[0]};{y[1]};{y[2]}\n")
            print("\033[31mThe new achievement is saved!\033[0m")


    def checkAchievement(self, filename, maxPoints, reachedPoints):
        self.readAchievement()
        if filename != "":
            for a in self.achievement:
                if filename == a[0]:
                    if reachedPoints > int(a[2]):
                        self.saveAchievement(filename, maxPoints, reachedPoints)
                    break
            else:
                self.saveAchievement(filename, maxPoints, reachedPoints)
        else:
            return

    def readAchievement(self):
        with open("saves/achievement.txt", encoding="utf-8") as f:
            for sor in f:
                sor = sor.strip()
                if not sor:
                    continue
                adatok = sor.split(";")
                self.achievement.append(adatok)


