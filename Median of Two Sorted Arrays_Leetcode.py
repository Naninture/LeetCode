
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        

        m = len(nums1)
        n = len(nums2)
        div = m+n
        N = nums1 + nums2
        N = sorted(N)
        # print(sum(iter(N)))
        # result = float(sum(iter(N))/div)

        # v = '{:.5f}'.format(result)
        # print(type(v))
        # print(float(format(result,'.5f')))
        
        # print('{:.5f}'.format(result))
        if div%2==0 :
            result = (N[int(div/2)] + N[int((div/2-1))])/2
            print(float(result))
        else:
            result = N[int(div/2)]
            
            print(float(result))


t = Solution()
t.findMedianSortedArrays([1,2],[3,4])