"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError

    list = []
    index = 2
    while len(list) < number_of_primes:
        if prime_separator(index) == True:
            list.append(index)
        index += 1

    return list

def prime_separator(value):
    if (value == 2) or (value == 3) or (value == 5) or (value == 7):
        return True
    elif value % 2 == 0:
        return False
    elif value % 3 == 0:
        return False
    elif value % 5 == 0:
        return False
    elif value % 7 == 0:
        return False
    
    else:
        return True
