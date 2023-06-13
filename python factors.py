import sys

def factorize_number(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append((i, n // i))
            n //= i
    if n > 1:
        factors.append((n, 1))
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            n = int(line)
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
