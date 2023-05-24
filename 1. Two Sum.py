#Original Solution, slow and memory inefficient
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #Creating 2 loops, one looping over the range of the length of list
      #The second looping on every other element after the current iterable
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                #Then looking up the index of the two elements and checking whether their sum is equal to target
                if nums[i] + nums[j] == target:
                    return ([i, j]


#single line solution, same logic
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [[i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target][0]
                            
#easier to understand version of a solution by GANJINAVEEN, much faster but ok in memory efficiency:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
                            
        #Adding index and element of list as key and value pair to dictionary
        for i,n in enumerate(nums):
            #Checking whether the value(element of num) is in dictionary
            if n not in dict:
                #If not, then adding its complement to the dictionary  (Complement is any number, that if added to
                #another number results in target number [2 is complement of 7 as adding 2 to 7 results in Target number (9)])
                dict[target-n]=i
            else:
                #If n is in dictionary (Is a complement of any previous iterated element),
                #return the index number of the complement number in dictionary, and the index of the current element
                return dict[n],i
