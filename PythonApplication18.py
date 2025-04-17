print("Task 1: Filtering Numbers")
multiples_of_3_not_5 = [number 
                        for number in range(1, 101) 
                        if number % 3 == 0 and number % 5 != 0]
print(multiples_of_3_not_5)
print("Task 2: Temperature Conversion")
celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)
print("Task 3: Squares of Even numbers")
squares_of_even = [number**2 
                   for number in range(1, 51) 
                   if number % 2 == 0]
print(squares_of_even)
print("Task 4: Text Analysis")
text = "Python is amazing and powerful language"
word_lengths = [len(word) 
                for word in text.split()]
print(word_lengths)
print("Task 5: Composite numbers")
def has_more_than_two_divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return len(divisors) > 2

composite_numbers = [number 
                     for number in range(1, 101) 
                     if has_more_than_two_divisors(number)]
print(composite_numbers)