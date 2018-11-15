'''
## left rotation algorithm
1. reverse the entire array
2. for n, reverse from start = (length of array - n) to idx = idx of end of array
3. for n, reverse from start = 0 idx of array to idx = length of array - (n + 1)
'''

def left_rotation(n, array):
	reversed_array = execute_reversal(0, len(array)-1, array)
	start=len(reversed_array)-n
	intermediate_array = execute_reversal(start, len(array)-1, reversed_array)
	end=len(array)-(n+1)
	final_array = execute_reversal(0, end, intermediate_array)
	return final_array

'''
## right rotation algorithm
## note : n = number of rotations
1. reverse the entire array
2. for n, reverse from idx 0 to n-1
3. for n, reverse n to end of array
'''

def right_rotation(n, array):
	reversed_array = execute_reversal(0, len(array)-1, array)
	end=n-1
	intermediate_array = execute_reversal(0, end, reversed_array)
	start=n
	final_array = execute_reversal(start, len(intermediate_array)-1, intermediate_array)
	return final_array

def execute_reversal(start, end, array):
	while(start<end):
		temp=array[end]
		array[end]=array[start]
		array[start]=temp
		start+=1
		end-=1
	return array

print 'right rotated array: '  
print right_rotation(2, [1,2,3,4,5]);	
print ''
print 'left rotated array: '
print left_rotation(2, [1,2,3,4,5]);	