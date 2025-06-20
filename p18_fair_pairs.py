def countFairPairs(nums, lower, upper):

    nums.sort()

    count = 0

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if lower <= nums[i] + nums[j] <= upper:

                count += 1

    return count

if __name__ == "__main__":
    # Example usage

    nums = [0,1,7,4,4,5]

    lower = 3

    upper = 6

    result = countFairPairs(nums, lower, upper)

    print(result)  # Expected output: 6