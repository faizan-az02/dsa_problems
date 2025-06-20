def calculateSum(num):

    sum = 0

    while num > 0:

        sum += num % 10

        num //= 10

    return sum

def countLargestGroup(n):

    groups = {}
    result = {}

    for i in range(1, n + 1):

        s = calculateSum(i)

        if s not in groups:

            groups[s] = [i]

        else:

            groups[s].append(i)

    keys = list(groups.keys())

    for key in keys:

        if len(groups[key]) not in result:

            result[len(groups[key])] = 1

        else:

            result[len(groups[key])] += 1

    max_count = max(result.keys())

    return result[max_count]

if __name__ == "__main__":

    n = 2

    result = countLargestGroup(n) # Expected output: 2

    print(result)