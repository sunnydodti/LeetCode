class Solution:
    def arraySign(self, nums: list[int]) -> int:
        count = 0

        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                count += 1
        
        if count %2 == 0:
            return 1
        return -1
    
    def arraySign2(self, nums: list[int]) -> int: 
        ans = 0        
        for num in nums:
            if num == 0: return 0
            if num < 0: ans = -ans
        return ans

if __name__ == "__main__":
    S = Solution()
    inp = [-1,-2,-3,-4,3,2,1]                               #1
    # inp = [1,5,0,2,-3]                                    #2
    # inp = [-1,1,-1,1,-1]                                  #3
    inp = [9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24]  #4
    inp = [-5]                                              #5
    inp = [-1,-2,-3,-4,3,2,1]                               #9

    print(S.arraySign(inp))