"""Determine the first number in a Fibonacci sequence to contain 100 digits.
    The method is fairly crude and will end up requiring a reworking as I get a bit more confident.
    Danielle Rosenfeld-Lovell, August 2019."""

# As an interim measure have found first number in sequence to contain 100 digits
def find_hundred_digits():

    # First define my two variables which will propagate the sequence
    n1 = 1
    n2 = 1

    # Make the conditional be that the length of most recent number in sequence is less than 1000
    while (len(str(n2)) < 100):
        # update numbers to progress in the Fibonacci sequence
        temp_num = n1 + n2
        n1 = n2
        n2 = temp_num

    print(n2)
    return n2

find_hundred_digits()