#Solution 1
#My original solution, slow but ok in memory efficiency
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_3 = {}
        
        #updating the nums_3 dict with the elements of the given list as keys and values as 0
        for i in set(nums):
            nums_3.update({i:0})
        
        #updating the values in nums_3 with how frequently the keys occur in the given list
        for i in nums:
            nums_3[i] += 1
        
        result = []
        
        #creating a loop to find the number of values required for the solution (represented by k)  
        #finding the higest value in the list using max function
        #appending the key having the highest value to result
        #deleting the element having the higest value
        for i in range(k):
            max_value_dict = max(zip(nums_3.values(), nums_3.keys()))
            result.append(max_value_dict[1])
            del(nums_3[max_value_dict[1]])
        
        return result
