class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Finished_nums = []
        char = []
        answer = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key, val in counts.items():
            char.append(key)
            Finished_nums.append(val)
            
        char_no = dict(zip(char, Finished_nums))
        sorted_keys = sorted(char_no, key=char_no.get, reverse=True)
        
        l = 0
        while l < k:
            get_maximum_key = sorted_keys[l]
            answer.append(get_maximum_key)
            l += 1
            
        return answer
