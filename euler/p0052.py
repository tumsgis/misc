#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math

_args = sys.argv[1:]

def smallest_int():
	smallest = 0
	i = 1
	while smallest == 0:
		for j in range(1, 7):
			if j == 6:
				smallest = i
			if set(list(str(i*j))) != set(list(str(i*(j+1)))):
				break
		i += 1
	return smallest

def main():
	print smallest_int()

if __name__ == "__main__":
	main()