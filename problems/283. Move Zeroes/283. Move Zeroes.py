class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
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
    nums = [0, 1, 0, 3, 12]
    print(S.moveZeroes(nums))
