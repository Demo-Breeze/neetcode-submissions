from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        num_words = len(words)
        char_counts = Counter("".join(words))
        return all(count % num_words == 0 for count in char_counts.values())
