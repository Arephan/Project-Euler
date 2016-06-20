#Find the largest palindrome made from the product of two 3-digit numbers.

import math

def is_it_palindrome(num):
	"""Divide num into two equal parts and converge toward center"""
	num_str = str(num)
	len_num = len(str(num))
	is_palindrome = 1

	if (len_num % 2 == 0):
		iterate = len_num / 2 
	else:
		iterate = (len_num - 1) / 2
	
	for x in range (0, iterate):
		if(num_str[x] != num_str[-(x+1)]):
			is_palindrome = 0
	
	return is_palindrome


#Test all 3 digit combo, and pick out palindromes
pal_list = []

for x in range(100, 999):
	for y in range(100, 999):
		if (is_it_palindrome(x*y)):
			pal_list.append(x*y)

print max(pal_list)