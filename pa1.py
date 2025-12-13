import numpy as np
import math

def is_prime_wilson(n):
    if n <= 1:
        return False
    return (math.factorial(n-1) + 1) % n == 0
 
# arccot(x) definition
def arccot(x):
    return np.pi/2 - np.arctan(x)

# function f(x)
def f(x):
   
    val = (arccot(-1*x) - np.pi/2) / np.pi
    
    if(val+abs(val)>0):
        return 1
    else:
        return 0
    

def count_primes_wilson(x):
    if x == 1:
        return 1
    count = 0
    for n in range(2, x+1):
        if is_prime_wilson(n):
            count += 1
    
    return count

def calc_x(x, n):
    
    return n+1 - count_primes_wilson(x)


def nth_prime(n):
    # upper bound approximation
    upper = n * (math.log(n) + math.log(math.log(n)))

    ans = 0
    for i in range(1, int(upper) + 1):
        
        x = calc_x(i, n-1)
        
        ans += f(x)
        
        

    return 1+ans

# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    n = int(input("Enter n: "))
    result = nth_prime(n)
    print(f"The computed value for nth_prime({n}) is: {result}")

# Run main when executed
if __name__ == "__main__":
    main()
