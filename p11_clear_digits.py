def clearDigits(s):

    stack = []

    for ch in s:

        if ch.isdigit():

            i = len(stack) - 1

            while i >= 0 and stack[i].isdigit():

                i -= 1

            if i >= 0:

                stack.pop(i)

        else:

            stack.append(ch)
            
    return ''.join(stack)

if __name__ == '__main__':
    print(clearDigits("abc"))                 # Expected: "abc"
    print(clearDigits("a1b2c3"))              # Expected: ""
    print(clearDigits("1abc"))                # Expected: "abc"
    print(clearDigits("no digits"))           # Expected: "no digits"
    print(clearDigits("123"))                 # Expected: ""
    print(clearDigits("a1b2"))                # Expected: ""
    print(clearDigits("abc1"))                # Expected: "bc"
