from collections import Counter
def firstUniqChar(s: str) -> int:
        cnt = Counter(s)

        for i in range( len(s) ):
            if cnt[s[i]] == 1:
                return i
        return -1

if __name__ == "__main__":
    s = "leetcode"
    print(firstUniqChar(s))  # Output: 0

    s = "loveleetcode"
    print(firstUniqChar(s))  # Output: 2

    s = "aabb"
    print(firstUniqChar(s))  # Output: -1