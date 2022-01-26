#Q1
print("Q1")
given_string="Python is a case sensitive language"
#finding length Q1-a
print("Length of the string is: " + str(len(given_string)))
#reversing order Q1-b
print("The reversed string is: " + given_string[-1::-1])
#slicing string Q1-c
new_string= given_string[10:26]
print("Sliced string is: " +new_string)
#replacing the new string Q1-d
new_string.replace("a case sensitive","object oriented")
#finding index of a Q1-e
print("The index of substring a is: " + str(given_string.find("a")))
#removing the white spaces Q1-f
print("After removing spaces: " +given_string.replace(" ",""))
#Q2
print("Q2")
name=input("Enter your name:")
sid=int(input("Enter your SID:"))
cgpa=float(input("Enter your CGPA:"))
dpt_name=input("Enter your department name:")
print("Hey,%s"%name+ " Here!")
print("My SID is %d"%sid)
print("I am from %s"%dpt_name+" department and my CGPA is %f"%cgpa)
#Q3
print("Q3")
a=56
b=10
print("a:",a&b)
print("b:",a|b)
print("c:",a^b)
print("d:",a<<2,b<<2)
print("e:",a>>2,b>>4)
#Q4
print("Q4")
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))
d=[a,b,c]
print("largest number is:",max(d))
#Q5
print("Q5")
user_string= input("Enter a string:")
if "name" in user_string:
    print('Is the word "name" in the string? Yes')
else:
    print('Is the word "name" in the string? No')
#Q6
print("Q6")
no_1=int(input("Enter first length:"))
no_2=int(input("Enter second length:"))
no_3=int(input("Enter third length:"))
if no_1+no_2>no_3 and no_1+no_3>no_2 and no_2+no_3>no_1:
    print("Yes")
else:
    print("No")



