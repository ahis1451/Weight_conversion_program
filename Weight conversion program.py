#weight conversion program
print('Figure out what your weight is in the other metric!!!')
weight = float(input("Enter your weight: "))
unit = input("Thats in Kilograms or Pounds? (K/L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else: print(f'{unit} is not valid')

print(f'Your converted weight is equal to {round(weight,1)} {unit}')