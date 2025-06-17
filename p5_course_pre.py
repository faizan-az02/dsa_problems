def checkIfPrerequisite(numCourses, prerequisites, queries):

    result = []

    for element in queries:

        if element in prerequisites:

            result.append(True)

        else:

            result.append(False)
    
    return result

if __name__ == "__main__":

    print(checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))