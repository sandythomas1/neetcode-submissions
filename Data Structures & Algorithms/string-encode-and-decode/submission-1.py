class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            len_s = len(s)
            sep = '#'
            new = str(len_s) + sep + s
            res.append(new)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        dec_res = []
        i = 0 

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            string = s[j+1 : j + 1 + length]
            dec_res.append(string)
            i = j + 1 + length

        return dec_res
