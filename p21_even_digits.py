def findNumbers(nums):

    count = 0

    for n in nums:

        if len(str(n)) % 2 == 0:

            count += 1

    return count

if __name__ == "__main__":
    print(findNumbers([12, 345, 2, 6, 7896]))  # Output: 2
    print(findNumbers([555, 901, 482, 1771]))   # Output: 1
    print(findNumbers([1000, 20000, 300000]))   # Output: 2
    print(findNumbers([1, 22, 333, 4444]))      # Output: 2
    print(findNumbers([]))                       # Output: 0