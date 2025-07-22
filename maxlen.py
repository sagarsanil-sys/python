#!/usr/bin/env python3

lopq=["Ravi", "Snehalata", "John", "Aman", "Siddharth"]

def pl(pj):
		#longest_word=max(pj,key=len)
		longest_word=sorted(pj, key=len, reverse=True)[:3]
		print(longest_word)
		
pl(lopq)
