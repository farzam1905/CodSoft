import time

def add(n1, n2):
    r = n1 + n2
    return r

def sub(n1, n2):
    p = n1 - n2
    return p

def mul(n1, n2):
    o = n1 * n2
    return o

def div(n1, n2):
    u = n1 / n2
    return u

def exp(u1, u2):
    t = u1 ** u2
    return t

def floor(u1, u2):
    w = u1 // u2
    return w
initial_time = time.time()
ch = "0"
while ch == "0":
    print("\t\t\t\t\t\t\tMenu\nPress 1 for division\nPress 2 for multiplication\nPress 3 for addition\nPress 4 for subtraction\nPress 5 for exponent/power\nPress 6 for floor division\n")
    
    u1 = int(input(""))

    if u1 == 3:
        try:
            o = int(input("Enter 1st number for addition: "))
            t = int(input("Enter 2nd number for addition: "))
        except ValueError:
            print("Invalid Value")
        except:
            print("An Error occurred")
        else:
            print("Addition =", add(o, t))

    elif u1 == 4:
        try:        
            p = int(input("Enter 1st number for subtraction: "))
            l = int(input("Enter 2nd number for subtraction: "))
        except ValueError:
            print("Invalid Value")
        except:
            print("An Error occurred")
        else:
            print("Subtraction =", sub(p, l))

    elif u1 == 2:
        try:
            o = int(input("Enter 1st number for multiplication: "))
            t = int(input("Enter 2nd number for multiplication: "))
        except ValueError:
            print("Invalid value")
        except:
            print("An Error occurred")
        else:
            print("Multiplication =", mul(o, t))

    elif u1 == 1:
        try:
            o = int(input("Enter 1st number for Division: "))
            t = int(input("Enter 2nd number for Division: "))
            if t == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Cannot be divided by zero")
        except ValueError:
            print("Invalid value")
        except TypeError:
            print("Invalid type")
        except:
            print("An Error occurred")
        else:
            print("Division =", div(o, t))

    elif u1 == 5:
        try:
            o = int(input("Enter number for to which you want to apply power/exponent: "))
            t = int(input("Enter power/exponent: "))
        except ValueError:
            print("Invalid Value")
        except:
            print("An Error occurred")
        else:
            print("Result =", exp(o, t))

    elif u1 == 6:
        try:
            o = int(input("Enter 1st number for floor Division: "))
            t = int(input("Enter 2nd number for floor Division: "))
            if t == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Cannot be divided by Zero")
        except ValueError:
            print("Invalid Value")
        except:
            print("An Error Occurred")
        else:
            print("Floor Division =", floor(o, t))
    
    ch = input("Enter 0 to try again else press any key to exit:\n")
end_time = time.time()
total_time = int(end_time - initial_time)
print(f'You spend {total_time} seconds')
print("Thanks for using me!\nHave a nice day :)")


