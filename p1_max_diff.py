def maximumDifference(nums):
        
        diff = -1

        n = len(nums)

        for i in range(n):

            for j in range(n):

                if i >= j:

                    pass
                
                else:

                    if nums[i] < nums[j]:

                        temp = nums[j] - nums[i]

                        if diff < temp:

                            diff = temp
        
        return diff

# Example usage:
if __name__ == "__main__":
    nums = [7, 1, 5, 4]
    print(maximumDifference(nums))  # Output: 4
    nums = [9, 4, 3, 2]
    print(maximumDifference(nums))  # Output: -1
    nums = [1, 2, 3, 4]
    print(maximumDifference(nums))  # Output: 3
    nums = [1, 2, 3, 0]
    print(maximumDifference(nums))  # Output: 2