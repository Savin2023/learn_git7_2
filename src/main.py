import modules.sko_calc as calc
import numpy.random as random

a=random.random_integers(1,100,25)
print("Массив:",a)
print("\nСтандартное отклонение(NumPy):", calc.sko1(a))
print("\nСтандартное отклонение(Pandas):", calc.sko2(a))
