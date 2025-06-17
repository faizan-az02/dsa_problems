def firstCompleteIndex(arr, mat):
        
        temp_list = []

        for e in range(len(arr)):

            temp_list.append(arr[e])

            if e < len(mat) - 1:

                pass

            else:

                for i in range(len(mat)):

                        if all(mat[i][j] in temp_list for j in range(len(mat))):
                            
                            return e

                for i in range(len(mat)):

                        if all(mat[j][i] in temp_list for j in range(len(mat))):
                            
                            return e
                         
        return -1    
                
if __name__ == "__main__":

    arr = [1, 3, 2, 4]
    mat = [[1, 2], [3, 4]]
    print(firstCompleteIndex(arr, mat)) # Output: 1 