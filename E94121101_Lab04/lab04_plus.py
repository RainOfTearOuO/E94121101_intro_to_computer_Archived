nums=[]

print("輸入的list為:",end='')
s=input("輸入的list為:") #input with bracket ex.[1,2,3,5,7]
nums=list(s[1:len(s)-1].split(',')) #change 'str' to 'list'
nums=[int(i) for i in nums] #let elements be integer

print(nums,', 要刪除的數字是:',sep='',end='')
val=int(input("要刪除的數字是:"))
print(val)

while val in nums:
    nums.remove(val)

print()
print("刪除後!")
print()
print('list的長度剩下:',end='')
print(len(nums),end=', ')
print("list變成:",end='')
print(nums)