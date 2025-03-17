import matplotlib.pyplot as plt
from timeit import default_timer as timer

def nested_loop(n):
    for i in range(n):
        for j in range(n):
            #print(f"i = {i} y j = {j}")
            pass 

n_values = [100, 400, 600, 800, 1000, 1100]
times = []

print("\n{:<10} {:<15}".format("n", "Tiempo (s)"))
print("=" * 26)

for n in n_values:
    start = timer()
    nested_loop(n)
    end = timer()

    proc_time = end - start
    times.append(proc_time)

    print(f"{n:<10} {proc_time:.10f}")

plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker='o', linestyle='-', color='r', label='Tiempo de ejecución')
plt.xscale('log') 
plt.xlabel('Tamaño de entrada n')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de procesamiento vs Tamaño de entrada n (Bucle anidado)')
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
