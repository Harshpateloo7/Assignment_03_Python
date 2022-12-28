def sieve_of_eratosthenes(nums):
    primes = []
    multiples = []

    for num in range(2, nums+1):
        if num not in multiples:
            primes.append(num)
            for multiple in range(num*num, nums+1, num):
                multiples.append(multiple)
    return primes

def get_user_input():
    user_input = int(input('Enter integer number between 0-100: '))
    return user_input

def main():
    user_input = get_user_input()
    print(sieve_of_eratosthenes(user_input))

if __name__ == '__main__':
    main()