import random  

class diningHall:
    def __init__(self, district, floorNum):
        self.district = district
        self.floorNum = floorNum
    
    def randomChooseFloor(self):
        return random.sample(range(1,self.floorNum+1),1)[0]
        

A = diningHall(district = 'A', floorNum = 4)
randomOption = A.randomChooseFloor()

print(randomOption)
input()

