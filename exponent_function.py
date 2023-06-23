# An exponent function is going to take a certain number and raise it to a power

print(2**3) # the same as 2^3

def raise_to_power(base_num, pow_num):
    result = 1

    # this will loop as many times as pow_num
    # the base_num will multiply by itself as many times as pow_num
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))