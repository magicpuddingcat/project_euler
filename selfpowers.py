"""Find the last 10 digits in thousanth entry in the series of n^n.
    Danielle Rosenfeld-Lovell, August 2019."""

def final_digit_self():

    # Defining max and the sum of the self-power values in the series
    max = 1000
    sum_series = 0

    for num in range (1, max+1):
        sum_series += num**num

    # Convert to string so that the lsat 10 digits can be returned
    string_series = str(sum_series)
    return string_series[-10:]

final_digit_self()