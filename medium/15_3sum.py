class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting + twosum?

        res = []
        seen = set()

        # sort
        nums.sort()

        # fix i, then perform 2sum on the rest
        for i in range(len(nums)):
            j, k = i+1, len(nums) - 1
            target = 0 - nums[i] # target for twosum

            while j < k:
                if nums[j] + nums[k] == target:
                    curr = (nums[i], nums[j], nums[k])
                    if curr not in seen:
                        seen.add(curr)
                        res.append(list(curr))
                    # need to move both after finding valid triplet
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] <= target:
                    j += 1
                else:
                    k -= 1
        return res
                



