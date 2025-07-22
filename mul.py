#!/usr/bin/env python3

num=int(input("Enter the number"))

def mult(opl):
	for i in range(10):
		print(f"{num}*{i}={num*i}")

mult(num)
