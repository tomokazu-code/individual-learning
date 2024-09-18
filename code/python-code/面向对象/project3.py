#多肽

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("wangwangwang")

class Cat(Animal):
    def speak(self):
        print("miaomiaomiao ")

def make_noise(animal:Animal):
    animal.speak()

dog=Dog()
cat=Cat()

make_noise(dog)
cat.speak()
