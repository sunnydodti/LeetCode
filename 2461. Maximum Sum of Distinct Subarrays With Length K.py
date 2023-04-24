class Solution:
    # def maximumSubarraySum(self, nums: list[int], k: int) -> int:
    #     max_sum = 0
    #     for i in range(len(nums) - k + 1):
    #         print(i)
    #         if self.isvalid_subarray(nums[i:int(i+k)], k):
    #             sub_sum = sum(nums[i:int(i+k)])
    #             if sub_sum > max_sum:
    #                 max_sum = sub_sum

    #     return max_sum

    # def isvalid_subarray(self, arr: list[int], k: int) -> bool:
    #     print(arr, end=' -> ')
    #     if len(arr) != k:
    #         print('False')
    #         return False

    #     checked = []
    #     for i in arr:
    #         if i in checked:
    #             print('False')
    #             return False
    #         checked.append(i)
    #     print('True')
    # return True

    def tmp(self, nums: list[int], k: int) -> bool:
        max = 0
        for l in range(len(nums) - k + 1):
            new_sum = 0
            r = l+k
            # print(l, r, nums[l:r])

            if max:
                new_sum = max
                print(f'\t {nums[l-1]}, {nums[r-1]}')
                new_sum -= nums[l-1]
                new_sum += nums[r-1]
            else:
                print(f'\t {nums[l]}, {nums[r]}')
                new_sum = sum(nums[l:r])
                max = new_sum

            print(nums[l:r], new_sum)

        return True


if __name__ == "__main__":
    S = Solution()
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3

    # print(S.maximumSubarraySum(nums, k))
    print(S.tmp(nums, k))
