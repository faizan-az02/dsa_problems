def countPairs(nums, k):

    count = 0

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if (nums[i] == nums[j]) and ((i * j) % k == 0):

                count += 1

    return count

if __name__ == "__main__":
    # Example usage
    nums = [3,1,2,2,2,1,3]

    k = 2

    result = countPairs(nums, k)

    print(result)  # Expected output: 4