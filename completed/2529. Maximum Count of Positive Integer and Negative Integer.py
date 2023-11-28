class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        nCount, pCount = 0, 0
        l = len(nums)
        start, end = 0, l - 1
        print(nums)


        while start <= end:
            print(nCount, pCount)
            mid = (end + start) // 2
            print(f'{start}-{mid}-{end} : {nums[start]} | {nums[mid]} | {nums[end]}', end=' - ')
            
            if nums[mid] < 0:
                print('less')
                start = mid + 1
                nCount = mid + 1
                continue
            
            if nums[mid] > 0:
                print('more')
                end = mid - 1
                pCount = l - mid
                continue
            
            print('zero')
            if nCount > pCount:
                end = mid - 1 
                continue

            if pCount > nCount:
                start = mid + 1
                continue
            
            # end = mid - 1 
            start = mid + 1
                
        print(nCount, pCount)
        return max(nCount, pCount)



if __name__ == '__main__':
    S = Solution()
    inp = [-2,-1,-1,1,2,3]
    inp = [-3,-2,-1,0,0,1,2]
    print(S.maximumCount(inp))