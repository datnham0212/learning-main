#No need for 'number' attribute yet. 'number' is the number of exam scores i.e length of 'score' list
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def getName(self):
        return self.name

    def getScore(self, i):
        return self.score[i]
    
    def getScores(self):
        return self.score

    def inputScore(self):
        self.score = list(map(int, input().split()))

    def getAverage(self):
        try:
            return sum(self.score)/len(self.score)
        except:
            if (len(self.score) == 0):
                return 0

    def getHighScore(self):
        return max(self.score)

    def receiveScholarship(self):
        return True if (self.getAverage() > 8 and 4 not in self.score) else False

    def __str__(self):
        return f"Name: {self.getName()}\nScores: {self.getScores()}\nEligable for scholarship: {self.receiveScholarship()}"