from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)

        l, r = 0, 0

        while r < len(s2):
            print(l, r, s2[l], s2[r])
            if s2[l] not in count:
                l += 1
                r += 1
            else:
                if s2[r] not in count:
                    l = r + 1
                    r = l + 1
                elif s2[r] in count:
                    arr = Counter(s2[l:r + 1])
                    if arr == count:
                        return True
                    else:
                        for key in arr:
                            if arr[key] > count[key]:
                                l += 1
                                continue
                        r += 1

        return False