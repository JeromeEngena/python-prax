my_list=['Apple', 'Orange', 'Cherry']
try:
    f(x):x=input("What index of the list do you want to display?\n")
	x=int(x)
	return my_list[x]
except IndexError:
    print("Index you entered is out of range.\n")
