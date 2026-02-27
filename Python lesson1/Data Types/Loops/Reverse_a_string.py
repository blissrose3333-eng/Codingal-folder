string =input("Please enter your own String:")
string2=('')

for i in string:
    string2= i+string2

print("\n The original String=",string)
print("The Reversed String=",string2)
print("The Reversed String=",string[::-1])