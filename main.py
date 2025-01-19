## m stands for metabolism
## r stands for reproduction
import random
import time

class Animal:
    def __init__(self,age,energy,maxfood,m_rate,r_cooltime,r_rate,minfood,maxage,foodCal,StraveDay):
        self.age = age
        self.energy = energy ## remove when test in real obj
        self.maxfood = maxfood
        self.m_rate = m_rate
        self.r_cooltime = r_cooltime
        self.r_rate = r_rate
        self.minfood = minfood
        self.maxage = maxage
        self.foodCal = foodCal
        self.StraveDay = StraveDay
        
        self.OffSpring = [age,energy,maxfood,m_rate,r_cooltime,r_rate,minfood,maxage,foodCal,StraveDay]
                
        self.propagate_bool = self.percentage_chance(r_rate)
        self.is_alive = True

    def percentage_chance(self,percent:float)->bool:
        return random.uniform(0, 100) < percent
    
    def eat(self,food:list):
        # print(food) ## Add remove a food in list
        self.energy += self.foodCal
        food.pop(1)
        pass
    
    def propagate(self,packs:list):
        print("propagate")
        packs.append(Animal(self.OffSpring[0],self.OffSpring[1],self.OffSpring[2],self.OffSpring[3],self.OffSpring[4],self.OffSpring[5],self.OffSpring[6],self.OffSpring[7],self.OffSpring[8],self.OffSpring[9]))
    
    def update(self):
        self.age += 1
        self.energy -= self.m_rate
        
    def mainLoop(self,packs:list,food:list):
        # print(packs)
        if self.age == self.maxage:
            self.is_alive = False
        
        elif self.energy < self.maxfood and self.energy + self.foodCal < self.maxfood:
            ## function Eat
            self.eat(food)
            pass
        
        elif self.energy > self.minfood and self.propagate_bool == True :
            self.propagate(packs)
        
        self.update()
            
class Rabbit(Animal):
    pass

class Wolf(Animal):
    pass

class Grass:
    def __init__(self):
        self.is_alive = True

def main():
    
    n = 400
    
    rabbit_list = []
    wolf_list = []
    grass_list = [Grass] * n
    
    for i in range(0,20):
        rabbit_list.append(Rabbit(0,45,45,3,10,50,40,25,10,3))
    
    for i in range(0,2):
        wolf_list.append(Wolf(0,120,200,2,10,50,120,50,10,2))
    
    state = 1
    
    while len(rabbit_list) and len(wolf_list) != 0:
        print(f"world Date {state}")
        
        
        ## Update rabbit activity
        for rab in rabbit_list:
            rab.mainLoop(rabbit_list,grass_list)

        ## Update wolf activity
        for wolf in wolf_list:
            wolf.mainLoop(wolf_list,rabbit_list)
        
        print("total rab {} total wolf {}".format(len(rabbit_list),len(wolf_list)))
        
        for c , rab in enumerate(rabbit_list):
            print("rabbit no.{} status is {} | {} | {}".format(c,rab.is_alive,rab.age,rab.energy))
            
        for c , wolf in enumerate(wolf_list):
            print("wolf no.{} status is {} | {} | {}".format(c,wolf.is_alive,wolf.age,wolf.energy))
        
        rabbit_list = [rab for rab in rabbit_list if rab.is_alive]
        
        wolf_list = [wolf for wolf in wolf_list if wolf.is_alive]
        
        print("total grass {} total rabbit {} total wolf {}".format(len(grass_list),len(rabbit_list),len(wolf_list)))
        state += 1
        time.sleep(0.5)
    
    print(f"total simulate {state} day")  
    print("total grass {} total rabbit {} total wolf {}".format(len(grass_list),len(rabbit_list),len(wolf_list)))
        
if __name__=="__main__":
    main()