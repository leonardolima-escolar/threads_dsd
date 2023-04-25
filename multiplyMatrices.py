import threading

num_linhas = 2
num_colunas = 2

matriz1 = [[None]*num_colunas for _ in range(num_linhas)]
matriz2 = [[None]*num_colunas for _ in range(num_linhas)]
matriz3 = [[None]*num_colunas for _ in range(num_linhas)]


for i in range(num_linhas):
    for j in range(num_colunas):
        matriz1[i][j] = 1
        matriz2[i][j] = 2
        matriz3[i][j] = 0

def multiplicaLinhaPorColuna(i):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
            print(threading.current_thread().name, matriz3[i][j], '+=', matriz1[i][k], '*', matriz2[k][j])

threads = list()

for i in range(len(matriz1)):
    th = threading.Thread(target=multiplicaLinhaPorColuna, args=(i,), name="Thread "+str(i))
    th.start()
    threads.append(th)
        
for t in threads:
    t.join()

print(matriz3)
