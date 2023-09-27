def main():
    user_input = input("Expression: ")
    x, y, z = user_input().split(" ")
    if y == "+":
        print(float(x + y))
    elif y == "-":
        print(float(x - y))
    elif y == "/":
        print(float(x / y))
    else:
        print(float(x * y))
if __name__ == "__main__":
    main()