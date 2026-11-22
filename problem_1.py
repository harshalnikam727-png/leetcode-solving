def sum():
    nums=[2,7,11,15]
    target=9
    seen={}
    for i,num in enumerate(nums):
        needed=target-num
        if needed in seen:
            return [seen[needed],i]
        else:
            seen[num]=i
print(sum())