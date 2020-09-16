class Animal:
    species = 'Animal'
    legs = 0
    life_span = '1 year'
    
class Cat(Animal):
    breed = 'domistic short hair'
    kittens = 0
class Fish(Animal):
    water = 'fresh water'
    fins = 2
   
cat1 = Cat()
print(cat1.legs)
cat1.legs = 4
print(cat1.legs)

