class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to hold the number as key and its index as value
        num_dict = {}
        
        # Iterate through the array of numbers
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            x = target - num
            
            # If the complement is already in our dictionary, return the solution
            if x in num_dict:
                return [num_dict[x], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

        # According to the problem statement, there's always exactly one solution,
        # so we don't need a return statement outside the loop