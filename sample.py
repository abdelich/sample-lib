import numpy as np
import matplotlib.pyplot as plt


class Sample:
    ni = 0
    sample = 0
    n = 0
    full_sample = []

    fig, ax = [], []

    def __init__(self, sample, ni=None):
        if ni is None:
            self.ni = [1 for _ in range(len(sample))]
        else:
            self.ni = ni

        self.sample = sample
        self.n = sum(self.ni)

        self.fig, self.ax = plt.subplots(1, 3)

    def info(self):
        self.hist()
        self.cumulative_plot()
        self.cdf_plot()

        mean = self.mean()
        median = self.median()
        mode = self.mode()

        var = self.var()
        std = self.std()
        vc = self.variance_coefficient()

        vk = [self.raw_moment(k) for k in range(5)]
        mk = [self.central_moment(k) for k in range(5)]

        skew = self.skewness()
        excess = self.kurtosis()

        print(f'Mean: {mean}\n'
              f'Median: {median}\n'
              f'Mode: {mode}\n'
              f'Variance: {var}\n'
              f'Standard deviation: {std}\n'
              f'Variance coefficient: {vc}\n'
              f'Raw moments k = (0, 1, 2, 3, 4): {vk}\n'
              f'Central moments k = (0, 1, 2, 3, 4): {mk}\n'
              f'Skewness: {skew}\n'
              f'Excess coefficient (Kurtosis): {excess}')

        plt.show()

    def hist(self):
        return self.ax[0].bar(self.sample, self.ni)

    def cumulative_plot(self):
        n_cum = self.n_cumulative()
        return self.ax[1].plot(self.sample, n_cum)

    def cdf_plot(self):
        n_cm = self.n_cumulative()
        cdf = self.cdf()
        return self.ax[2].plot(n_cm, cdf)

    def n_cumulative(self):
        n_cm = [0 for _ in range(len(self.ni))]
        for i in range(len(self.sample)):
            n_cm[i] = n_cm[i-1] + self.ni[i]

        return n_cm

    def pmf(self):
        return [i/self.n for i in self.ni]

    def cdf(self):
        n_cm = self.n_cumulative()
        return [i/self.n for i in n_cm]

    def mean(self):
        return sum(np.array(self.sample) * np.array(self.ni))/self.n

    def median(self):
        for i in range(len(self.ni)):
            sub_sample = [self.sample[i]] * self.ni[i]
            self.full_sample.extend(sub_sample)

        middle = self.n // 2
        if self.n % 2 == 0:
            return (self.full_sample[middle-1] + self.full_sample[middle])/2
        else:
            return self.full_sample[middle]

    def mode(self):
        max_freq = max(self.ni)
        modes = [self.sample[i] for i in range(len(self.ni)) if self.ni[i] == max_freq]
        if len(modes) > 1:
            return modes
        else:
            return modes[0]

    def var(self):
        mean = self.mean()
        return sum([((self.sample[i] - mean)**2)*self.ni[i] for i in range(len(self.sample))])/self.n

    def std(self):
        var = self.var()
        return np.sqrt(var)

    def variance_coefficient(self):
        std = self.std()
        mean = self.mean()
        return std/mean

    def raw_moment(self, k):
        return sum([(self.sample[i]**k) * self.ni[i] for i in range(len(self.sample))])/self.n

    def central_moment(self, k):
        mean = self.mean()
        return sum([((self.sample[i] - mean)**k)*self.ni[i] for i in range(len(self.sample))])/self.n

    def skewness(self):
        return (self.central_moment(3))/(self.std()**3)

    def kurtosis(self):
        return ((self.central_moment(4))/(self.std()**4)) - 3
