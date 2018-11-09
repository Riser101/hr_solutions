#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	number_of_pairs=0
	hashMap={}
	for item in ar:
		if item not in hashMap:
			hashMap[item] = 1
		else:
			number_of_pairs+=1
			del(hashMap[item])
	return number_of_pairs

sockMerchant(9, [10,20,20,10,10,30,50,10,20])

'''
{10:4, 20:3, 30:1, 50: 1}
number_of_pairs for 10 => 2
number_of_pairs for 20 => 1
number_of_pairs for 30 => 0
number_of_pairs for 50 => 0
'''