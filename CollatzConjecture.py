import random
from matplotlib import pyplot as plt
from collections import OrderedDict
r=0
x=[]
y=[]
r=random.randint(1,1000)
najveci=r
r1=int(r)
r=int(r)
y.append(r)
print(r)
i=1
x.append(i)
while not r==1:
    if r%2==0:
        r=r/2
    else:
        r=3*r+1
    r=int(r)
    if r>najveci:
        najveci=r
    i=i+1
    y.append(r)
    x.append(i)
    print(r)
fig = plt.figure("Collatz Conjecture")
plt.plot(x,y, marker = 'o', c="teal")
r1=str(r1)
print("First number: ",r1)
print("Biggest number: ",najveci)
string="Collatz Conjecture"
string2="Collatz Conjecture - Start No.: ",r1
#change here ˇˇ to string2 if you want second option!
plt.title(string)
plt.legend(["Number"])
plt.xlabel('Number')
plt.ylabel('Value')
plt.grid()
plt.show()

