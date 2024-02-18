s = input()

nums = s.split()
l = len(nums)
for i in range(l):
    print('+' * int(nums[i]))