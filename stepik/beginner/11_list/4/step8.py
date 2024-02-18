n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)

for i in range(n):
    if nums[i] < 0:
        print(nums[i])

for i in range(n):
    if nums[i] == 0:
        print(nums[i])

for i in range(n):
    if nums[i] > 0:
        print(nums[i])