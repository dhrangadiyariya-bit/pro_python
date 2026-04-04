"""try:
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    result=a/b
    print("result:",result)
except zerodivisionerror:   
    print("error:cannot divide by zero:")
except valueerror:
    print("error:please enter only integers")     """
print("program start")
try:
    result=10/0
    print("result:",result)
except:
    print("an error occurred.division by zero is not allowed")
    print("program end")        