#ans
n=int(input())
a=list(map(int,input().split()))
b=[]
x=sum(a)
for i in range(n):
    b.append(x-a[i])
print(*b)



#que
Write a program to replace every element with sum of all other elements

Input Format

Each line contains the array size & values

Constraints

1 ≤ array_size ≤ 10000

Output Format

print the array

Sample Input 0

5
12 34 56 76 87
Sample Output 0

253 231 209 189 178
