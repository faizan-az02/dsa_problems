def findLucky(arr):

    res_dict = {}

    res = []

    for element in arr:

        if element in res_dict:

            res_dict[element] += 1

        else:

            res_dict[element] = 1

    for element in res_dict:

        if element == res_dict[element]:

            res.append(element)

    if res:

        return max(res)
    
    else:

        return -1

if __name__ == "__main__":

    print(findLucky([2,3,4])) # Expected -1