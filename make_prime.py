def generate_prime(max):
    """ Program to generate primes to a fixed maximum for use on some of the Project Euler
        tasks. Danielle Rosenfeld-Lovell, July 2019."""
    lst_prime = []

    # select every number up to max and determine whether it is a prime
    for num in range(2, max):
        is_prime = True

        # loop through divisors and then break as soon as there is found to be a factor
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break

    # finish by creating a total list of primes up to specified range
        if is_prime:
            lst_prime.append(num)

    print(lst_prime)
    return lst_prime