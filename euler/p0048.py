#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math, operator

_args = sys.argv[1:]

def self_powers():
	f11_sum = 0
	f11_sum_str = ''
	for i in xrange(1,1001):
		f11_sum += i**i
		f11_sum_str = str(f11_sum)[-11:]
		f11_sum = int(f11_sum_str)
	return f11_sum_str[-10:]

# þetta fall er hraðara, svekkjandi...
def self_powers2():
	num = 0
	for i in range(1,1001):
	    num+=i**i
	print str(num)[-10:]

def main():
	#print self_powers()
	print self_powers2()

if __name__ == "__main__":
	main()