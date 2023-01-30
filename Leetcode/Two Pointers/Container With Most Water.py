class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = (len(height)-1) * min(height[0], height[len(height)-1])
        s = 0
        e = len(height)-1
        while s < e:
            w = e - s
            h = min(height[s], height[e])
            answer = answer if answer >= w*h else int(w*h)
            if height[s] <= height[e]:
                s += 1
            else:
                e -= 1
        return answer