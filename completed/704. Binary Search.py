class Solution:
    def search(self, nums: list[int], target: int) -> int:
        print(nums)
        return self.binarySearch(nums, 0, len(nums)-1, target)
        
    def binarySearch(self, nums: list[int], start: int, end: int, target: int) -> int:
        if start > end: return -1
        mid = (end + start) // 2
        print(mid, nums[mid], target)
        if nums[mid] == target: return mid
        if nums[mid] < target: return self.binarySearch(nums, mid + 1, end, target)
        if nums[mid] > target: return self.binarySearch(nums, start, mid - 1, target)

if __name__ == '__main__':
    S = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    nums = [-1,0,3,5,9,12]
    target = 9
    print(S.search(nums, target))