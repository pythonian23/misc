def sum_product(num: int):
    vals = []
    for n in range(num, 0, -1):
        #   a ,  a , b, c, ... =>    a**2    * ...
        #  a+1, a-1, b, c, ... => (a**2 - 1) * ...
        higher = num % n
        low = num // n
        vals.append((low ** (n - higher)) * ((low + 1) ** higher))
    return max(vals)


for test in range(1, 20):
    print(test, sum_product(test))
