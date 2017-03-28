#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

_args = sys.argv[1:]
_numbers = [3, 5]

def multiples(n):
	sum = 0
	for i in range(1, n):
		if any(i % number == 0 for number in _numbers):
			sum += i
	return sum

def main():
	n = int(_args[0])
	print multiples(n)

if __name__ == "__main__":
	main()