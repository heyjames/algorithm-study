def validate(myInput):
    myInput = int(myInput)

    if myInput == 0:
        raise Exception("Cannot be 0.")

    return myInput

# Assume n = 9
def test(n):
    if n == 3:
        return ["***", "* *", "***"]

    # "Floor" division (Rounds down to nearest whole number)
    x = test(n // 3)

    # Multiply each array element by 3.
    # Example: *** times 3 => *********
    y = []
    for a in range(len(x)):
        y.append(x[a] * 3)

    # Multiply a space by the length of an array element.
    blank = " " * len(x[0])

    # Concatenate the 1st and 3rd element with the blank spaces.
    # Example: x[0] + 3 spaces + x[0] => ***   ***
    z = []
    for b in range(len(x)): # x = 3
        z.append(x[b] + blank + x[b])

    return y + z + y

# Begin program
print("Enter 3, 9, 27:")
myInt = validate(input())

# Get array of all formatted lines.
myArray = test(myInt)

# Return each element into a new line.
print('\n'.join(myArray))
