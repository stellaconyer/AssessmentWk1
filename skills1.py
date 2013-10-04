# Things you should be able to do.
my_ints = [5, 4, 2, 25]
my_list = ["one", "two", "four", "or", "more"] 

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = []    
    for i in my_list:
        if i % 2 == 1:
            new_list.append(i)
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.


new_list = []
def long_words(word_list):
    for i in my_list:
        if len(i) >= 4:    
            new_list.append(i)
    return new_list


# Write a function that finds the smallest element in a list of integers and returns it


def smallest(some_list):
    smalls = my_ints[0]
    for i in my_ints:
        if i < smalls:
            smalls =  i
    return smalls    


def bubble_sort(some_list):
    bubble_range = len(my_ints)-1  
    while bubble_range != 0: 
        for i in range(bubble_range):
            print bubble_range, my_ints[i], my_ints[i + 1]  
            if my_ints[i] > my_ints[i + 1]:
                my_ints[i], my_ints[i+1] = my_ints[i+1], my_ints[i]
        bubble_range = bubble_range - 1
             
    return my_ints

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    large = my_ints[0]
    for i in my_ints:
        if i > large:
            large =  i
    return large   

print largest(my_ints)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    for i in my_ints:
        new_list.append(i/2)
    return new_list


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    for i in my_list:
        new_list.append(len(i))
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum_of_nums = 0
    for i in my_ints:
        sum_of_nums += i
    return sum_of_nums



# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mult_num = 1
    for i in my_ints:
        mult_num = mult_num*i
    return mult_num

   

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    string = ""
    for i in my_list:
        string = string+i
    return string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    sum = 0
    for i in my_ints:
        sum = sum + i
    return sum/len(my_ints)
