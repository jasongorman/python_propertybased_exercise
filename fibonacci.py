def fibonacci(index):
    minus_one = 0
    minus_two = 0
    fib = 0

    for i in range(index + 1):
        if i < 2:
            fib = i
        else:
            fib = minus_one + minus_two

        minus_two = minus_one
        minus_one = fib

    return fib
