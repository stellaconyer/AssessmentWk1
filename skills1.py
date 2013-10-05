# Things you should be able to do.
my_ints = [5, 4, 2, 25]
my_list = ["one", "two", "four", "or", "more"] 


# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = []    
    for i in some_list:
        if i % 2 == 1:
            new_list.append(i)
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []
    for i in some_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.


def long_words(word_list):
    new_list = []
    for i in word_list:
        if len(i) >= 4:    
            new_list.append(i)
    return new_list


# Write a function that finds the smallest element in a list of integers and returns it


def smallest(some_list):
    smalls = some_list[0]
    for i in some_list:
        if i < smalls:
            smalls =  i
    return smalls    


def bubble_sort(some_list):
    bubble_range = len(some_list)-1  
    while bubble_range != 0: 
        for i in range(bubble_range):
            print bubble_range, some_list[i], some_list[i + 1]  
            if some_list[i] > some_list[i + 1]:
                some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
        bubble_range = bubble_range - 1
             
    return some_list

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    large = some_list[0]
    for i in some_list:
        if i > large:
            large =  i
    return large   


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for i in some_list:
        new_list.append(i/2)
    return new_list


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    new_list = []
    for word in word_list:
        new_list.append(len(word))
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum_of_nums = 0
    for i in numbers:
        sum_of_nums += i
    return sum_of_nums



# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mult_num = 1
    for i in numbers:
        mult_num = mult_num*i
    return mult_num

   

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    string = ""
    for i in string_list:
        string = string+i
    return string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
