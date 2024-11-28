'''num=14
ans=0
pos=1
while num!=0:
    rem=num%2
    ans=ans+(rem*pos)
    pos=pos*10
    num//=2
print(ans)
'''
num=10110
ans=0
power=0
while num!=0:
    rem=num%10
    ans=ans + (rem * 2**(power))
    power+=1
    num//=10
print(ans)

num =10110
res=0
pos=1
while num!=0:
    rem=num%10
    res=res+rem(pos*=2)
    num//=10
    print (res)
    
