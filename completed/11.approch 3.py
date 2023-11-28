class Solution:
    def maxArea(self, height: list[int]) -> int:
        print(height)
        max_water = 0
        start = 0
        end = len(height)-1
        while start < end:
            print(f'{max_water} - {start}:{height[start]} - {end}:{height[end]}')
            if max_water < min(height[end], height[start]) * (end-start):
                max_water = min(height[end], height[start]) * (end-start)
                
            if height[start] < height[end]:
                start += 1
                print('start: ', start-1, start)
            else:
                end -= 1
                print('end: ', end+1, end)
        return max_water


if __name__ == "__main__":
    S = Solution()
    inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    inp = [1, 2, 1]
    inp = [1, 1]
    inp = [2, 3, 10, 5, 7, 8, 9]
    inp = [1, 2, 4, 3]
    inp = [2, 3, 4, 5, 18, 17, 6]

    print(S.maxArea(inp))
