#!/usr/bin/env python3

stro=input("Enter the string")

def revstr(pla):
	rev=""
	count=0
	for i in pla:
		rev = i + rev
		if i in ('a','e','i','o','u') :
			count+=1
	return rev,count

print(revstr(stro))	
