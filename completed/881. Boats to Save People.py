class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        if len(people) == 1:
            return 1

        people.sort()
        print(people)

        count = 0
        i, j = 0, len(people) - 1

        while i <= j:
            print(people[i], people[j])
            sum = people[j] + people[i]

            if sum > limit:
                print('sent', people[j])
                count += 1
                j -= 1
                continue

            if sum <= limit:
                print('sent', people[i], people[j])
                count += 1
                i += 1
                j -= 1
                continue

            print('-- sent', people[i], people[j])
            count += 1
            i += 1
            j -= 1

        return count


if __name__ == "__main__":
    S = Solution()
    print(S.numRescueBoats([3, 2, 2, 1], 3))
