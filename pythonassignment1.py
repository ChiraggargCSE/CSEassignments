#Q1
a= float(input("Number 1 : "))
b=float(input("Number 2 : "))
c=float(input("Number 3 : "))
average= (a+b+c)/3
print( "Average: " +str(average))
#Q2
grossincome= float(input("Enter your gross income(in $): "))
dependents= float(input("Enter number of dependents: "))
standard_deduction= 10000
taxableincome= (grossincome - standard_deduction)-(3000*dependents)
print("Taxable income: " +str(taxableincome))
tax= (taxableincome*20)/100
print("Tax: " +str(tax))
#Q3
SID= input("SID: ")
name=input("Name: ")
gender=input("Gender: ")
course=input("Course name: ")
cgpa=float(input("CGPA: "))
list=[SID,name,gender,course,cgpa]
print(list)
#Q4
q= float(input("Enter marks of student 1: "))
w= float(input("Enter marks of student 2: "))
e= float(input("Enter marks of student 3: "))
r= float(input("Enter marks of student 4: "))
t= float(input("Enter marks of student 5: "))
list= [q,w,e,r,t]
list.sort()
print(list)
#Q5a
list =['Red','Green','White','Black','Pink','Yellow']
print("Colour: ")
print(list)
list.remove('Green')
print("After removing element")
print(list)
#Q5b
list =['Red','Green','White','Black','Pink','Yellow']
print("Colour: ")
print(list)
list.remove('Black')
list.remove('Pink')
list.append('Purple')
print(" After editing: ")
print(list)
