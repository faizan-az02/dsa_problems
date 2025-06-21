import random

def findDifferentBinaryString(nums):

    num = ""

    length = len(nums[0])

    for i in range(length):

        char = random.choice(["0", "1"])

        num += char

    if num in nums:

        return findDifferentBinaryString(nums)
    
    else:

        return num

if __name__ == "__main__":

    nums = ["111","011","001"]

    print(findDifferentBinaryString(nums))