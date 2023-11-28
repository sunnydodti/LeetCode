class Solution:

    # brute force method
    def brute_force_method(self, s: str) -> str:
        def longestPalindrome(self, s: str) -> str:
            if len(s) == 1:
                return s
            ans = ""
            l = len(s)
            tmp = 0
            for start in range(l):
                for end in range(tmp, l+1):
                    if end >= start:
                        sub_str = s[start:end]
                        if len(sub_str) > len(ans):
                            if isPalindrome(sub_str):
                                ans = sub_str
                            print(start, end, end=" : ")
                            print(sub_str)
                tmp += 1

            return ans

        def isPalindrome(s: str):
            if s == s[::-1]:
                return True
            return False
        x = 0

        return longestPalindrome(self, s)


    def expand_arround_center_method(self, s: str) -> str:
        def longestPalindrome(self, s: str) -> str:
            start, end = 0, 0
            for i in range(len(s)):
                oddLength = expandArroundCenter(s, i, i)
                evenlength = expandArroundCenter(s, i, i + 1)

                palindromeLen = max(oddLength, evenlength)

                if palindromeLen > (end - start + 1):
                    start = i - (palindromeLen-1)//2
                    end = i + palindromeLen//2

            return s[start:end+1]

        def expandArroundCenter(s: str, left: int, right: int) -> int:
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left + 1

        return longestPalindrome(self, s)

if __name__ == "__main__":
    S = Solution()

    inp_string = "dwvvlmokkdtnbrpnueyamqwrvrcwpwiaglvoizmsfuxzgvkvsexgwxwoygayznjlswucmoehugrkjkduwtdrguaqtqwdvrekxgphbitvxmpazkceodsyjzuvjfvgjbtiawrpcwomeiwgoelilfylydsdgawybjjmbgfhkndnvqdryncglaxmzndsoziqqmrwticjomsyatisjduifwfzjkgpdpneurlylzgrdlixhosmmwhaqgpxhmjqxsasfnqnppyufxwpukaruvlnfetymzqwzfklpwdwwrupvrttxdkgjbrzwuvwkkjiynnoemfzrjaepvejvxqkvhqtegtiwtbwlneqzryjzzjyrzqenlwbtwitgetqhvkqxvjevpeajrzfmeonnyijkkwvuwzrbjgkdxttrvpurwwdwplkfzwqzmytefnlvurakupwxfuyppnqnfsasxqjmhxpgqahwmmsohxildrgzlylruenpdpgkjzfwfiudjsitaysmojcitwrmqqizosdnzmxalgcnyrdqvndnkhfgbmjjbywagdsdylyflileogwiemowcprwaitbjgvfjvuzjysdoeckzapmxvtibhpgxkervdwqtqaugrdtwudkjkrguheomcuwsljnzyagyowxwgxesvkvgzxufsmziovlgaiwpwcrvrwqmayeunprbntdkkomlvvwd"
    # print("ans: ", S.longestPalindrome(inp_string))

    x = "dwvvlmokkdtnbrpnueyamqwrvrcwpwiaglvoizmsfuxzgvkvsexgwxwoygayznjlswucmoehugrkjkduwtdrguaqtqwdvrekxgphbitvxmpazkceodsyjzuvjfvgjbtiawrpcwomeiwgoelilfylydsdgawybjjmbgfhkndnvqdryncglaxmzndsoziqqmrwticjomsyatisjduifwfzjkgpdpneurlylzgrdlixhosmmwhaqgpxhmjqxsasfnqnppyufxwpukaruvlnfetymzqwzfklpwdwwrupvrttxdkgjbrzwuvwkkjiynnoemfzrjaepvejvxqkvhqtegtiwtbwlneqzryjzzjyrzqenlwbtwitgetqhvkqxvjevpeajrzfmeonnyijkkwvuwzrbjgkdxttrvpurwwdwplkfzwqzmytefnlvurakupwxfuyppnqnfsasxqjmhxpgqahwmmsohxildrgzlylruenpdpgkjzfwfiudjsitaysmojcitwrmqqizosdnzmxalgcnyrdqvndnkhfgbmjjbywagdsdylyflileogwiemowcprwaitbjgvfjvuzjysdoeckzapmxvtibhpgxkervdwqtqaugrdtwudkjkrguheomcuwsljnzyagyowxwgxesvkvgzxufsmziovlgaiwpwcrvrwqmayeunprbntdkkomlvvwd"
    y = "babad"
    
    # print(S.brute_force_method(x))
    print(S.expand_arround_center_method(x))
