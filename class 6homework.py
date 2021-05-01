class Cat():
    def __init__(self,color,weight,time,speed):
        self.color = color
        self.weight = weight
        self.time = time
        self.speed = speed
        self.rt = 0
    def run(self):
            self.rt = self.speed * self.time - self.weight * 4
            return self.rt

class Dog():
    def __init__(self,color,weight,time,speed):
        self.color = color
        self.weight = weight
        self.time = time
        self.speed = speed
        self.sp = 0
    def run(self):
            self.sp = self.speed * 2 * self.time - self.weight * 4
            return self.sp

    
    

            
cat1 = Cat((255,255,255),23,45,56)

print("跑了" + str(cat1.run()) + "公尺")

dog1 = Dog((255,34,123),34,34,45)
print("跑了" + str(dog1.run()) + "公尺")