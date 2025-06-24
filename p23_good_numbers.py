def countGoodNumbers(n):

    for i, d in enumerate(str(n)):

        if i in  [0, 2, 4, 6, 8]:

            if d not in "02468":

                return False
            
        elif i in [1, 3, 5, 7, 9]:

            if d not in "2357":

                return False
    return True

if __name__ == "__main__":

    print(countGoodNumbers(3245))  # Output: False