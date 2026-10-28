'''try:
    age=int(input("Enter Your Age: "))
    print(age)
except Exception as a:
    print("Enter a valid number for your age.")
    print(a)
    print(type(a))
    print(a.__class__)
    print(a.__class__.__name__)

print("End")
"--------------------------------------------------------------------------"
'''
'''
try:
    x=10/0
except Exception as b:
    print(b)
    print(type(b))
    print(b.__class__)
    print(b.__class__.__name__)
    print(type(b))
    print(b.__class__)
    print(b.__class__.__name__)
"---------------------------------------------------------------------------------"

try:
    number=int(input("Enter a Number: "))
    result=10/number
    print("The test result is : ",result)
except ZeroDivisionError:
    print("Division by zero is not allowed ")
except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print(e)
'''

'''
try:
    num=int(input("Ener a number "))
    result=10/num
    print("The test result is : ",result)
except (ZeroDivisionError,ValueError,LookupError):
    print("Enter Valid NUmber")
except Exception as e: 
    print(e)

'''


# write the proram to read containt of file using file hadling concept and if file is not present then print appopriate massege

import os
try:
    f=open("exception_name.txt","r")
    lines=f.readlines()
    line1=f.readline()
    f.close()
except Exception :
    print("File Not Found")
finally:
    print("End of the program")
