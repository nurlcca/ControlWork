class Player:
    def __init__(self, name, position, goals):
        self.name = name
        self.position = position
        self.goals = goals
    def action(self):
        return f"{self.name} is playing as a {self.position} and has scored {self.goals} goals"
    def score_goal(self):
        self.goals += 1
        return f"{self.name} scored a goal. Total goals: {self.goals}"
    
ronaldo = Player("Ronaldo", "Forward", 1000)
kante = Player("Kante", "Midfielder", 50)
print(ronaldo.action())
print(ronaldo.score_goal())
print(kante.action())
print(kante.score_goal())