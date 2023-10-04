class Animal():
    def __init__(self,leg,hand):
        self.leg = leg
        self.hand = hand
    
    def walk(self):
        print(f"The hand is {self.hand} and the leg is {self.leg}")

class rabbit(Animal):
    def __init__(self, hand,leg):
        # Animal.__init__(self,leg,hand)
        self.hand = hand
        self.leg = leg
        super().walk()

r = rabbit(2,2)
# r.walk()
