'''

Exponent calculator from scratch

'''

def taylor_ln(x: float) -> float:

    # Computes natural log of x.

    pass

def taylor_exp(x: float) -> float:

    # Computes e^(x).

    pass

def integer_exp(a: float, b: int) -> float:

    # Computes a^b for all b belongs to integers.

    result = a #* result
    base = 1.00

    is_b_neg = (b < 0)
    
    if is_b_neg:
        b -= 2*b #* Get positive b

    while (b > 1):

        if b%2 == 1:
            base *= result
            b -= 1
        
        result *= result
        b /= 2
    
    result *= base

    if is_b_neg:
        result = 1/result
    
    return result

print("\n",integer_exp(5,5))
print("\n",integer_exp(7,5))
print("\n",integer_exp(1224,12))
print("\n",integer_exp(11,16))
print("\n",integer_exp(8,2))
print("\n",integer_exp(2,12))