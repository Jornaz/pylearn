n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

mx = max(nums)
mx_index = nums.index(mx)
del nums[mx_index]

mn = min(nums)
mn_index = nums.index(mn)
del nums[mn_index]

print(*nums, sep = '\n')