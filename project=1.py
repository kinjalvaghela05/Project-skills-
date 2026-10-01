print("Welcome to the Interactive Personal Data Collector!")

name=input("Please enter your name:")
age=int(input("Please enter your age:"))
height=float(input("Please enter your height:"))
favourite_number=int(input("Please enter your favourite number:"))

current_year = 2026
birth_year = current_year - age
rounded_height = int(height)

print("Name:" , name) 
print("Age:" , age) 
print("Height:" , height)
print("Favourite_number:" ,favourite_number)


print("Type:",type(name))
print("Type:",type(age))
print("Type:",type(height))
print("Type:",type(favourite_number))


print("Memory Address:", id(name))
print("Memory Address:", id(age))
print(" Memory Address:",id(height))
print("Memory Address:", id(favourite_number))


print("your birth year is approximately:", birth_year)
print("original Height:", height)


print("Thank you for using the Personal Data collector!") 









