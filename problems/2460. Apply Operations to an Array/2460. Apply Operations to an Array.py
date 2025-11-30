class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        non_zore_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zore_index] = nums[i]
                non_zore_index += 1

        for i in range(non_zore_index, len(nums)):
            nums[i] = 0

        return nums


if __name__ == "__main__":
    S = Solution()
    nums = [1, 2, 2, 1, 1, 0]
    print(S.applyOperations(nums))
