from typing import List

nums = [2, 7, 10, 3]
target = 9

class two_sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return[num_to_index[complement], index]
            num_to_index[num] = index


solver = two_sum()

result = solver.twoSum(nums, target)

print(result)
