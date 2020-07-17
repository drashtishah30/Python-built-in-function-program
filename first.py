nums = list()
while True:
    inp = input('Enter no:')
    if inp == 'done':break
    value = float(inp)
    nums.append(value)
    average = sum(nums)/len(nums)
print('Average:--',average)
