temp = float(input("Enter the temperature: "))
unit = input("In Celsius or in Fahrenheit(C/F): ")

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    unit = "ºF"
    print(f"In Farenheit, the temperature is: {temp} {unit}.")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = "Cº"
    print(f"In Celsius, the temperature is: {temp} {unit}.")
else:
    print(f"{unit} was not valid!")
