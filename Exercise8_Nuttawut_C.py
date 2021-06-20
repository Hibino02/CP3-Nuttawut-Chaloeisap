u = input("User : ")
p = input("Pass : ")
if u == "aaa"and p == "bbb":
    print("------------------------------")
    print("Welcome to Brandon Coffee Shop")
    print("1.Americano = 100THB")
    print("2.Mocca = 80THB")
    print("------------------------------")
else:
    print("Wrong!!")
typeinput = int(input("Please select coffee type :"))
qtyinput = int(input("Qty :"))
if typeinput == 1:
    print("------------------------------")
    print("Americano (100THB) :",qtyinput,"Cup")
    print("Amount :",qtyinput * 100,"THB")
if typeinput == 2:
    print("------------------------------")
    print("Mocca (80THB) :",qtyinput,"Cup")
    print("Amount :",qtyinput * 80,"THB")
if typeinput > 2 or typeinput < 1:
    print("------------------------------")
    print("Wrong Input")
    print("------------------------------")
