from random import randrange
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def play(doors, nd, ngs):
    choice = randrange(nd)
    del(doors[choice]) # Deleting the first guess
    for g in range (ngs):
        for i, door in enumerate(doors):
            if door == 0:
                del(doors[i]) # Deleting the first door with a goat and quiting for
                break

    if (doors[randrange(len(doors))] == 1):
        return 1
    return 0


def simulation(N, nd, ngs):
    change, stay = 0, 0
    for i in range (N):
        doors = [0]*nd
        doors[randrange(nd)] = 1
        stay += doors[randrange(nd)]
        change += play(doors, nd, ngs)
    return change, stay

def probTheorical (nd, ngs):
    return ((nd-1)/(nd*(nd-1-ngs)))

def sampling(N):

    doors = int(input("The number of doors is: "))
    while (doors < 3):
        doors = int(input("Please, type a number >= 3: "))
    goats = int(input("The number of goats is: "))
    while (goats < 0 or goats > doors-1):
        goats = int(input(f"Please, type a number >= 0 and <= {doors-1}: "))
    print("May the games begin!")

    change, stay = simulation(N,nd,ngs)
    pTC, pTS = probTheorical(nd, ngs), 1/nd

    print("\nChanging simulation/theorical probability =",change/N,"/",pTC)
    print("Staying simulation/theorical probability =",stay,"/",pTS,"\n")

    graphic = input("Type 'g' if you want a graph: ")
    if (graphic == "g"):
        label = input("Type 'l' if you want labels: ")
        bl = False
        if (label == "l"):
            bl = True

        l = "Doors = " + str(nd) + " / Goats Shown = " + str(ngs)
        labels = [l]
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, [change/N], width, label='Change')
        rects2 = ax.bar(x + width/2, [stay/N], width, label='Stay')
        rects3 = ax.bar(x - 3*width/2, [pTC], width, label='Theorical Change')
        rects4 = ax.bar(x + 3*width/2, [pTS], width, label='Theorical Stay')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Probability')
        ax.set_title('Theory VS Simluation')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        def autolabel(rects):
            # From matplotlib.org
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        if (bl):
            autolabel(rects1)
            autolabel(rects2)
            autolabel(rects3)
            autolabel(rects4)

        fig.tight_layout()

        plt.show()

def bars(list):
    probC = []
    probS = []
    for i in range(len(list)):
        probC.append(list[i][0])
        probS.append(list[i][1])
    return probC, probS

def barsT(list):
    probC = []
    probS = []
    pTheoricalC = []
    pTheoricalS = []
    for i in range(len(list)):
        probC.append(list[i][0])
        probS.append(list[i][1])
        pTheoricalC.append(list[i][2])
        pTheoricalS.append(list[i][3])
    return probC, probS, pTheoricalC, pTheoricalS

def graphic(list, labels, string, bt, bl):
    if (bt):
        probC, probS, pTheoricalC, pTheoricalS = barsT(list)
    else:
        probC, probS = bars(list)

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, probC, width, label='Change')
    rects2 = ax.bar(x + width/2, probS, width, label='Stay')

    if (bt):
        rects3 = ax.bar(x - width/2, pTheoricalC, width, label='Theorical Change')
        rects4 = ax.bar(x + width/2, pTheoricalS, width, label='Theorical Stay')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Probability')
    ax.set_title(string)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        # From matplotlib.org
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    if (bl):
        autolabel(rects1)
        autolabel(rects2)
        if (bt):
            autolabel(rects3)
            autolabel(rects4)

    fig.tight_layout()

    plt.show()

def Ngoats(N, doors, bt, bl):
    list = []
    labels = []
    for goats in range(doors-1):
        change, stay = simulation(N,doors,goats)
        if (bt):
            list.append([change/N,stay/N,probTheorical(doors,goats),1/doors])
        else:
            list.append([change/N,stay/N])
        labels.append(goats)
    graphic(list, labels, "Probability by number of goats", bt, bl)

def interval(N, a, b, bg, bt, bl):
    list = []
    labels = []
    goats = 1
    if (bg):
        goats += a-3
    for doors in range(a,b+1):
        change, stay = simulation(N,doors,goats)
        if (bt):
            list.append([change/N,stay/N,probTheorical(doors,goats),1/doors])
        else:
            list.append([change/N,stay/N])
        #print("i =",doors,"/ prob = ",change/N)
        if (bg):
            goats += 1
        labels.append(doors)
    graphic(list, labels, "Probability by number of doors", bt, bl)

def main():
    mode = input("Choose a mode, sampling (s) or graphic (g): ")
    while (mode != "s" and mode != "g"):
        mode = input("Type 's' or 'g': ")
    N = int(input("The number of simulations is: "))
    while (N < 0):
        N = int(input("Please, type a number >= 1: "))

    if (mode == "g"):
        theorical = input("If you want to show theorical data type 'Y': ")
        bt = False
        if (theorical == "Y"):
            bt = True
        label = input("If you want to display a label with each probability type 'Y': ")
        bl = False
        if (label == "Y"):
            bl = True
        type = input("Choose a mode: Ngoats (ng) or Interval (i) ")
        while (type != "ng" and type != "i"):
            type = input("Type 'ng' or 'i': ")
        if (type == "ng"):
            doors = int(input("The number of doors is: "))
            while (doors < 2):
                doors = int(input("Please, type a number >= 3: "))
            Ngoats(N,doors,bt,bl)
        else:
            a = int(input("Type the first door (a) of the interval: "))
            b = int(input("Type the last door (b): "))
            while (a < 3 or a >= b):
                print("a >= 3 and b > a")
                a = int(input("Please, type (a): "))
                b = int(input("Type (b): "))
            g = input("Type (o) for one goat in all simulations and (n) for n-2 goats: ")
            while (g != "o" and g != "n"):
                g = input("Type 'o' or 'n': ")
            bg = False
            if (g == "n"):
                bg = True
            interval(N,a,b,bg,bt,bl)

    else:
        sampling(N)

main()
