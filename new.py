print('Hello World')

class MySub:
    def __init__(self , name , age):
        self.name  = name 
        self.age = age 

    def getName(self):
        return f"My name is {self.name}, my name is WHOO! My name is chickkuu chickkuu {self.name}"

slimshady = MySub('Slimshady' , 48)
print(slimshady.getName())