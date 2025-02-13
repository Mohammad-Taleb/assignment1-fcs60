# mohmmad taleb fcs 60
# my first time trying git here so please excuse any mistakes, thanks 

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age > 0:
    if 1 <= age <= 7:
      print(f"{name} your price ticket is $5")
    elif age >= 18:
      print(f"{name} your price ticket is $15")
    elif age <= 18:
      print(f"{name} your price ticket is $10")
else:
  print("Enter a valid age")