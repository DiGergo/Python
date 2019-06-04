def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    evens = 0
        
    for i in numbers:
        if is_even(i):
            evens += 1
            
    if evens == 0:
        return False
    else:
        return is_even(evens)
        
assert even_number_of_evens ([]) == False, ("NO numbers")
assert even_number_of_evens([2]) == False, ("One even number")
assert even_number_of_evens([2, 4]) == True, ("two even numbers")
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, ("Multiple numbers, three even")
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 12]) == True, ("Multiple numbers, four even")
assert even_number_of_evens([ 3, 9, 13, 7,]) == False, ("NO even numbers")

print ("All test are passed!")