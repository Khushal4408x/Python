class Animal:
    def speak(self):
        print("Animal Speaking!")

class Dog(Animal):
    def speak(self):
        print("Dog barking!")

d = Dog()
d.speak()  # Output: Dog barking!
