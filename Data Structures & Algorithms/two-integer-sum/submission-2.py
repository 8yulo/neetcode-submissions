class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - nums[i]

            # Find if complement of nums[i] is seen
            if complement in seen:
                return[seen[complement], i]

            # Adds complement if not already seen
            seen[num] = i

        return []