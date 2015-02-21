class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        i = 0
        maxArea = 0
        while i < len(height):
            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                h = height[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
        return maxArea
