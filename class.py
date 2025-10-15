# Class describing my favorite animal: Cat
class Cat:
    def __init__(self, armLength, legLength, numEyes, hasTail, isFurry):
        self.armLength = armLength
        self.legLength = legLength
        self.numEyes = numEyes
        self.hasTail = hasTail
        self.isFurry = isFurry

    def print_animal(self):
        print("Physical characteristics of my favorite animal (Cat):")
        print(f"Arm length: {self.armLength} inches")
        print(f"Leg length: {self.legLength} inches")
        print(f"Number of eyes: {self.numEyes}")
        print(f"Has a tail: {self.hasTail}")
        print(f"Is furry: {self.isFurry}")

def main():
    # Create and print instance
    my_cat = Cat(
        armLength=4.5, 
        legLength=6.0, 
        numEyes=2, 
        hasTail=True, 
        isFurry=True
        )
    
    my_cat.print_animal()

if __name__ == "__main__":
    main()