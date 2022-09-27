class Dog:
    
    race = "Big dog"
    
    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name and self.age == other.age
        
    def more_age(self, more):
        
        new_age = self.age * more
        print(new_age, self.race)
        
dog = Dog("bru", 1)
dog.age = 2
dog.more_age(4)
print(dog)

print("***********************************")

class Bulldog(Dog):
    
    name_dog = "bulldog"
    
    def more_age(self, more=5): # override parent method
        
        new_age = self.age + more # child class method
        old_age = super().more_age(more) # parent class method
        
        print(new_age, self.name_dog)
                        
        
dog1 = Bulldog("bru", 2)
dog1.more_age()
print("***********************************")
print(isinstance(dog1, Dog))
print(isinstance(dog1, Bulldog))
print("***********************************")
print(dog == dog1) # two distinct objects in memory (space)