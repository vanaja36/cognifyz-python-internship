unit = input("Is this temperature in celsius or Fathernheit (c/f): ")
temp = float(input("enter the temperature: "))


if unit == "C" :
    temp = round((9* temp)  /5 + 32 , 1)
    print(f"The temperature in fahrenheit is:{temp} F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9 ,1)
    print(f"The temperature in celsius is: {temp} C")
else:
    print(f"{unit} is an invalid unit of measurement")

