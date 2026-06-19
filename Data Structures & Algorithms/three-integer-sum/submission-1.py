class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Reset pointers inside the loop for each new 'i'
            j = i + 1
            k = n - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])  # Fixed syntax & storing values
                    
                    # Move pointers forward to avoid infinite loop
                    j += 1
                    k -= 1
                
                    while j < k and nums[j] == nums[j - 1]:
                            j += 1
                    while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                        
                elif current_sum < 0:
                    j += 1  # Sum is too small, make it bigger by moving right
                else:
                    k -= 1  # Sum is too big, make it smaller by moving left
                        
        return res
                