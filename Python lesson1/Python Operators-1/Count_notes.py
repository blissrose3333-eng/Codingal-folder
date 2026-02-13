Amount=int(input("Enter your withdrawal here:"))

note1 =Amount//100
note2=(Amount%100)//50
note3=((Amount%100)%50)//10

print("The number of 100 rupees",note1)
print("The number of 50 rupees",note2)
print("The number of 10 rupees",note3)