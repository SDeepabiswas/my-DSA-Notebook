from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for string in strs:
            sorted_key = ''.join(sorted(string))
            anagram_groups[sorted_key].append(string)

        return list(anagram_groups.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]