# function 'equation' that returns x ** 3 + 8
def equation(x):
    return x ** 3 + 8

def main():
    # print equation with x = 9
    result = equation(9)
    print(result)
    # if result is greater than 27, prints "YAY!"
    if result > 27:
        print("YAY!")

if __name__ == "__main__":
    main()