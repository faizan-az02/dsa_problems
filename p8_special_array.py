def isArraySpecial(nums):

    for i in range(len(nums) - 1):

        e1 = (nums[i] % 2)

        e2 = (nums[i + 1] % 2)

        if e1 == e2:

            return False

    return True

# Example usage:
if __name__ == "__main__":

    nums = [2, 1, 4]

    print(isArraySpecial(nums))  # Output: True

        