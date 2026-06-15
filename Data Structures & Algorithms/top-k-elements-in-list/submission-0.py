class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        count = 0
        for num in nums:
            if num in dic:
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1
        sorted_numbers = sorted(dic.keys(), key=dic.get, reverse=True)
        return sorted_numbers[:k]