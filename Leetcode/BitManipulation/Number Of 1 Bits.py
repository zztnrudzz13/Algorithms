class Solution:
    def hammingWeight(self, n: int) -> int:
        dic = {'1': 0}
        tmp = bin(n)[2:]
        for i in tmp:
            if i == "1":
                dic[i] += 1

        return dic["1"]