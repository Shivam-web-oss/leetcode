class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):
            # Avoid duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Pruning/Optimization
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break  # Smallest possible sum for this i is greater than target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue # Largest possible sum for this i is less than target

            for j in range(i + 1, n - 2):
                # Avoid duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Pruning/Optimization
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                # Two-pointer approach for the remaining two numbers
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Skip duplicate elements for left and right
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans