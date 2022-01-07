import time
for j in range(100):
    pi = 0
    t = time.time()
    for i in range(10**j):
        pi += 2*10**j/((4*i+1)*(4*i+3))
    print("3." + str(round(4*pi))[1::] + f"\ntime taken: {round(time.time() - t)} sec; DIGITS: {j}\n\n")
