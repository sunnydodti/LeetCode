class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        ans = "0" * len(nums[0])

        if ans not in nums:
            return ans

        def get_inverse(number: int) -> str:
            if number:
                return "0"
            return "1"

        lst = list(ans)

        for i in range(len(ans)):
            new = get_inverse(int(ans[i]))
            lst[i] = new
            new_ans = "".join(lst)
            if new_ans not in nums:
                return new_ans

        return ans

    def findDifferentBinaryString2(self, nums: list[str]) -> str:
        def get_inverse(number: str) -> str:
            number = int(number)
            if number:
                return "0"
            return "1"

        ans = ""

        for i in range(len(nums)):
            print(nums[i])
            print("\t", i,  nums[i][i])
            ans += get_inverse(nums[i][i])
            print(ans)
        return ans


if __name__ == "__main__":
    s = Solution()
    inp = ["01", "10"]
    inp = ["111", "011", "001"]
    print(s.findDifferentBinaryString(inp))
    print("*"*20)
    print(s.findDifferentBinaryString2(inp))
