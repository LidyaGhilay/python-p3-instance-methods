class Dog:
    # Class body goes here

    # Instance method definition
    def bark(self):
        print("Woof!")

    def sit(self):  # <--- Move the sit method inside the class definition
        print("The dog is sitting.")

if __name__ == "__main__":
    fido = Dog()
    fido.bark()  
    fido.sit()