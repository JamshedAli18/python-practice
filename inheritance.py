class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Example
d = Dog()
d.speak()  # from parent
d.bark()   # from child

