#Original Solution, not using heap [Easy to solve but painful to implement as I had no clue about what exactly is k, nums or val]
#thought that nums was the input list, and we had to create the variables k and val from nums

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums   

    def add(self, val: int) -> int:
      #appending val(integer) to nums(list)
      #sortings nums in reverse
      #finding the kth largest element (using k - 1 as index starts from 0)
        self.nums.append(val)
        self.nums.sort(reverse = True)
        return self.nums[self.k - 1]
