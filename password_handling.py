def hashPassword(password):
    hashed = ''
    for i in range(len(password)):
        symbol = ord(password[i])
        symbol += fibonacci(i + 1)**2
        hashed += chr(symbol)
    return hashed

def saltPassword(password):
    endPassword = password
    for i in range(primes(len(password))):
        endPassword += str(chr(i))
    return endPassword

def encryptPassword(password):
    encrypted = password
    for i in range(len(password)):
        encrypted = hashPassword(saltPassword(encrypted))
    return encrypted

def fibonacci(n):
    more = 1
    less = 1
    temp = 0
    if n < 3:
        return 1
    for i in range(n - 2):
        temp = more
        more += less
        less = temp
    return more

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(n):
    primes = []
    number = 2
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes[-1]