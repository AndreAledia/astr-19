import random


# Print "Hello World" to the console
def PrintSum():
    # random float 'a' between 0 and 100
    a = random.uniform(0, 100)
    # random float 'b' between 0 and 100
    b = random.uniform(0, 100)
    # print a
    print("a:", a)
    # print b
    print("b:", b)
    # print and calculate sum c of a and b
    c = a + b
    # print data type of c
    print("c is of type:", type(c))
    print(c)

def PrintDifference():
    # random integer 'a' between 0 and 100
    a = random.randint(0, 100)
    # random integer 'b' between 0 and 100
    b = random.randint(0, 100)
    # print a
    print("a:", a)
    # print b
    print("b:", b)
    # print and calculate difference c of a and b
    c = a - b
    # print data type of c
    print("c is of type:", type(c))
    print(c)
    
def PrintProduct():
    # random integer 'a' between 0 and 100
    a = random.randint(0, 100)
    # random integer 'b' between 0 and 100
    b = random.uniform(0, 100)
    # print a
    print("a:", a)
    # print b
    print("b:", b)
    # print and calculate product c of a and b
    c = a * b
    # print data type of c
    print("c is of type:", type(c))
    print(c)
    
# Main function to execute the print function
def main():
    PrintSum()
    PrintDifference()
    PrintProduct()

# When we run the program, call the main function
if __name__ == "__main__":
    main()