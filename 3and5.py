"""Small program to find the sum of all multiples of 3 and 5.
    Danielle Rosenfeld-Lovell, August 2019"""

def three_and_five():

    # First define the upper limit on multiples and the sum value initialised to 0
    max = 1000
    sum_multiples = 0

    # Then loop over all values less than or equal to 1000 to determine if a multiple
    for num in range(3, max):
        if (num % 3 == 0 or num % 5 == 0):
            sum_multiples+=num
            # Otherwise just keep looping until we reach 1000

    print(sum_multiples)
    return sum_multiples


three_and_five()