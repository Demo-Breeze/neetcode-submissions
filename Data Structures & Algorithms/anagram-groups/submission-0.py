from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            l = "".join(sorted(word))
            anagram_groups[l].append(word)
        result = list(anagram_groups.values())
        return result