#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math

_args = sys.argv[1:]
_numbers = range(3, 21)

def smallest_evenly_div():
	res = 0
	i = 20
	while res == 0:
		for num in _numbers:
			if i % num != 0:
				break
			if num == _numbers[-1]:
				res = i
		i += 20
		#divs = [i / float(num) for num in _numbers]
		#if all(div.is_integer() for div in divs):
		#	res = i
		#i += 2
	return res

def main():
	print smallest_evenly_div()

if __name__ == "__main__":
	main()