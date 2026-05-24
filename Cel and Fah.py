temp=float(input("Enter the temp: "))
unit=input("enter the unit: (C or F)")
if unit=="C":
    temp=round((temp*9)/5+32,1)
    print(f"The temperature is: {temp} F")
elif unit=="F":
    temp=round((temp-32)/1.8,2)
    print(f"The temperature is: {temp} C")
    
else:
    print(f"this {unit} is not valid")
    
