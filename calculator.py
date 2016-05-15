# This is my second Codecool project, the Calculator program
# It shall ask for numbers and an operator
# If any of the values types are wrong, the program shall terminate
# ===================================================
# 	-=By: Csányi Levente, Codecool BP 1st semester=-

import sys
# Some introdunction for the program
print("This is a pretty simple Python calculator. \nIt can add(+), substract(-), multiply(*) or divide(/) numbers. \nIf you press any other key than numbers or operators\nthe program will terminate!")

#With the following 2 lines I can handle the bold text
bold_start = ('\033[1m')
bold_end = ('\033[0m')

#This function do the math stuff
def Add(a,b,op):
	if op == "+":
		print("Result: ",a+b)

	if op == "/":
		print("Result: ",a/b)

	if op == "*":
		print("Result: ",a*b)

	if op == "-":
		print("Result: ",a-b)

#
# I used a while loop to handle Value Error in the first place
while True:
	operators=("+-*/") #This variable responsible for the operator error // !CHECK line 37 &38 too!
	try:
		a = int(input("\nEnter a number (or a letter to " + bold_start +" exit" + bold_end + ".)"))
		op = input("Enter an operation: ")
		b = int(input("Enter another number: "))
		if op not in operators:
			print("The operator You Entered either False or this simple program can't handle it")
			exit()

	except ValueError:  # If the input not an integer the program stops
		exit()

#Calling my sole function
	Add(a,b,op)
