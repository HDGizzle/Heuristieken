import matplotlib.pyplot as plt


def plotter(costs):
    """
    this function plots bars based on observations and frequency
    """
    # the amount of bars you want to use
    bars = 3

    costs = sorted(costs)

    max = costs[-1]

    length = len(costs)

    # generate dictionary to count frequency of group components
    bars_dict = {}
    for i in range(bars):

        # minimum value in bar is used as bar key
        bars_dict[str(max * (i + 1) / bars)] = 0

    # startpoint for cost list iteration
    start = 0

    # iterate over the amount of bars
    for i in range(bars):

        # iterate over list
        for j in range(start, length):

            # add frequency to respective bar
            if costs[j] <= max * (i + 1) / bars:
                bars_dict[str(max * (i + 1) / bars)] += 1

            # if costs need to be added to new bar stop
            else:
                # adjust startpoint in cost list to new bar
                start = j
                break

    # plot function
    plt.bar(bars_dict.keys(), bars_dict.values(), color="g")
    plt.xlabel("Costs")
    plt.ylabel("Frequency")
    plt.show()
