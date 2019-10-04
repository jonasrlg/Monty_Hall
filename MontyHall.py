import random

def play(doors, nd, ng):
    choice = random.randrange(nd)
    del(doors[choice]) # Deleting the first guess
    for g in range (ng):
        for i, door in enumerate(doors):
            if door == 0:
                del(doors[i]) # Deleting doors with goats
                break
    if (doors[random.randrange(len(doors))] == 1):
        return 1
    return 0

def simulation(N, nd, ng):
    change, stay = 0, 0
    for i in range (N):
        doors = [0]*nd
        doors[random.randrange(nd)] = 1
        stay += doors[random.randrange(nd)]
        change += play(doors, nd, ng)
    return change, stay

def sampling(N):
    nd = int(input("The number of doors is: "))
    while (nd < 2):
        nd = int(input("Please, type a number >= 2: "))
    ng = int(input("The number of goats is: "))
    while (ng < 0 or ng > nd-2):
        ng = int(input(f"Please, type a number >= 0 and <= {nd-2}: "))
    print("May the games begin!")
    change, stay = simulation(N,nd,ng)
    print("Changing wins = ",change,"/ Probability of winning = ",change/N)
    print("Staying wins = ",stay,"/ Probability of winning = ",stay/N)

def graphic(N, list):
    probC = []
    probS = []
    for i in range(len(list)):
        probC.append(list[i][0]/N)
        probS.append(list[i][1]/N)
    # plotar gráfico de portas versus probabilidade

def graphic(N, a, b, bool):
    list = []
    j = 1
    for i in range(a,b+1):
        change, stay = simulation(N,i,j)
        list.append([change,stay])
        if (bool):
            j += 1
    graphic(N,list)

def main():
    mode = input("Choose a mode, sampling (s) or graphic (g): ")
    while (mode != "s" and mode != "g"):
        mode = input("Type 's' or 'g'")
    N = int(input("The number of simulations is: "))
    while (N < 0):
        N = int(input("Please, type a number >= 1: "))

    if (mode == "g"):
        a, b = int(input("Type the interval of doors: "))
        while (a < 3 or a > b):
            a,b = int(input("Please, type an interval [a,b], with a >= 3 and b >= a: "))
        g = input("Type (o) for one goat in all simulations and (n) for n-1 goats: ")
        while (g != "o" and g != "n"):
            g = input("Type 'o' or 'n'")
        bool = False
        if (g == "n"):
            bool = True
        graphicN(N,a,b,bool)

    else:
        sampling(N)

main()
