#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    print(fib_sequence)

# Example usage:
sequence_length = int(input("Enter the length of Fibonacci sequence: "))
print_fibonacci(sequence_length)
