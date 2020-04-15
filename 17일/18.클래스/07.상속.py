class Player: #수퍼클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SoccerPlayer(Player): #서브클래스
    def Goal(self, goal):
        self.goal = goal

class Midfielder(SoccerPlayer): #서브클래스의 서브클래스
    def assist(self, ass):
        self.ass = ass

class GamePlayer(Player): #서브클래스
    def KDA(self, K, D, A):
        self.K = K
        self.D = D
        self.A = A


son = SoccerPlayer("손흥민", 29)
son.Goal(3)
print(son.name, son.age, son.goal)
