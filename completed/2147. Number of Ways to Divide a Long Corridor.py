class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """failed"""
        seats = 0
        plants = 0
        ways = 0
        seat_count = 0
        for char in corridor:
            print(char)
            if char == "S":
                seats += 1
                seat_count += 1
            if char == "P" and seats == 0:
                plants += 1
                continue
            print(f"\ts: {seats}, : {plants}")

            if seats == 2:
                if seat_count == 2:
                    seats = 0
                    plants = 0
                    continue
                seats = 0
                ways += (plants+1)
                plants = 0
            print(f"\tw: {ways}")
            # if seats == 1:
        if ways == 0 and seat_count >= 2:
            ways = 1
        mod = 10000000007
        return ways % mod

    def numberOfWays2(self, corridor: str) -> int:
        """works"""
        seats = 0
        plants = 0
        ways = []
        seat_count = 0
        for char in corridor:
            print(char)
            if char == "S":
                seats += 1
                seat_count += 1
            if char == "P" and seats == 0:
                plants += 1
                print(f"\tp: {plants}")
                continue
            print(f"\ts: {seats}, p: {plants}")

            if seats == 2:
                ways.append(plants+1)
                seats = 0
                plants = 0

            # if seats == 2:
            #     if seat_count == 2:
            #         seats = 0
            #         plants = 0
            #         continue
            #     seats = 0
            #     ways += (plants+1)
            #     plants = 0
            print(f"\tw: {ways}")
            # if seats == 1:

        if seat_count % 2 != 0:
            return 0

        ways = ways[1:]
        print(ways)
        if not ways:
            if seat_count == 2:
                return 1
            return 0

        result = 1
        for way in ways:
            result *= way

        mod = 1000000007
        return result % mod

    def numberOfWays3(self, corridor: str) -> int:
        """works"""

        print(corridor)
        seats = 0
        # last_pair_index = 0
        ways = []
        index = 0
        i, j = 0, 0
        for char in corridor:
            index += 1
            print("seats: ", seats)
            if char == "S":
                seats += 1
                print("\ts at: ", index, "seats: ", seats)
            if char != "S":
                continue
            if seats == 2:
                i = index
                print("\t", "i", i)
            if seats == 3:
                j = index
                print("\t", "j", j)
                # ways *= (x)
            if seats == 4:
                print("\t", f"{j} - {i} = {j-i}")
                ways.append(j-i)
                seats = 2
                i = index
                print("\t", "i", i)
                print("\t", ways)
        print(corridor)
        print(ways)
        if seats < 2:
            return 0
        if seats % 2 != 0:
            return 0
        mod = 1000000007
        result = 1
        for way in ways:
            print(way)
            print(f"{result} * {way} = {result * way} - ")
            result *= way

        return result % mod
    
    def numberOfWays_r_1(self, corridor: str) -> int:
        MOD = 1_000_000_007

        zero = 0
        one = 0
        two = 1

        for thing in corridor:
            if thing == "S":
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % MOD

        return zero

if __name__ == "__main__":
    S = Solution()
    inp = "SSPPSPS"
    inp = "PPSPSP"
    inp = "S"
    inp = "SSPPSPSPSS"  # own
    inp = "SPPSSSSPPS"
    inp = "PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"
    # inp = "p"
    # print(S.numberOfWays(inp))
    # print(S.numberOfWays2(inp))
    # print(S.numberOfWays3(inp))
    print(S.numberOfWays_r_1(inp))
