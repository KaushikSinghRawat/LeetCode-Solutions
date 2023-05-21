#simplified variation of a clever solution provided by lostworld21
#solution
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        competitive_subsequence = []
      
        for  i in range(len_nums):
            #if element of nums is less than the last digit of subsequence and
            #there are enough unprocessed elements in nums to fill the subsequence to the length stated in k
            #then remove the last element of the subsequence
            while competitive_subsequence and nums[i] < competitive_subsequence[-1] and len(competitive_subsequence) + len_nums - i > k:
                competitive_subsequence.pop()
                
            #if the length of subsequence is less than k, append the element to subsequence
            if competitive_subsequence < k:
                competitive_subsequence.append(nums[i])
                
        return (competitive_subsequence)
   

            
