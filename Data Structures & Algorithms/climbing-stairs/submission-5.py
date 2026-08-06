class Solution:
    def climbStairs(self, n: int) -> int:
        i=0
        first_variable = 0
        second_variable = 0
        third_variable  = 1
        while i <= n:
            first_variable = third_variable
            print(first_variable)
            print(second_variable)
            third_variable = first_variable + second_variable
            second_variable = first_variable
            print(third_variable)
            i+=1
        return first_variable