#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math

_args = sys.argv[1:]

def sum_square(n):
	return sum(i**2 for i in range(n+1))

def square_sum(n):
	return sum(range(n+1))**2

def main():
	n = int(_args[0])
	print square_sum(n) - sum_square(n)

if __name__ == "__main__":
	main()