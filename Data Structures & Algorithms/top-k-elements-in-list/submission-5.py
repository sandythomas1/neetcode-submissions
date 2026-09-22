class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}

        for num in nums:
            if num not in freq_count:
                freq_count[num] = 1 
            else:
                freq_count[num] += 1

        freq_pairs = []
        for num in freq_count:
            freq_pairs.append((freq_count[num], num))

        freq_pairs.sort(reverse=True)

        result = []
        index = 0
        while k > 0:
            result.append(freq_pairs[index][1])
            index += 1
            k -= 1
        return result 

        