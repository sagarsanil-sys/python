#!/usr/bin/env python3

def numchek(numo):
	
	if numo < 0:
		print("Number is negative")
	elif numo > 0:
		print("Number is positive")
	else:
		print("Number is zero")
try:
	num=int(input("Enter your number"))
	numchek(num)
except ValueError:
	print("Enter a number not a string")
