weight=float(input("enter ur weight: "))
unit=input("enter the unit: (K or L)")
if unit=="K":
    weight*=2.205
    unit="lbs"
    print(f"Your weight is: {round(weight,2)} {unit} ")
else:
    weight/=2.205
    unit="kgs"
    print(f"Your weight is: {weight} {unit}")
