#Original Solution, slow and memory inefficient
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #Creating 2 loops, one looping over the range of the length of list
      #The second looping on every other element after the current iterable
      #Then looking up the index of the two elements and checking whether their sum is equal to target
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i, j]


#single line solution, same logic
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [[i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target][0]
