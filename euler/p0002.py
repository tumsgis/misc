#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

_args = sys.argv[1:]

def even_fibo_sum(max):
	fibos = []
	max_fibo = 0
	while max_fibo < max:
		length = len(fibos)
		if length < 2:
			max_fibo = length + 1
		else:
			max_fibo = fibos[length-2] + fibos[length-1]
		fibos.append(max_fibo)
	return sum(fibo for fibo in fibos if fibo % 2 == 0)


def main():
	max = int(_args[0])
	print even_fibo_sum(max)

if __name__ == "__main__":
	main()