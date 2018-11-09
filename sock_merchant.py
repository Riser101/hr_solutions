'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer n, the number of socks represented in ar. 
The second line contains  space-separated integers describing the colors  of the socks in the pile.

Sample Input

9
10 20 20 10 10 30 50 10 20
Sample Output

3
'''

#!/bin/python3

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

	print number_of_pairs			
	return number_of_pairs

sockMerchant(9, [10,20,20,10,10,30,50,10,20])

'''
{10:4, 20:3, 30:1, 50: 1}
number_of_pairs for 10 => 2
number_of_pairs for 20 => 1
number_of_pairs for 30 => 0
number_of_pairs for 50 => 0
'''