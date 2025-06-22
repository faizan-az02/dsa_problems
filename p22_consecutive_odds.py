def threeConsecutiveOdds(arr):

    count = 0

    for n in arr:

        if n % 2 == 1:

            count += 1

            if count == 3:

                return True
        else:
            count = 0

    return False

if __name__ == "__main__":
    print(threeConsecutiveOdds([2, 6, 4, 1, 3, 5]))  # Output: True
    print(threeConsecutiveOdds([1, 2, 34, 3, 5]))    # Output: False
    print(threeConsecutiveOdds([1, 3, 5, 7]))         # Output: True
    print(threeConsecutiveOdds([2, 4, 6]))             # Output: False
    print(threeConsecutiveOdds([]))                    # Output: False