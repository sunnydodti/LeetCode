class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum = 0
        average = float('-inf')

        for i in range(len(nums) - k+1):
            sum = 0
            for j in range(i, k+i):
                sum += nums[j]
            average = max(sum/k, average)

        return average
    
    def findMaxAverageBruteForce(self, nums: list[int], k: int) -> float:
        sum = 0
        average = float('-inf')

        for i in range(len(nums) - k+1):
            sum = 0
            for j in range(i, k+i):
                sum += nums[j]
            average = max(sum/k, average)

        return average

    def findMaxAverageSlidingSum(self, nums: list[int], k: int) -> float:
        sum = 0
        average = float('-inf')

        for i in range(k):
            sum += nums[i]
        average = max(sum/k, average)
        
        for i in range(k, len(nums)):
            sum -= nums[i-k]
            sum += nums[i]
            average = max(sum/k, average)
        return average

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    # nums = [5]
    # k = 1

    # nums = [0,1,1,3,3]
    # k = 4

    # nums = [-1]
    # k = 1
    # print(solution.findMaxAverage(nums, k))
    print(solution.findMaxAverageV2(nums, k))
