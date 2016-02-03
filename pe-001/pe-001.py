###############################################################################
# Author: Ariel Skye Levy	 												  # 
# Date: 02-02-2016															  #
#																			  #
# Project Euler 001															  #
#   Multiples of 3 and 5													  # 
###############################################################################

'''
PROBLEM

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

result = 0  # sum of multiples

for i in range(1000):
	if( (i%3 == 0) | (i%5 == 0) ):
		result += i

print(result)
