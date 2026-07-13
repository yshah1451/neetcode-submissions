from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] # Consistently use res instead of output
        q = deque() # Stores indices of elements
        l = r = 0

        while r < len(nums):
            # Pop smaller elements from the back of the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove the front element if it's outside the current window
            if l > q[0]:
                q.popleft()

            # If the window has reached size k, record the maximum
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res # Fixed indentation
