dict0={}

for i in range (0,4):
    print("Enter Keys: ",end='')
    key=input("Enter Keys:")
    print(key)
    
    print("Enter Values: ",end='')
    val=input("Enter Values:")
    print(val)
    
    val=list(val.split(','))
    
    dict0[key]=val

print(dict0)