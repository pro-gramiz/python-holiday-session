#ans
a=list(input())
i=0
while(len(a)-1>i):
    if a[i]==a[i+1]:
        a.remove(a[i+1])
    else:
        i+=1
print(''.join(a))



#que
Given a string, remove a adjacent duplicate charachters from the given string

Input Format

Input contains a string

Output Format

Output contains a string after the adjacency characters are removed.

Sample Input 0

abbacce
Sample Output 0

abace
