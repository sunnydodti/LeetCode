class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        bits = list(bin(n)[2:])
        print(bits)
        count = 0
        for i in range(len(bits)-1):
            print(i, bits[i], bits)
            if bits[i] == "1":
                print(f"\t{i+1} {bits[i+1]}")
                if bits[i+1] == "1" and "1" not in bits[i+2:]:
                    count += 1
                    bits[i] = "0"

        return count

    def minimumOneBitOperations_o_1(self, n: int) -> int:
        print(bin(n)[2:])
        res = 0
        while n:
            print(res)
            print(f"\t{-res} - ({n}^({n-1})) = {-res - (n ^ (n-1))}")
            res = -res - (n ^ (n - 1))
            print(f"\t{n} &= {n} - 1 :", n & n-1)
            n &= n - 1

        return abs(res)


if __name__ == "__main__":
    S = Solution()
    inp = 3
    # print(S.minimumOneBitOperations(inp))
    print(S.minimumOneBitOperations_o_1(inp))
