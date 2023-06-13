import sys
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (pow(x, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    return d

def factorize_number(n):
    factors = []
    while n > 1:
        if is_prime(n):
            factors.append((n, 1))
            break
        factor = pollard_rho(n)
        exponent = 0
        while n % factor == 0:
            n //= factor
            exponent += 1
        factors.append((factor, exponent))
    return factors

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(10):  # Number of Miller-Rabin tests
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        n = int(file.read())
        factor_pairs = factorize_number(n)
        for pair in factor_pairs:
            p, q = pair
            print(f"{n} = {p} * {q}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    file_path = sys.argv[1]
    factorize_file(file_path)
