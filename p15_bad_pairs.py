def countBadPairs(nums):

    res = 0

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if j - i != nums[j] - nums[i]:
                
                res += 1

    return res




if __name__ == "__main__":
    # Example usage
    nums = [4,1,3,3]
    
    result = countBadPairs(nums)

    print(result)  # Expected output: 0