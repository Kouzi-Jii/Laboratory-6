age = int(input("please enter your age: "))
mem = str(input("Are you a member?(yes or no): "))

if age <= 17 and age >= 1 and mem == "yes":
    print("Your fee is 450.00 pesos")
elif age <= 17 and age >= 1 and mem == "no":
    print("Your fee is 650.00 pesos")
elif age >= 18 and age <65 and mem == "yes":
    print("Your fee is 550.00 pesos")
elif age >= 18 and age <65 and mem == "no":
    print("Your fee is 750.00 pesos")    
elif age >= 65 and mem == "yes":
    print("Your fee is 400.00 pesos")
elif age >= 65 and mem == "no":
    print("Your fee is 600.00 pesos")
else:
    print("Invalid values entered.")