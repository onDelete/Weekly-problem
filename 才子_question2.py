def last(x, step):
    nums = []
    if x <= 0 or step <= 1:return 'params error'
    
    temp_step = step - 1
    
    for i in range(x):
        nums.append(i+1)

    while len(nums) > 1:
        if temp_step - len(nums) >=0:
            temp_step = temp_step - len(nums)
        else:
            nums.pop(temp_step)
            temp_step += step -1
    return nums[0]
