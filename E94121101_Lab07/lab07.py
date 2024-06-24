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

class Cats(Animals): #child class, inherited from Animals
    def feed(self):
        self.weight += 0.1
        self.mood += 1
    def walk(self):
        self.weight -= 0.1
        self.mood -= 1
    def bath(self):
        self.mood -= 2
    def printf(self, n_feed, n_walk, n_bath):
        for i in range(n_feed):
            self.feed()
        for i in range(n_walk):
            self.walk()
        for i in range(n_bath):
            self.bath()
        print("貓貓現在的體重=",round(self.weight,3),"kg, 心情",self.mood) # using "round()" cuz it'll display 11.4999999999... if we don't do that
dog = Dogs(4.8, 65) 
dog.printf(18, 10, 4) 

cat = Cats(8.2, 60) 
cat.printf(40, 7, 1)
