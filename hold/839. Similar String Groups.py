class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int: # does not work
        l = len(strs[0])
        ans = []
        for i in range(1, len(strs)):
            word = strs[i-1]
            count = 0
            for j in range(l):
                if word[j] != strs[i][j]:
                    count += 1

            print(word, strs[i], count)
            if count not in ans:
                ans.append(count)

        return len(ans) 

    def numSimilarGroups2(self, strs: list[str]) -> int: # does not work

        for i in range(1, len(strs)):
            prev = set(strs[i-1])
            cur = set(strs[i])

            diff = prev.intersection(cur)

            print(prev, cur, len(diff))
            

if __name__ == "__main__":
    S = Solution()
    inp = ["tars","rats","arts","star"]

    print(S.numSimilarGroups2(inp))
