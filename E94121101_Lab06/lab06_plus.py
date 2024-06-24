used=list()
str=input("input a number series")
ans=list()
tmp=""

for i in range(len(str)): #initialize used list
    used.append(0)
    tmp=""
#codes above are initialization
def func(used,ans,tmp,str):
    if(len(tmp)==len(str)):
        ans.append(tmp)
        tmp=""
    
    for i in range(len(str)):
        if(used[i]==1):
            continue
        else:
            used[i]=1
            tmp+=str[i]
            func(used,ans,tmp,str)
            tmp=tmp[:len(tmp)-1]+""
            used[i]=0
#codes above are func definition
func(used,ans,tmp,str)
print(ans)
