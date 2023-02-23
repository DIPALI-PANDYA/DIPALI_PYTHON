"""
#WAP sum of first n +ve integers
n = int(input("Enter the No.:"))
sum=0
for i in range(0,n+1):
    sum=sum+i
    n=n-1


print("Sum:",sum)


#WAP to find out if the number is positive or negative
n = int(input("Enter the No.:"))
if n>0:
    print("No. is positive")
else:
    print("No. is negative")

#WAP to find maximum number
n1= int(input(" Enter the value= "))
n2= int(input(" Enter the value= "))
if(n1>n2):
    print("N1 is maximum")
else:
    print("N2 is maximum")
"""
#WAP to get student's percentage using ladder if else
roll= int(input("Enter your Roll No.: "))
name= input("Enter your name: ")
p= int(input("Enter Physics marks"))
m= int(input("Enter Maths marks"))
c= int(input("Enter Chemistry marks"))
total= (p+m+c)
per= (total/3)
print()
print("Roll no.: ",roll)
print("Name: ",name)
print("Total: ",total)
print("Percentage: ",per)


if per>=75:
      print("Class is Distinction")
elif per>=65:
        print("First Class")
elif per>=55:
        print("Second Class")
elif per>=45:
        print("Pass Class")
else:
        print("Fail")























