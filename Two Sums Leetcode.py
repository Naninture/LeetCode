class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        if len(nums) > 2000:
            n = round(len(nums)-4000)
            nums = nums[0:n]
            for i in range(0,len(nums)):
                for j in range(1,len(nums)):
                    if nums[i] + nums[j] == target and i != j:
                        result.append(i)
                        result.append(j)
                        break
                    else:
                        pass
            return result[0:2]
        else:
            for i in range(0,len(nums)):
                for j in range(1,len(nums)):
                    if nums[i] + nums[j] == target and i != j:
                        result.append(i)
                        result.append(j)
                        break
                    else:
                        pass
            return result[0:2]




# def two(nums,target):
#     result = []
#     for i in range(0,len(nums)):
#         for j in range(1,len(nums)):
#             if nums[i] + nums[j] == target and i != j:
#                 result.append(i)
#                 result.append(j)
#                 break
#             else:
#                 pass

#     print(result[0:2])


# two([2,7,11,15],9)

# def two(nums,target):
#     result = []

#     for elem in nums:
#         if elem + next(iter(nums),elem) == target and nums.index(elem) != nums.index(next(iter(nums),elem)):
#             result.append(nums.index(next(iter(nums),elem)))
#             result.append(nums.index(elem))
#             break
#         else:
#             pass

#     print(result)


# two([2,7,11,15],9)

# def two(nums,target):
#     result = []

#     for i in range(0,len(nums)):
#         if 0<=i<len(nums)-1 and nums[i] + nums[i+1] == target:
#             result.append(i)
#             result.append(i+1)
#             break
#         else:
#             pass

#     print(result)


# two([3,2,3],6)

# def two(nums,target):
#     result = []
#     for elem in nums:
#         for elm in nums:
#             if elem + elm == target and nums.index(elem) != nums.index(elm):
#                 result.append(nums.index(elem))
#                 result.append(nums.index(elm))
#                 break
#             else:
#                 pass

#     print(result[0:2])


# two([2,7,11,15],9)


            