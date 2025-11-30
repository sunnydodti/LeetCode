class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u' ]
        vowels = {'a', 'e', 'i', 'o', 'u' }
        
        count = 0
        
        for i in s[0:k]:
            if i in vowels:
                count += 1
        
        ans =  count

        for i in range(1, len(s) - k + 1):
            count
            print('count:', count)
            # print(s[i:i+k], end = '\t')
            
            print(s[i-1], ':', end='')
            if s[i-1] in vowels:
                count -= 1
            print(count, end='\t')

            print(s[i+k-1], ':', end='')
            if s[i+k-1] in vowels:
                count += 1
            print(count, end='\t = ')
            
            print(count)
            ans = max(ans, count)

        return ans

if __name__ == '__main__':
    S = Solution()
    s = 'abciiidef'
    k = 3
    
    s = "weallloveyou"
    k = 7
    print(S.maxVowels(s, k))