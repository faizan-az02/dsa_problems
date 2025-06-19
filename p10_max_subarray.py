def maxAscendingSum(nums):

    sum = 0

    for i in range(len(nums)):

        if i > 0 and nums[i] >= nums[i - 1]:
            
            sum += nums[i]

        else:

            sum = nums[i]

    return sum

if __name__ == "__main__":

    # Example usage

    nums = [10, 20, 30, 5, 10, 50]

    result = maxAscendingSum(nums)

    print(result)  # Output: 65