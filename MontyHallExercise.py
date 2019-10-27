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

def sampling(N,nd,ngs):

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

def main():

    N = int(input("The number of simulations is: "))
    while (N < 0):
        N = int(input("Please, type a number >= 1: "))
    nd = int(input("The number of doors is: "))
    while (nd < 2):
        nd = int(input("Please, type a number >= 3: "))
    ngs = int(input("The number of goats shown is: "))
    while (ngs < 0 or ngs > nd-2):
        ngs = int(input("Please, type a number >= 0 and <= {doors-2}: "))
    print("May the games begin!")
    sampling(N,nd,ngs)

main()
