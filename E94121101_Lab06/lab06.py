def gcd(a,b): #This is just a "print func", the real func to do gcd is "ff"
    if(a==0 or b==0):
        print("0沒有gcd")
    elif(ff(a,b)==1):
        print(a,"和",b,"互質")
    else:
        print(a,"和",b,"的gcd=",ff(a,b))

def ff(a,b): #This is where the true gcd function is defined.
    if(b==0):
        return a
    return ff(b,a%b)
    
ans1 = gcd(80,10) #ans1, ans2, ans3 are "NoneType", 
ans2 = gcd(10,0)
ans3 = gcd(19,20)
