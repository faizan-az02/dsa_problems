def check(nums):

    def is_sorted_either(lst):

        return lst == sorted(lst) or lst == sorted(lst, reverse=True)


    for i in range(len(nums)):

        rotated = nums[i:] + nums[:i]

        if is_sorted_either(rotated):

            return True
        
    return False

# Example usage:
if __name__ == "__main__":
    
    nums = [3, 4, 5, 1, 2]
    print(check(nums))  # Output: True

    nums = [2, 1, 3, 4]
    print(check(nums))  # Output: False