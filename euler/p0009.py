#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math, operator

_args = sys.argv[1:]

def pyth_triplet():
	triplet = []
	a = 2
	while len(triplet) == 0:
		for b in xrange(a):
			c2 = a**2 + b**2
			c = math.sqrt(c2)
			if c.is_integer() and a+b+c == 1000:
				triplet = [a,b,int(c)]
		a += 1
	return triplet, reduce(operator.mul, triplet, 1)

def main():
	print pyth_triplet()

if __name__ == "__main__":
	main()