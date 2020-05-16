def next_prime():
    num = 2
    prime_list = []

    while True:
        for n in prime_list:
            if not num % n:
                break
        else:
            prime_list.append(num)
            yield num
        num += num % 2 + 1


primes = next_prime()
print([next(primes) for i in range(100)])

def next_prime_():
    num = 2
    prime_list = []


    while True:
        for el in prime_list:
            if num % el == 0:
                break
        else:
            prime_list.append(num)
            yield num
        num += num % 2 + 1


primes = next_prime_()
print([next(primes) for i in range(100)])