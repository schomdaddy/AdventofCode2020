nums = []
for x in open("input.txt"):
    num = int(x.strip())
    nums.append(num)
for x in range(0,len(nums)):
    for y in range(x + 1, len(nums)):
        for z in range(y + 1, len(nums)):
            if nums[x] + nums[y] + nums[z] == 2020:
                print(nums[x] * nums[y] * nums[z])


