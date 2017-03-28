#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math

_args = sys.argv[1:]

def largest_prime_factor(n):
	factors = []
	d = 2
	while n > 1:
		while n % d == 0:
			factors.append(d)
			n /= d
		d += 1
	return factors[-1]

def main():
	n = int(_args[0])
	print largest_prime_factor(n)

if __name__ == "__main__":
	main()