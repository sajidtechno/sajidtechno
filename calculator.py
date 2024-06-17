#Codsoft calculator for multipurpose
#Choose the operaton number that you want to perform.
#Enter only sequence number of operation that you want to perform
import math
print("Select operation -\n" 
		"1. Addition\n" 
		"2. Subtraction\n" 
		"3. Multiplication\n" 
		"4. Division\n"
		"5. Modulus\n"
		"6. Sqaure Root\n"
		"7. Factorial\n"
		"8. HCF\n"
		"9. LCM\n"
		)
#1.Addition
def add(num1,num2):
	return num1+num2

#2.subtraction
def subtract(num1,num2):
	return num1-num2

#3.multiplication
def multiply(num1,num2):
	return num1*num2

#4.Division 
def divide(num1,num2):
	return num1/num2

#5.Modulus
def modulus(num1,num2):
	return num1%num2

#6.Square Root
def square_root(num1): #enter same number for both num1 and num2
	return num1*num1

#7.Factorial
def factorial(num1):  #enter same number for both num1 and num2
	if num1==0 or num1==1:
		return 1
	else:
		return num1*factorial(num1-1)

#8.HCF
def hcf(num1,num2):
	while num2!=0:
		num1,num2=num2,num1%num2
	return(num1)

#9.LCM
def lcm(num1,num2):
	lcm=(abs(num1*num2)//math.gcd(num1,num2))
	# return abs(num1*num2)//math.gcd(num1,num2) 

# Take input from the user
option = int(input("option of operations 1, 2, 3, 4,5,6,7,8,9:"))

num1 = int(input("Enter first num1:"))
num2 = int(input("Enter second num2:"))

#Performing the addition operation
if option==1:
	print("Answer is",num1+num2)
	print("Thank you for using codesoft calculator")

#Performing the subtraction operation
elif option==2:
	print("Answer is",num1-num2)
	print("Thank you for using codesoft calculator")

#Performing the multiplication operation
elif option==3:
	print("Answer is",num1*num2)
	print("Thank you for using codesoft calculator")

#Performing the Division operation
elif option==4:
	print("Answer is",num1/num2)
	print("Thank you for using codesoft calculator")

#Performing the modulus operation
elif option==5:
	print("Modulus is ",num1%num2)
	print("Thank you for using codesoft calculator")

#Finding the square
elif option==6:
	print("Sqaure is",num1*num1)
	print("Thank you for using codesoft calculator")

#Finding the factorial
elif option==7:
	print("Factorail is ",num1*factorial(num1-1))
	print("Thank you for using codesoft calculator")

#Finding the HCF
elif option==8:
	print("HCF is",num1%num2)
	print("Thank you for using codesoft calculator")

#Finding the LCM
elif option==9:
	print("LCM is:",abs(num1%num2)//math.gcd(num1,num2)) #math.gcd-The math.gcd function in Python is used to compute the greatest common divisor (GCD) of two integers
	print("Thank you for using codesoft calculator")
    
elif option>9:
	print("Invalid input")


