dict0={"index":["國文","英文","數學","自然","社會"], "StuA":[50,60,70,80,90], "StuB":[57, 86, 73, 82, 43], "StuC":[97, 96, 86, 97, 83]}
print(dict0)

print("A學生平均成績：",sum(dict0["StuA"])/len(dict0["StuA"]))
print("B學生平均成績：",sum(dict0["StuB"])/len(dict0["StuB"]))
print("C學生平均成績：",sum(dict0["StuC"])/len(dict0["StuC"]))
print()

for i in range(0,5):
    print(dict0["index"][i]+"平均成績：",(dict0["StuA"][i]+dict0["StuB"][i]+dict0["StuC"][i])/3)