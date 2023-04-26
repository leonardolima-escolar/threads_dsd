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




def multiplicaLinhaPorColuna(start, end):
    for i in range(start, end):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
                print(threading.current_thread().name,
                      matriz3[i][j], '+=', matriz1[i][k], '*', matriz2[k][j])




threads = list()




quantasThread = 2




linhasMatriz = len(matriz3)


for i in range(quantasThread):
    start = i * (linhasMatriz/quantasThread)
    end = (i + 1) * (linhasMatriz/quantasThread)
    th = threading.Thread(target=multiplicaLinhaPorColuna,
                          args=(int(start), int(end),), name="Thread "+str(i))
    th.start()
    threads.append(th)


for t in threads:
    t.join()


print(matriz3)
