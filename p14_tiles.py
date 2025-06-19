def numTilePossibilities(tiles: str) -> int:

    def backtrack(path, used):

        for i in range(len(tiles)):

            if used[i]:

                continue

            if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:

                continue

            used[i] = True

            result.add(''.join(path + [tiles[i]]))

            backtrack(path + [tiles[i]], used)

            used[i] = False

    tiles = sorted(tiles)

    result = set()

    backtrack([], [False] * len(tiles))
    
    return len(result)


if __name__ == "__main__":
    tiles = "AAB"
    print(numTilePossibilities(tiles))  # Output: 8
    tiles = "AAABBC"
    print(numTilePossibilities(tiles))  # Output: 188
    tiles = "V"
    print(numTilePossibilities(tiles))  # Output: 1