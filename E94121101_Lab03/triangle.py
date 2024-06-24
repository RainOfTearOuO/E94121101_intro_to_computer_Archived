side=[0,0,0]
side[0]=int(input("請輸入第一個邊長"))
side[1]=int(input("請輸入第二個邊長"))
side[2]=int(input("請輸入第三個邊長"))
side.sort()

if not(side[0]+side[1]>side[2]):
    print("這三個邊長不能構成一個合法的三角形")
elif (side[0]==side[1]==side[2]):
    print("這是一個正三角形")
elif ((side[0]==side[1]) or (side[1]==side[2])):
    print("這是一個等腰三角形")
else:
    print("這是一個一般三角形")
