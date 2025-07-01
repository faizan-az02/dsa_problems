def maximumTripletValue(nums):

    n = len(nums)

    res = 0

    val = 0

    for i in range(n - 2):

        for j in range(max(1, i + 1), n - 1):

            for k in range(max(2, j + 1), n):

                val = (nums[i] - nums[j]) * nums[k]

                if val > res:

                    res = val

    return res


if __name__ == "__main__":

    nums = [12,6,1,2,7]

    print(maximumTripletValue(nums)) # Expected Output 77