import matplotlib.pyplot as plt

T=[]
alfa=[]
beta=[]
N=   100      #int(input('Введите кол-во простр-х узлов N = '))
t_end=  10    #int(input('Введите окончание повремени t_end = '))
L= 16          #float(input('Введите толщину пластины L = '))
lamb= 46       #int(input('Введите коээф-т теплоп-ти материла пластины lamb = '))
ro=  4800         #int(input('Введите плотность материала пластины ro = '))
c=  460          #int(input('Введите теплоёмкость материала пластины c = '))
TO= 20          #int(input('Введите начальную температуру T0 = '))
Tl= 30          #int(input('Введите температуру на границе x=0 T1 = '))
Tr= 40         #int(input('Введите температуру на границе x=L Tr = '))
for i in range(1,N+1):
    T.append(0)
    alfa.append(0)
    beta.append(0)
h=L/(N-1)
tau=t_end/100
for i in range(1,N):
    T[i]=TO
    time=0
while time<t_end:
    time=time+tau
    alfa.append(0)
    beta.append(Tl)
    for i in range(2,N-1):
        ai=lamb/(h**(1/2))
        bi=2*lamb/(h**(1/2))+ro*c/tau
        ci=lamb/(h**(1/2))
        fi=-ro*c*T[i]/tau
        alfa[i]=ai/(bi-ci*alfa[i-1])
        beta[i]=(ci*beta[i-1]-fi)/(bi-ci*alfa[i-1])
    T[N-1]=Tr
    for i in range(N-2,2,-1):
        T[i]=alfa[i]*T[i+1]+beta[i]
        
print('\nРезультаты')
print('Толщина пластины L = ', L)
print('Число узлов по координате N = ', N)
print('Коэ-т тепло-ти материла пластины lamb = ', lamb)
print('Плотность материала пластины ro = ', ro)
print('Теплоёмкость материала пластины c = ', c)
print('Начальная температура TO = ', TO)
print('Температура на границе  x = 0: ', Tl)
print('Температура на границе x = L: ', Tr)
print('Шаг по координате h = ', h)
print('Шаг по времени tau', tau)
print('Температура поля с момента времени t = ', t_end)

sp=[]
for i in range(1,N-1):
    sp.append(h*(i-1))
    sp.append('-')
    sp.append(T[i])
    #print(h*(i-1),'     ', T[i])

# plt.plot(T, sp)
# plt.show()
print('Длина T = ', len(T), 'длина sp = ', len(sp))

xt = []

for i in range(294):
    xt.append(i)

plt.plot(xt, sp)
plt.show()