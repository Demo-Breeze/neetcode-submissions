class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        total = []
        for i in words:
            b = 0
            while b<len(words):
                if words[b] in i:
                    total.append(words[b])
                    print(words[b])
                b+=1
        final = []
        for i in total:
            if total.count(i)>1:
                final.append(i)
        return list(set(final))