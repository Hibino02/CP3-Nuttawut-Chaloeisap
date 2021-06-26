correctNumber = 333
correctNumber2 = 444
inputNumber = int(input("Please guess no.1:"))
inputNumber2 = int(input("Please guess no.2:"))
while inputNumber!=correctNumber or inputNumber2!=correctNumber2:
    inputNumber = int(input("Please guess no.1:"))
    inputNumber2 = int(input("Please guess no.2:"))
    if inputNumber > correctNumber or inputNumber2 > correctNumber2:
        print("Too Large! for no.1&2")
    elif inputNumber < correctNumber or inputNumber2 < correctNumber2:
        print("Too Small for no.1&2!")
    elif inputNumber == correctNumber or inputNumber2 == correctNumber2:
        print("Yes!!")
    elif inputNumber < correctNumber or inputNumber2 > correctNumber2:
        print("Too Small for no.1 but Too Large for no.2 !")
    elif inputNumber > correctNumber or inputNumber2 < correctNumber2:
        print("Too Large for no.1 but Too Small for no.2 !")
    elif inputNumber == correctNumber or inputNumber2 < correctNumber2:
        print("Yes! for no.1 but Too Small for no.2 !")
    elif inputNumber == correctNumber or inputNumber2 > correctNumber2:
        print("Yes! for no.1 but Too Large for no.2 !")
    elif inputNumber < correctNumber or inputNumber2 == correctNumber2:
        print("Too Small for no.1 but Yes! for no.2 !")
    elif inputNumber > correctNumber or inputNumber2 == correctNumber2:
        print("Too Large for no.1 but Yes! for no.2 !")