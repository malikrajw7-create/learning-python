#conditional statement in python 
#if___ else statemnet 
age = int(input("Enter the number : "))

if age > 18:
  print("You are Eligible for vote.")
else:
  print("You are not Eligible for vote.")

num = int(input("Enter your number: "))

if num % 2 == 0 :
  print("Number is Even Number.")
else:
  print("Number is odd.")

#if__elif_else statement 
  marks = int(input("Enter your marks :"))

  if marks > 90:
    print("Grade A")
  elif marks > 75:
    print("Grade B")
  elif marks > 50:
    print("Grade C")
  else:
    print("Fail")

#Nested if 
age = int(input("Enter your age:"))
marks = int(input("Enter your marks"))

if age > 17 :
  if marks > 60:
    print("You are Eligible for admission .")
  else:
    print("Your Marks was two low ")
else:
     print("Your age was not met")

#string 
str1 = """this ia a string/t this is manish """

#basic opertion 

#concatenation
str2= "manish"
str3= "kumar"
final_str= str2+str3
print(final_str)

#length of funstion 
str1 = "manish"
len(str1)

#intexing in python
str = "Manish kumar "
ch = str[5]
print(ch)
print(str[0])

#slicing:Accessing part of a string
str ="Manish kumar "
print(str[:6])#[0:6]
print(str[5:])#[5:len(str)]
print(str[-5:-1])

#string function
str= "manish kumar"
print(str.endswith("mar"))
print(str.capitalize())
print(str)
print(str.replace("m"," a"))
print(str.find("m"))
print(str.count("a"))

#WAP to input user fist name & print its length
name = input("Enter your first name :")
print(len(name))

#list in Python
"""its ia built in data type in python """
marks = [2,5,8,9,8,7,]
print(type(marks))
print(marks[0])
print(marks[1])
student = [ "Manish",20, 2320661]
print(student[0])
student[0]= "Malik"
print(student[0])
print(student[0:2])
print(student[:3])
print(student[0:])

#list method
list = [2,1,4]
list.append(3)
print(list)

print(list.sort())
print(list)
list.sort(reverse = True)
print(list)
