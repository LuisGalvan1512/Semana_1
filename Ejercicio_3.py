import matplotlib.pyplot as plt
from timeit import default_timer as timer

def loop_with_print(n):
    for i in range(n):
        #print(f"I = {i}")
        pass

n_values = [1, 10, 100, 1000, 10000, 100000]
times = []

print("\n{:<10} {:<15}".format("n", "Tiempo (s)"))
print("=" * 26)

for n in n_values:
    start = timer()
    loop_with_print(n)
    end = timer()

    proc_time = end - start
    times.append(proc_time)

    print(f"{n:<10} {proc_time:.10f}")

plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='b', label='Tiempo de ejecución')
plt.xscale('log') 
plt.xlabel('Tamaño de entrada n')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de procesamiento vs Tamaño de entrada n (Bucle con print)')
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
