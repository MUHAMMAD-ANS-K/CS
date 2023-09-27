def main():
    user_input = input("Expression: ")
    x, y, z = user_input.split(" ")
    if y == "+":
        print(float(int(x) + int(z)))
    elif y == "-":
        print(float(int(x) - int(z)))
    elif y == "/":
        print(float(int(x) / int(z)))
    else:
        print(float(int(x) * int(z)))
if __name__ == "__main__":
    main()