class Solution:
    def hammingWeight(self, n: int) -> int:
        """accepted"""
        # return len(bin(n)[2:].replace("0", ""))
        # or
        return bin(n)[2:].count("1")
    
    def hammingWeight2(self, n: int) -> int:
        """accepted"""
        binary = bin(n)[2:]
        count = 0
        for i in binary.strip("0"):
            if i == "1":
                count += 1
        return count

    def hammingWeight3_kernighans_algorithm(self, n: int) -> int:
        """accepted"""
        count = 0
        while n != 0:
            n &= (n - 1)
            count += 1
        return count

if __name__ == "__main__":
    S = Solution()
    inp = 0
    inp = 4294967293
    print(S.hammingWeight(inp))
    print(S.hammingWeight2(inp))
    print(S.hammingWeight3_kernighans_algorithm(inp))
