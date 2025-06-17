def firstCompleteIndex(arr, mat):
        
        found = 1

        for e in range(len(arr)):

            print(e)

            if e < len(mat) - 1:

                pass

            else:

                temp_list = []

                for k in range(e + 1):

                    temp_list.append(arr[k])

                print(temp_list)

                for i in range(len(mat)):

                    found = 1

                    for j in range(len(mat)):

                        print(f"Checking element {mat[i][j]} in temp_list")

                        if mat[i][j] not in temp_list:

                            found = 0

                            break

                    if found:

                        return e

                for i in range(len(mat)):

                    found = 1

                    for j in range(len(mat)):

                        print(f"Checking element {mat[j][i]} in temp_list")

                        if mat[j][i] not in temp_list:

                            found = 0

                            break

                    if found:
                    
                        return e
                
        return -1    
                
if __name__ == "__main__":

    arr = [1, 3, 2, 4]
    mat = [[1, 2], [3, 4]]
    print(firstCompleteIndex(arr, mat)) # Output: 1

