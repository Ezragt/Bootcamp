"""
Given a list of digits, determine the integer that it represents.

For example, given the list: [8,3,5,1], your program should output 8351.

Note: You are not allowed to use conversion functions.

Hint: have a think about place values.Could you use this to ‘build’ a number,
      starting from 0, using addition?

answer: Let's see each element as a place value:  e.g. 8 is 8000
        We have (each element) * 10^(Multipliers):  e.g.  8 * 10^3
        Then we add them up: 8000 + 300 + 50 + 1 = 8351
"""

# Let's try the example first.

list1 = [8, 3, 5, 1]
output = 0

# we use for loop to access each element of the list
for x in list1:
    # get the multiplayer by using the length of the list and the index of certain element
    # e.g. list1,8 : len(list1) = 4  index(8) = 0 . we get multiplayer 4 - 0 - 1 = 3
    output += x*10**(len(list1) - list1.index(x) - 1)

print(output)
# output: 8351

# Now let's try to write a function to take list from user.


def determine_int(input_list):
    determined_int = 0
    for i in input_list:
        determined_int += i*10**(len(input_list) - input_list.index(i) - 1)

    print(determined_int)


a = [1, 3, 5, 6]
determine_int(a)
# output: 1356
