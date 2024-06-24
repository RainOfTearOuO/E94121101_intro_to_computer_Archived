list=[['A'],['B'],['C']] #2-dimensional list

for i in range(0,3):
    print("輸入",chr(ord('A')+i),"學生成績",sep="")
    print("國文:")
    list[i].append(int(input()))
    print("數學:")
    list[i].append(int(input()))
    print("英文:")
    list[i].append(int(input()))
    
    list[i].append((list[i][1]+list[i][2]+list[i][3])/3) #Average

for i in range(0,3):
    print(list[i])