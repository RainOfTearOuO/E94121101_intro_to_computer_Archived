class Animals(): #create a parent class
    def __init__(self, weight, mood): #constructor of weight & mood
        self.weight = weight
        self.mood = mood
    def feed(self): #since the detail of methods are different, we leave "pass" here
        pass
    def walk(self):
        pass
    def bath(self):
        pass

class Dogs(Animals): #child class, inherited from Animals
    def feed(self):
        self.weight += 0.2
        self.mood += 1
    def walk(self):
        self.weight -= 0.2
        self.mood += 2
    def bath(self):
        self.mood -= 2
    def printf(self, n_feed, n_walk, n_bath):
        for i in range(n_feed):
            self.feed()
        for i in range(n_walk):
            self.walk()
        for i in range(n_bath):
            self.bath()
        print("狗狗現在的體重=",self.weight,"kg, 心情",self.mood)
        
class Shiba(Dogs):
    def feed(self):
        self.weight += 0.3
        self.mood += 5
    def printf(self, n_feed, n_walk, n_bath):
        for i in range(n_feed):
            self.feed()
        for i in range(n_walk):
            self.walk()
        for i in range(n_bath):
            self.bath()
        print("柴犬現在的體重=",round(self.weight,3),"kg, 心情",self.mood) #using round() cuz of float's feature
    def mood_constraint(self, constr):
        self.constr = constr
        print("mood最高只能為=" ,self.constr)
        if(self.mood>self.constr):
            self.mood=self.constr
            print("所以，柴犬現在的心情 =", self.mood)
            

shiba = Shiba(5, 70)
shiba.printf(20, 10, 3)
shiba.mood_constraint(90) #change mood_constraint here
shiba.mood_constraint(300)