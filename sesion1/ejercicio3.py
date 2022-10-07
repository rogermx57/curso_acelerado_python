horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
extras = float(input("Introduce horas extras: "))
salario=horas * coste
paga_extra = extras * coste
paga=salario + paga_extra
print("Tu paga es", paga)