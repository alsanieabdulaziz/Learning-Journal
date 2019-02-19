count=0
sum=0
num=[36,256,745,433,56,26,123,65,98,235,88]
for i in num:
    count=count+1
    sum=sum+i
    print("Incremental Sum + Count:",sum, count)

print("Mean:", sum/count)
