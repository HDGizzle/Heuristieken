import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np

def plotter(data_list, xlabel, png_name, combinations):
    """
    this function plots bars based on observations and frequency
    """
    # the amount of bars you want to use
    bars = 20

    data_list = sorted(data_list)

    max = data_list[-1]
    min = data_list[0]

    length = len(data_list)

    # startpoint for cost list iteration
    start = 0

    # generate dictionary to count frequency of group components
    bars_dict = {}
    for i in range(bars):

        bar_division = round((((max - min) / bars) * i) + min, 2)
        # bar_division = round(max * (i + 1) / bars, 2)

        # minimum value in bar is used as bar key
        bars_dict[str(bar_division)] = 0

        # iterate over list
        for j in range(start, length):

            # add frequency to respective bar
            if data_list[j] <= bar_division:
                bars_dict[str(bar_division)] += 1

            # if data_list need to be added to new bar stop
            else:
                # adjust startpoint in cost list to new bar
                start = j
                break

    # plot function

    params = {'legend.fontsize': 'x-large',
          'figure.figsize': (12, 7),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'small',
         'ytick.labelsize':'x-large'}
    pylab.rcParams.update(params)




    plt.bar(bars_dict.keys(), bars_dict.values(), color="g")
    plt.xticks(rotation=40)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.title("Number of iterations: " + str(combinations))
    plt.show()
    plt.savefig(png_name)
    print(max)
