# miles_per_gallon.py
""" Calculate miles per driven using input provided by user"""

print()

miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons of gas used: "))

miles_per_gallon = round(miles_driven / gallons_used, 2)

print("\n───────────────────────────────────────────────────────")
print("The Miles Per Gallon program\n")
print(f"      Miles Driven: {miles_driven}")
print(f"      Gallons Used: {gallons_used}")
print(f"  Miles Per Gallon: {miles_per_gallon}")
print("───────────────────────────────────────────────────────\n")
