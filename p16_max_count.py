def maximumCount(nums):

    pos_count = 0
    neg_count = 0

    for num in nums:

        if num > 0:

            pos_count += 1

        elif num < 0:

            neg_count += 1

    return max(pos_count, neg_count)

if __name__ == "__main__":
    # Example usage
    nums = [-2, -1, 0, 1, 2]

    result = maximumCount(nums)

    print(result)  # Expected output: 2