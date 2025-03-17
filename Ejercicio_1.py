import matplotlib.pyplot as plt
from timeit import default_timer as timer

def logarithms(n):
    i = 1
    while i <= n:
        i = i * 2
        print(i) 


n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
times = []


for n in n_values:
    start = timer()
    logarithms(n)
    end = timer()
    proc_time = end - start
    times.append(proc_time)
    print(f"Processing time for n={n} -> {proc_time:.8f} seconds")


plt.plot(n_values, times, marker='o', linestyle='-', color='b', label='Tiempo promedio de ejecución')
plt.xscale('log')
plt.yscale('linear') 
plt.xlabel('Tamaño de entrada n')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de procesamiento vs Tamaño de entrada n')
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
