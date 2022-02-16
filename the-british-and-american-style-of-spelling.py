n=int(input())
w=[]
for i in range(0,n):
    w.extend(input().split(" "))
t=int(input())
case=[]
for i in range(0,t):
    case.extend(input().split(" "))

count=[0]*len(case)
for i in range(0,len(w)):
    #print("i=",i)
    for j in range(0,t):
        #print("j=",j)
        if(w[i][:-2]==case[j][:-2]):
            count[j]+=1

for i in range(0,len(count)):
    print(count[i])
