from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in both strings
        mag_count = Counter(magazine)
        note_count = Counter(ransomNote)
        
        # Verify magazine has enough characters to build the ransom note
        for char, count in note_count.items():
            if mag_count[char] < count:
                return False
                
        return True