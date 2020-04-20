k=2-(1/8)
x0=0
N=1000 #iteraciones
n = N/100
n=int(n)
x=[0,0,0,0,0,0,0,0,0,0]#matrix para numeros alteatorios
s=[0,0,0,0,0,0,0,0,0,0]#matrix de ceros
x[1] = x0;
i=2
for i in range(n):
    if x[i-1]<0:
        x[i]=k*x[i-1]+1;
    else:
        x[i]=k*x[i-1]-1;
    s[i]= (x[i] >= 0);

print("Numeros alteatorios generados:")        
print(x)
