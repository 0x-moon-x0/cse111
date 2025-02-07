# tutorial followed to create this: https://www.youtube.com/watch?v=KAmZe5D3v5I&ab_channel=Kite

import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

GREY = (0.78, 0.78, 0.78)   # uninfected
RED = (0.96, 0.15, 0.15)    # infected
GREEN = (0, 0.86, 0.03)     # recovered
BLACK = (0, 0, 0)           # dead

COVID19_PARAMS = {
    "r0": 2.28,
    "incubation": 5,
    "percent_mild": 0.8,
    "mild_recovery": (7, 14),
    "percent_severe": 0.2,
    "severe_recovery": (21, 42),
    "severe_death": (14, 56),
    "fatality_rate": 0.034,
    "serial_interval": 7
}

def main():

    coronavirus = Virus(COVID19_PARAMS)
    coronavirus.animate()
    plt.show()

class Virus():
    def __init__(self, params):

        # create plot
        self.fig = plt.figure()                                     # create empty figure
        self.axes = self.fig.add_subplot(111, projection="polar")   # create a polar plot (1st subplot, 1x1 grid)
        self.axes.grid(False)                                       # remove grid lines
        self.axes.set_xticklabels([])                               # and tick marks
        self.axes.set_yticklabels([]) 
        self.axes.set_ylim(0, 1)                                    # set the radius of the plot to 1

        # create annotations
        self.day_text = self.axes.annotate(                         # this annotation will display at the top
            "Day 0", xy=[np.pi / 2, 1], ha="center", va="bottom")   # np.pi / 2 is the theta value of pi over 2 (specifies the y axis) and 1 is the r value (specifies the top of the circle)
        self.infected_text = self.axes.annotate(
            "Infected: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=RED) # these annotations will display at the bottom
        self.deaths_text = self.axes.annotate(
            "\nDeaths: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=BLACK)
        self.recovered_text = self.axes.annotate(
            "\n\nRecovered: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=GREEN)

        # create member variables
        self.day = 0
        self.total_num_infected = 0
        self.num_currently_infected = 0
        self.num_recovered = 0
        self.num_deaths = 0
        self.r0 = params["r0"]                            # measure of the contagiousness of the disease (expected number of cases generated by a single infection)
        self.percent_mild = params["percent_mild"]
        self.percent_severe = params["percent_severe"]
        self.fatality_rate = params["fatality_rate"]
        self.serial_interval = params["serial_interval"]  # average time between successive cases in a chain transmission

        # for each infected person, there is some amount of time between the emergence of symptoms and the outcome of the disease (whether they recover or die).
        # this interval depends on the severity of the symptoms tends to be longer for those who ultimately die.

        # the various ranges represented as days are stored in these params.

        self.mild_fast = params["incubation"] + params["mild_recovery"][0]
        self.mild_slow = params["incubation"] + params["mild_recovery"][1]
        self.severe_fast = params["incubation"] + params["severe_recovery"][0]
        self.severe_slow = params["incubation"] + params["severe_recovery"][1]
        self.death_fast = params["incubation"] + params["severe_death"][0]
        self.death_slow = params["incubation"] + params["severe_death"][1]

        self.mild = {i: {"thetas": [], "rs": []} for i in range(self.mild_fast, 365)} # setting the upper bound of the pandemic simulation to 1 year

        # creating a severe dictionary with 2 keys: recovery and death

        self.severe = {
            "recovery": {i: {"thetas": [], "rs": []} for i in range(self.severe_fast, 365)},
            "death": {i: {"thetas": [], "rs": []} for i in range(self.death_fast, 365)}
        }

        # restricting the potential spread of the virus to only a subset of the population
        # and making it so that the virus spreads from the center outward

        self.exposed_before = 0   # people who has been exposed to the virus already 
        self.exposed_after = 1    # total number of people who will be exposed to the virus by the end of the current wave

        self.initial_population()


    def initial_population(self):

        population = 4500   # initializing the plot with a population of 4500
        self.num_currently_infected = 1
        self.total_num_infected = 1
        indices = np.arange(0, population) + 0.5

        # these two lists are used to plot points in the visualization and to keep track of each person in the population

        self.thetas = np.pi * (1 + 5**0.5) * indices
        self.rs = np.sqrt(indices / population)

        # plotting the data points

        self.plot = self.axes.scatter(self.thetas, self.rs, s=5, color=GREY) # size 5, color grey

        # patient zero

        self.axes.scatter(self.thetas[0], self.rs[0], s=5, color=RED) # updating the patient 0's color to red (infected) at the center of the plot
        self.mild[self.mild_fast]["thetas"].append(self.thetas[0])    # giving them mild symptoms with the quickest recovery
        self.mild[self.mild_fast]["rs"].append(self.rs[0])


    def spread_virus(self, i):
        # calculates the number of newly infected people using a serial interval of 7 days
        # the number of people exposed in a given wave is the difference between exposed_before and exposed_after

        self.exposed_before = self.exposed_after # at the beginning of a wave, set exposed_before to the value of exposed after of the last wave that we saw

        if self.day % self.serial_interval == 0 and self.exposed_before < 4500:  # check whether the current day is a multiple of the serial interval and whether the exposed population is less than the total population

            self.num_new_infected = round(self.r0 * self.total_num_infected) # calculate the number of newly infected people (r0 * people who are already infected and round)
            self.exposed_after += round(self.num_new_infected * 1.1) # 10% of the population is not succeptible to the contagion

            if self.exposed_after > 4500: # making sure the number of assigned exposures doesn't surpass the total number of the population
                self.num_new_infected = round((4500 - self.exposed_before) * 0.9)
                self.exposed_after = 4500
                
            self.num_currently_infected += self.num_new_infected
            self.total_num_infected += self.num_new_infected

            self.new_infected_indices = list(
                np.random.choice(  # randomly select the newly infected people
                    range(self.exposed_before, self.exposed_after),
                    self.num_new_infected,
                    replace=False))
            
            thetas = [self.thetas[i] for i in self.new_infected_indices]
            rs = [self.rs[i] for i in self.new_infected_indices]

            self.anim.event_source.stop() # pauses the other animation for spread_virus

            if len(self.new_infected_indices) > 15:

                size_list = round(len(self.new_infected_indices) / 15)
                theta_chunks = list(self.chunks(thetas, size_list))
                r_chunks = list(self.chunks(rs, size_list))

                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.one_by_one,
                    interval=50,
                    frames=len(theta_chunks),
                    fargs=(theta_chunks, r_chunks, RED))
                
            else:

                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.one_by_one,
                    interval=50,
                    frames=len(thetas),
                    fargs=(thetas, rs, RED))
                
            self.assign_symptoms()

        self.day += 1

        self.update_status()
        self.update_text()


    def one_by_one(self, i, thetas, rs, color):   # plots points individually

        self.axes.scatter(thetas[i], rs[i], s=5, color=color)

        if i == (len(thetas) - 1):   # once the points for a given wave are plotted, stop anim2 and start anim

            self.anim2.event_source.stop()
            self.anim.event_source.start()


    def chunks(self, a_list, n):   # generator function that divides a given list into chunks of equal size

        for i in range(0, len(a_list), n):

            yield a_list[i:i + n]


    def assign_symptoms(self):
        # calculates the number of mild and severe cases in the new wave of people

        num_mild = round(self.percent_mild * self.num_new_infected)
        num_severe = round(self.percent_severe * self.num_new_infected)

        # choose random subset of newly infected to have mild symptoms

        self.mild_indices = np.random.choice(self.new_infected_indices, num_mild, replace=False)

        # assign the rest severe symptoms, either resulting in recovery or death

        remaining_indices = [i for i in self.new_infected_indices if i not in self.mild_indices]
        percent_severe_recovery = 1 - (self.fatality_rate / self.percent_severe) # % of severe cases that recovered
        num_severe_recovery = round(percent_severe_recovery * num_severe)

        # sorting severe cases into 2 groups 

        self.severe_indices = []
        self.death_indices = []

        # if there are any severe cases in a given wave, use percent_severe_recovery to sort severe cases in the correct proportion to these two new lists:

        if remaining_indices:
            self.severe_indices = np.random.choice(remaining_indices, num_severe_recovery, replace=False)
            self.death_indices = [i for i in remaining_indices if i not in self.severe_indices]

        # assign recovery/death day
        low = self.day + self.mild_fast  # calculate the lower and
        high = self.day + self.mild_slow # upper bound for the day of the recovery

        for mild in self.mild_indices:
            recovery_day = np.random.randint(low, high) # randomly choosing a recovery day within this range
            mild_theta = self.thetas[mild]
            mild_r = self.rs[mild]
            self.mild[recovery_day]["thetas"].append(mild_theta) # appending the theta and
            self.mild[recovery_day]["rs"].append(mild_r)         # r coordinates to the lists that are sorted as values to their respective keys

            # same logic for the below:

        low = self.day + self.severe_fast
        high = self.day + self.severe_slow

        for recovery in self.severe_indices:
            recovery_day = np.random.randint(low, high)
            recovery_theta = self.thetas[recovery]
            recovery_r = self.rs[recovery]
            self.severe["recovery"][recovery_day]["thetas"].append(recovery_theta)
            self.severe["recovery"][recovery_day]["rs"].append(recovery_r)

        low = self.day + self.death_fast
        high = self.day + self.death_slow

        for death in self.death_indices:
            death_day = np.random.randint(low, high)
            death_theta = self.thetas[death]
            death_r = self.rs[death]
            self.severe["death"][death_day]["thetas"].append(death_theta)
            self.severe["death"][death_day]["rs"].append(death_r)


    def update_status(self):    # updates the color of plotpoints when a recovery or death occurs

        if self.day >= self.mild_fast: # mild cases recovery (green)
            mild_thetas = self.mild[self.day]["thetas"]
            mild_rs = self.mild[self.day]["rs"]
            self.axes.scatter(mild_thetas, mild_rs, s=5, color=GREEN)
            self.num_recovered += len(mild_thetas)
            self.num_currently_infected -= len(mild_thetas)

        if self.day >= self.severe_fast: # severe cases recovery (green)
            rec_thetas = self.severe["recovery"][self.day]["thetas"]
            rec_rs = self.severe["recovery"][self.day]["rs"]
            self.axes.scatter(rec_thetas, rec_rs, s=5, color=GREEN)
            self.num_recovered += len(rec_thetas)
            self.num_currently_infected -= len(rec_thetas)

        if self.day >= self.death_fast: # severe cases death (black)
            death_thetas = self.severe["death"][self.day]["thetas"]
            death_rs = self.severe["death"][self.day]["rs"]
            self.axes.scatter(death_thetas, death_rs, s=5, color=BLACK)
            self.num_deaths += len(death_thetas)
            self.num_currently_infected -= len(death_thetas)


    def update_text(self):  # updates the annotations when the day changes, or when a recovery, infection, or death occurs

        self.day_text.set_text("Day {}".format(self.day))
        self.infected_text.set_text("Infected: {}".format(self.num_currently_infected))
        self.deaths_text.set_text("\nDeaths: {}".format(self.num_deaths))
        self.recovered_text.set_text("\n\nRecovered: {}".format(self.num_recovered))


    def gen(self):    # generator that determines the iteration at which the repeated call to spread_virus is terminated

        while self.num_deaths + self.num_recovered < self.total_num_infected: 
            # if the number of deaths together with the number of recoveries is less than the total number of infections

            yield  # then iterate over the sequence


    def animate(self):  # creates the spread animation

        self.anim = ani.FuncAnimation(
            self.fig,
            self.spread_virus,
            frames=self.gen,  # the frames are determined by the gen function
            repeat=True)


if __name__ == "__main__":
    main()