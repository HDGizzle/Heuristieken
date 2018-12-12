import matplotlib.pyplot as plt

stdev_tracker = [0.2, 0.4, 3, 4, 2.3, 4.1, 2.1, 2.3]
cost_tracker = [100, 200, 400, 3300, 2233, 2103, 203, 458, 309, 50]

def stdev_plotter(stdev_tracker):
    dict = {"0.5" : 0, "1" : 0, "1.5" : 0, "2" : 0, "2.5" : 0, "3" : 0, "3.5" : 0, "4" : 0, "4.5" : 0, "5" : 0, "5.5" : 0, "6" : 0, "6.5" : 0, "7" : 0, "7.5" : 0, "8" : 0, "8.5" : 0, "9" : 0, "9.5" : 0, "10" : 0}
    for stdev in stdev_tracker:
        if stdev < 0.5:
            dict["0.5"] += 1
        elif stdev < 1:
            dict["1"] += 1
        elif stdev < 1.5:
            dict["1.5"] += 1
        elif stdev < 2:
            dict["2"] += 1
        elif stdev < 2.5:
            dict["2.5"] += 1
        elif stdev < 3:
            dict["3"] += 1
        elif stdev < 3.5:
            dict["3.5"] += 1
        elif stdev < 4:
            dict["4"] += 1
        elif stdev < 4.5:
            dict["4.5"] += 1
        elif stdev < 5:
            dict["5"] += 1
        elif stdev < 5.5:
            dict["5.5"] += 1
        elif stdev < 6:
            dict["6"] += 1
        elif stdev < 6.5:
            dict["6.5"] += 1
        elif stdev < 7:
            dict["7"] += 1
        elif stdev < 7.5:
            dict["7.5"] += 1
        elif stdev < 8:
            dict["8"] += 1
        elif stdev < 8.5:
            dict["8.5"] += 1
        elif stdev < 9:
            dict["9"] += 1
        elif stdev < 9.5:
            dict["9.5"] += 1
        elif stdev < 10:
            dict["10"] += 1

    plt.bar(list(dict.keys()), dict.values(), color="g")
    plt.xlabel("stdev")
    plt.ylabel("Frequency")
    plt.show()

# 23.75 - 20.75 - 24.25 - 28

def cost_plotter(cost_tracker):
    dict = {"100": 0, "200": 0, "300": 0, "400": 0, "500": 0, "600": 0, "700": 0, "800": 0, "900": 0, "1000": 0, "1100": 0, "1200": 0, "1300": 0, "1400": 0, "1500": 0, "1600" : 0, "1700": 0, "1800" : 0, "1900" : 0, "2000": 0, "2100": 0, "2200": 0, "2300": 0, "2400": 0, "2500": 0, "2600": 0, "2700": 0, "2800": 0, "2900": 0, "3000": 0}
    for cost in cost_tracker:
        if cost < 100:
            dict["100"] += 1
        elif cost < 300:
            dict["300"] += 1
        elif cost < 400:
            dict["400"] += 1
        elif cost < 500:
            dict["500"] += 1
        elif cost < 600:
            dict["600"] += 1
        elif cost < 700:
            dict["700"] += 1
        elif cost < 800:
            dict["800"] += 1
        elif cost < 900:
            dict["900"] += 1
        elif cost < 1000:
            dict["1000"] += 1
        elif cost < 1100:
            dict["1100"] += 1
        elif cost < 1200:
            dict["1200"] += 1
        elif cost < 1300:
            dict["1300"] += 1
        elif cost < 1400:
            dict["1400"] += 1
        elif cost < 1500:
            dict["1500"] += 1
        elif cost < 1600:
            dict["1600"] += 1
        elif cost < 1700:
            dict["1700"] += 1
        elif cost < 1800:
            dict["1800"] += 1
        elif cost < 1900:
            dict["1900"] += 1
        elif cost < 2000:
            dict["2000"] += 1
        elif cost < 2100:
            dict["2100"] += 1
        elif cost < 2200:
            dict["2200"] += 1
        elif cost < 2300:
            dict["2300"] += 1
        elif cost < 2400:
            dict["2400"] += 1
        elif cost < 2500:
            dict["2500"] += 1
        elif cost < 2600:
            dict["2600"] += 1
        elif cost < 2700:
            dict["2700"] += 1
        elif cost < 2800:
            dict["2800"] += 1
        elif cost < 2900:
            dict["2900"] += 1
        elif cost < 3000:
            dict["3000"] += 1

    plt.bar(list(dict.keys()), dict.values(), color="g")
    plt.xlabel("Costs")
    plt.ylabel("Frequency")
    plt.show()

cost_plotter(cost_tracker)
# stdev_plotter(stdev_tracker)
