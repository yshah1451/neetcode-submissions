class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores pair: (start_index, height)
        max_area = 0
 
        for i, h in enumerate(heights):
            start = i
 
            # If current height is smaller, previous taller bars cannot continue
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                max_area = max(max_area, height * width)

                # current smaller bar can start from this popped index
                start = index
                
 
            stack.append((start, h))
 
        # Calculate area for remaining bars in stack
        n = len(heights)
        for index, height in stack:
            width = n - index
            max_area = max(max_area, height * width)
 
        return max_area