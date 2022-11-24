def squares(n):

    num = 1

    while num <= n:

        # yield num * num
        yield num ** 2

        num += 1

print(list(squares(5)))