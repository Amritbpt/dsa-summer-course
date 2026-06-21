def is_prime(x):
    for i in range(2, x // 2 + 1, 1):
        if x % i == 0:
            return False        
    return True
            
print(f"is 11 a prime {is_prime(11)}")   