#!/bin/bash python3

# A very simple function to print a number
def test_number(number_of_tests):
	print("TEST_" + str(number_of_tests))


#for loop with range() function
for i in range(1, 101):
	test_number(i)

#list comprehension
num_list = [i for i in range(46) if i%3 == 0]
print(num_list)

# normal while loop with counter
counter = 0
while counter <= 46:
	test_number(counter)
	counter = counter + 1


