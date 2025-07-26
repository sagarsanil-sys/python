#!/usr/bin/env python3

PFA="names.txt"

def totname(plo):
	count=0
	length=0
	longest=""
	try:	
		with open(PFA,"r") as file:
			for i in file:
				count+=1
				#length=len(i.strip())
				if len(i) > len(longest):
					longest = i	
					pl=len(longest)
				if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or  i[0] == 'u' or i[0] == 'A' or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U' :
					print(i)	
			return print(f"{count},{pl}")
	except FileNotFoundError:
		print(f"Error: File '{PFA}' not found")

totname(PFA)
