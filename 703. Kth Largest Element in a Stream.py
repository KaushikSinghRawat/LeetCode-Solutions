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

#Solution using heap, inspired by the solution by yourick
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums
        #converting the list nums to a heap
        #elements are automatically ascendingly ordered upon converting to heap
        heapq.heapify(self.nums)
        #using headpop to pop the first element of the heap while length of heap is larger than k
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)    

    def add(self, val: int) -> int:
        #appending/adding val(integer) to the heap
        heapq.heappush(self.nums, val)
        #using headpop to pop the first element of the heap while length of heap is larger than k
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        #returning the first element of the heap (Which is the kth largest element in the heap)
        return self.nums[0]
