Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum_of_n (n):
	the_sum = 0
	for i in range (1,n+1):
		the_sum = the_sum + i
	return the_sum
print (sum_of_n(10))