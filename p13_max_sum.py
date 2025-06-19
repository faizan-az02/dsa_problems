def maximumSum(nums):

    def calculateSum(num):

        total = 0

        while num > 0:

            total += num % 10

            num //= 10

        return total

    max_sum = 0

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            
            if calculateSum(nums[i]) == calculateSum(nums[j]):

                if nums[i] + nums[j] > max_sum:

                    max_sum = nums[i] + nums[j]

    if max_sum > 0:

        return max_sum
    
    else:

        return -1

if __name__ == "__main__":
    # Example usage
    nums = [18,43,36,13,7]
    
    result = maximumSum(nums)

    print(result)  # Expected output: 54