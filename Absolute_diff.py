'''You are given an array A of size N. In one operation you can select any two elements 
from it, add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input1: An integer value N, representing the size of array A
input2: An integer array A
Output Specification:
Return an integer value, representing the maximum score.
Sample Input:
4
1 2 3 4 
Sample Output: 4
'''


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