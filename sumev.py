#!/usr/bin/env python3

num =int(input("Enter the number"))

def eveodd(kpo):
	sump=0
	for i in range(101):
		if i%2==0:
			sump+=i
	return sump

print(eveodd(num))
