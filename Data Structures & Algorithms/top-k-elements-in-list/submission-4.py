class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        k_freq = freq.most_common(k)

        return [val for val, val_id in k_freq]


        