class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        len1 = len(word1)
        len2 = len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                ans += word1[i]
            if i < len2:
               ans += word2[i]
    
        return ans

if __name__ == "__main__":
    S = Solution()
    inp1 = 'abc'
    inp2 = 'pqr'
    print(S.mergeAlternately(inp1, inp2))