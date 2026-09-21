from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for string in strs:
            freq_array = [0] * 26 

            for char in string:
                mapping = ord(char) - ord('a')
                freq_array[mapping] += 1

            key = tuple(freq_array)
            group[key].append(string)

        return list(group.values())


            