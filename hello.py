print("    ___SCHOOL MARKING RESULT PLATFORM___")

name = input("enter your name: ")
marks = int(input("enter Your marks: "))

if marks > 100 or marks < 0:
    print("Invalid input!")
elif marks > 75:
     print(f"{name}, you have A pass")
elif marks >= 65:
    print(f"{name}, you have B pass")
elif marks >= 55:
     print(f"{name}, you have C pass")
elif marks >= 35:
     print(f"{name}, you have S pass")
else:
     print(f"{name}, you are fail.")

