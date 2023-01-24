#To receive a console value we use Input

name = input("Enter your name: ")


#Convert String to Int

age = int(input("Write your age: "))


print(f"Hi! {name} you have {age} years old")

#Excercise quadratic

print("Enter 3 number")
a = int(input("number 1 :"))
b = int(input("number 2 :"))
c = int(input("number 3 :"))

root1 =  (-b + (b * b - 4 * a * c) **0.5) / (2 * a)
root2 = (-b - (b * b - 4 * a * c ) **0.5) / (2 * a)

print(root1)
print(root2)