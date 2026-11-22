def duplicate():
    nums=list(map(int,input("enters numbers: ").split()))
    repeat=set()
    for i in nums:
        if i in repeat:
            return True
        repeat.add(i)
    return False
print(duplicate())