# Class to tabulate sin(x) over x
import math

class Sine:
    def __init__(self, x):
        self.x = x

    def tabulate(self):
        return math.sin(self.x)

def main():
    # Iterate n times
    # For x = 0, to x = 2*pi, in steps of 2pi/n
    n = 1000
    for i in range(n):
        x = (2 * math.pi * i) / n
        sine_instance = Sine(x)
        print(f"x: {x:.5f}, sin(x): {sine_instance.tabulate():.5f}, n: {i}")
    

if __name__ == "__main__":
    main()