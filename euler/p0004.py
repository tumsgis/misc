#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math

_args = sys.argv[1:]

def is_palindrome(x):
	s = str(x)
	length = len(s)
	head = s [:length/2]
	tail = ''
	if length % 2 == 0:
		tail = s[length/2:]
	else:
		tail = s[length/2 + 1:]
	return head == tail[::-1]

def largest_palindrome_product():
	palindromes = []
	for i in xrange(999, 99, -1):
		for j in xrange(i, 99, -1):
			if is_palindrome(i*j):
				palindromes.append(i*j)
	return max(palindromes)				
	#return sorted(set(palindromes))

def main():
	print largest_palindrome_product()

if __name__ == "__main__":
	main()