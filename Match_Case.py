a = int(input("Enter the Number :"))
match a:
    case 0:
        print("a = 0")
    case 1:
        print("a = 1")
    case _ if a == 10:
        print("ERROR 1")
    case _ if a==20:
        print("ERROR 2")
    case _ if a==30:
        print("ERROR 3")
def name ( a,b):
    if(a>b):
        print("a is grater")
    else:
        print("B is grater")
