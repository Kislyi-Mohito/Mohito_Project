T = []
alfa = []
beta = []
N =  100        #       int(input("Введите колво простр-х узлов N = "))
t_end = 100       # int(input("Введите ограничение по времени t_end = "))
L =   16      #       float(input("Введте толщину пластины L = "))
lamb = 46       # int(input("ВВедите коэфицент теплоемкости материала пластины lamb = "))
ro =   7800   #       int(input("ВВедите плоность материала пластины ro = "))
c =     460#       int(input("Введите теплоемкость материала пластины с = "))
TO =   0 #       int(input("ВВедите начальную температу T0 = "))
Ti =    0 #       int(input('Введите температуру на границе x = 0, Ti = '))
Tr =   1     #       int(input('Введите температуру на грнице x=L, Tr = '))

for i in range(1, N - 1):
    T.append(0)
    alfa.append(0)
    beta.append(0)
h = L / (N - 1)
tau = t_end / 100

for i in range(1, N):
    T[i] = TO
    time = 0
while time < t_end:
    time = time + tau
    alfa.append(0)
    beta.append(0)
    for i in range(2, N - 1):
        ai = lamb / (h ** (1 / 2))
        bi = 2 * lamb / (h ** (1 / 2) + ro * c / tau)
        ci = lamb / (h ** (1 / 2))
        fi = ro * c * T[i] / tau
        alfa[i] = ai / (bi - ci * alfa[i - 1])
        beta[i] = (ci * beta[i - 1] - fi) / (bi - ci * alfa[i - 1])
    T[N - 1] = Tr

    for i in range(N - 2, 2, -1):
        T[i] = alfa[i] * T[i + 1] + beta[i]

print('\nРезультаты')
print("Толщина пластины L = ", L)
print("Число узлов по  координате N = ", N)
print("Коэфициент теплоемкости материала пластины lamb = ", lamb)
print("Плотность материала пластины ro = ", ro)
print("Теплоемкость материала пластины c = ", c)
print("Начальная температура T0 = ", TO)
print("Температура на границе x = 0: ", Ti)
print("Температура на границе x = L: ", Tr)
print("Шаг по координате h = ", h)
print("Шаг по координате tau = ", tau)
print("Температура поля с момента времени t = ", t_end)
