'''token is the smallest unit in a python program 
the token has main five types of token in our python program 
1. keywords 
2. identifiers
3.Literals
4.operators
5.Punctuators  
'''
#some program to learn keywords 
for i in range(5):
  print(i) 
  #in there there is for and in are keywords 

#indentifiers to learn (it is nothing but the name given to the variable, function, class )
name = "Manish"
age =21
#in there there are name and age are indentifiers

#literals are those fixed value are written directly inthe code 
name = "Manish"
age =21

#operators perform operation like(+,-,*,/,**,//,%) there are arithmetic operators 
# campersion operators (==, != ,<,>,<=,>=)
a = 2
b = 5
c = a+b
d = a-b
e = a*b
f = a/b
g = a**b
h = a//b 
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

#punctuators are symbols to organized sentence structure in programming([] {} () , . ; : )
print("hello")
#in there we can use () punctuators


#Expression Execution 
# string & Number value can operate together with *
A,B = 2,3
Txt = "@"
print(2*Txt*3)

# string & string can operate with + 
A,b = "2",3
Txt = "@"
print((A+Txt) *b) 

# numeric value can operate with all arithmetic operators 
a,b = 2,3
c = 4 
print(a+b*c)

#Arithmetic expression with integer and float will result is float 
a,b = 10 ,5.0
c = a*b
print(c)

b,a = 5.0 , 23
c = b*a
print(c)

# result of devision  operator with two integers will be float
a,b = 1,2
c = 1/2
print(c) 

a = 3
b = 4
c = a/b
print(c)
print(type(c))

# integer division with float and int will get displayed as float 
a = 10.00 
b = 4
result = a//b
print(result)
print(type(result))

#Remimber is negative when demoniator is nagative 
a,b =-5,4
c = a%b
print(c)