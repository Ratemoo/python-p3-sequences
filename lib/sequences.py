#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        print('[]')
        return
    
    fibonacci_sequence = []
    a, b = 0, 1
    while length > 0:
        fibonacci_sequence.append(a)
        a, b = b, a + b
        length -= 1
    
    print(fibonacci_sequence)
