while 1:
    no = int(input("NO: "))
    pi = 0
    for i in range(10**no):
        pi += 2*10**no/((4*i+1)*(4*i+3))
    print("3." + str(round(4*pi))[1::])
