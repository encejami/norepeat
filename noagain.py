e=("wwwooooorlllddddddffffffj")
x=e+"x"
y=[]

for i in range(len(x)):
    if i==len(x)-1:
        break
    elif x[i]==x[i+1]:
            pass
    elif x[i]!=x[i+1]:
            y.append(x[i])
print(''.join(y))