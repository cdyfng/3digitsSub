#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)


def Subtraction(num):
	num = int(num)	
	l = list([num/100, num%100/10, num%10])
	l2 = sorted(l)
	maxx = l2[2]*100 + l2[1]*10 + l2[0]
	minn = l2[0]*100 + l2[1]*10 + l2[2]
	print("maxx: ", maxx, "min", minn, " result: ", maxx-minn)
	return maxx-minn

def contain_same_list(num1, num2):
	num1 = int(num1)
	num2 = int(num2)
	l1 = sorted(list([num1/100, num1%100/10, num1%10]))
	l2 = sorted(list([num2/100, num2%100/10, num2%10]))
	#print (l1, l2)
	#print( l1 == l2)
	return l1 == l2

input = sys.argv[1]
output = Subtraction(input)
while(not contain_same_list(input, output)):
	input = output
	output = Subtraction(input)




