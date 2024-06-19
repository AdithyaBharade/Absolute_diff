#Take a max and min num from the list and find the diff and repeat abd return
n=int(input("Enter the number of elementes: "))
score=list(map(int,input("Enter the element: ").split()))
max_score=0
res=[]
score.sort()
while len(score)>=1:
    max_score=abs(score[0]-score[-1])
    score.pop(0)
    score.pop(-1)
    res.append(max_score)
print(sum(res))
