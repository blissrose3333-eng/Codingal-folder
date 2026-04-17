import math

degree_angle = float(input("Enter angle in degrees: "))

radian_angle = math.radians(degree_angle)

sin_va = math.sin(radian_angle)
cos_va = math.cos(radian_angle)
tan_va= math.tan(radian_angle)

# Display results rounded to 4 decimal places
print(f"Results for {degree_angle}°:")
print(f"Sin:   {round(sin_va, 4)}")
print(f"Cos: {round(cos_va, 4)}")
print(f"Tan:{round(tan_va, 4)}")
