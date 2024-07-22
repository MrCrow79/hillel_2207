def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


def find_primes(n: int) -> list:
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
