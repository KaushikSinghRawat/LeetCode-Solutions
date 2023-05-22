class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        #creating for loop for individually checking the sum of wealth of each account
        #if wealth is greater than the current max_wealth, then changing value of max_wealth to be equal to the new sum
        for i in accounts:
            if sum(i) > max_wealth:
                max_wealth = sum(i)
        return max_wealth
      
      
      #one line solution using generator, same logic as above
      return max(sum(i) for i in accounts)
      
      #another one line solution inspired from other solutions submitted
      return (max(map(sum, accounts))
              
      #
