class Solution:
    def maxArea(self, height: list[int]) -> int:
        print(height)
        max_water = 0
        start = 0
        end = 0
        for i in range(1, len(height)):
            print(
                f'{max_water} - {start}:{height[start]}, {i}:{height[i]} - {min(height[start], height[i])} * {i-start} = {min(height[start], height[i]) * (i-start)}')
            if max_water < min(height[start], height[i]) * (i-start):

                print(
                    f'\t {min(height[start], height[i]) * (i-start)} > { max_water}')
                max_water = min(height[start], height[i]) * (i-start)
                print('\t-- set max_water as', max_water)

                print(
                    f'\t- {height[start]} & {height[i]} - {height[start] < height[i]}')

                if height[start] < height[i]:
                    end = start
                    start = i
                else:
                    end = i

                print('\t-- set start as', start)
                print('\t-- set end as', end)

            elif max_water < min(height[end], height[i]) * (i-end):
                print(
                    f'\t {min(height[end], height[i]) * (i-end)} > { max_water}')
                max_water = min(height[end], height[i]) * (i-end)
                print('\t-- set max_water as', max_water)

                print(
                    f'\t- {height[end]} & {height[i]} - {height[end] < height[i]}')

                if height[end] > height[i]:
                    start = end
                    end = i
                else:
                    start = i

        return max_water


if __name__ == "__main__":
    S = Solution()
    # inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # inp = [1, 2, 1]
    # inp = [1, 1]
    # inp = [2, 3, 10, 5, 7, 8, 9]
    inp = [1, 2, 4, 3]

    print(S.maxArea(inp))
