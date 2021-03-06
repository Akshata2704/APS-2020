
# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    

    for _ in range(n - 1):
        previous, current = current%10, (previous + current)%10
        

    return current % 10

p=input()
n1=int(p)
print(get_fibonacci_last_digit_naive(n1))
