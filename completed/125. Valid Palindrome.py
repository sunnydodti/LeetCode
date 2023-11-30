class Solution:
    def isPalindrome(self, s: str) -> bool:
        """accepted"""
        i = 0
        j = len(s) - 1
        print(len(s))
        valid_alphabets = "abcdefghijklmnopqrstuvwxyz1234567890"

        while j > i:
            l = s[i].lower()
            if l not in valid_alphabets:
                i += 1
                continue
            r = s[j].lower()
            if r not in valid_alphabets:
                j -= 1
                continue
            print(i, j, l, r,
                  l == r)
            if l != r:
                return False
            i += 1
            j -= 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        """accepted"""
        i = 0
        j = len(s) - 1
        print(len(s))

        while j > i:
            l = s[i].lower()
            if not l.isalnum():
                i += 1
                continue
            r = s[j].lower()
            if not r.isalnum():
                j -= 1
                continue
            print(i, j, l, r,
                  l == r)
            if l != r:
                return False
            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    S = Solution()
    inp = "amanaplanacanalpanama"
    inp = " "
    inp = " a"
    inp = "0a"
    inp = "A man, a plan, a canal: Panama"  # should be converted to :
    print(S.isPalindrome(inp))
