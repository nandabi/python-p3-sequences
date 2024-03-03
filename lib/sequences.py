#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print("[]")
    else:
        fibonacci_sequence = [0, 1] if length > 1 else [0]
        while len(fibonacci_sequence) < length:
            next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fibonacci)
        print(f"[{', '.join(map(str, fibonacci_sequence))}]")       