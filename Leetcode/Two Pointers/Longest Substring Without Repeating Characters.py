class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 1
        start = 0
        end = 1
        dic = {}
        if len(s) == 0:
            return 0
        dic[s[start]] = start

        while end < len(s):
            if s[end] in dic:
                start = dic[s[end]]
                end = dic[s[end]] + 1
                dic = {}
                dic[s[end]] = end
                answer = max(answer, len(dic))
                compare = len(dic)
            dic[s[end]] = end
            end += 1

            answer = max(answer, len(dic))
            if end == len(s):
                break

        return answer