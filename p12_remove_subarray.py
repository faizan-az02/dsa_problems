def removeOccurrences(s, part):

    while part in s:

        s = s.replace(part, '')

    return s

if __name__ == "__main__":
    s = "daabcbaabcbc"
    part = "abc"
    result = removeOccurrences(s, part)
    print("Final Result:", result)  # Expected: "dab"