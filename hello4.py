#day4 types of operation in python 
#arithmetic operators 

#Additions 
num1 = 3
num2 = 5
total = num1+num2
print(total)

#Substrtaction 
num1 = 5
num2 = 9
total = num1 - num2 
print(total)

#Multiplication
num1 = 5
num2 = 9
total = num1 * num2 
print(total)

#divide 
num1 = 5
num2 = 9
total = num1 / num2 
print(total)

#floor division
num1 = 5
num2 = 9
total = num1 // num2 
print(total)

#Modulus 
num1 = 5
num2 = 9
total = num1 % num2 
print(total)

#Exponent 
num1 = 5
num2 = 9
total = num1 ** num2 
print(total)

# Relation Operation 
''' == equal to , != Not Equal , > Greater than, < less than , >= Greater than or equal , <= Less than or equal  '''
#example
num1 = 10
num2 = 40

print(num1 == num2 )
print(num1 != num2)
print(num1 < num2)
print(num1 > num2 )
print(num1 <= num2)
print(num1 >= num2)

#Assignment operation 
''' = assign value , += add value and assign , -= Subtact and assign value, *= multiply and assign , /= divide and assign , //= floor divide and assign , % = Modules and assign , **= Power and assign  '''
#example 
num1 = 10 

num1 += 5
print(num1)

num1 -= 7
print(num1)

num1 *= 10
print(num1) 

#logocal operation 
'''and  both conditions must be true , or At least one condition must be true , not reverse the result '''
#example 
#and
age = 20 
citizen = True 
print(age >= 18 and citizen)

#or 
print(10>20 or 5<10)

#not 
print(not True )
print(not False)

#bitwise operator
''' & and , |  or, ^ Xor , ~ Not , << Left side , >> Right side '''
#and (&)
print(5&8)

#or (|)
print(5|3)

#(^) xor
print(5^3)

# left side (<<)
print(5<<1)

# right side 
print(8>>1)

#member ship opertor 
# in Exists ,not in Does not exists 

Fruits = ["Apple", "Banana" ," Mango "]
print("Apple" in  Fruits)
print("Orrgange " in Fruits)

#same as identity operator 
# is same  opject and is not Different object
a = [1,2,3]
b = a
c = [1,2,3]

print( a is b)
print(a is c)

#unary operations 
# + unary plus , - unary minus, not logical not , ~bitwise not 
#example
x = 10 

print(+x)
print(-x)
print(~5)
print(not False )
