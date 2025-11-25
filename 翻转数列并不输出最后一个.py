nums = list(map(int, input().split()))
reversed_nums = nums[::-1]
for i in range(1,len(reversed_nums) ):
    print(reversed_nums[i], end=" ")