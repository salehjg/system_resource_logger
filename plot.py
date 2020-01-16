import numpy as np
import matplotlib.pyplot as plt


class log_obj:
    swap_used = 0
    swap_percent = 0
    ram_used = 0
    ram_percent = 0
    cpu_percents = []

    def set_swap(self, obj):
        self.swap_used = obj.used / 1024.0 / 1024.0 / 1024.0
        self.swap_percent = obj.percent

    def set_ram(self, obj):
        self.ram_used = obj.used / 1024.0 / 1024.0 / 1024.0
        self.ram_percent = obj.percent

    def set_cpu(self, obj):
        self.cpu_percents = obj

    def get_log(self):
        arr = []
        arr.append(self.swap_used)
        arr.append(self.swap_percent)

        arr.append(self.ram_used)
        arr.append(self.ram_percent)

        for element in self.cpu_percents:
            arr.append(element)
        return arr

    def __str__(self):
        return str(self.get_log())


samples = []


def plot():
    saved_logs = np.load('data.npy')
    print 'shape: ', saved_logs.shape

    time_axis = np.arange(0, saved_logs.shape[0])

    plt.figure(figsize=(9, 3))

    plot1 = plt.subplot(311)
    for i in range(4, saved_logs.shape[-1]):
        plot1.plot(time_axis, saved_logs[:, i], label=''.join(['CPU', str(i-4)]))  # cpu percent
    plot1.title.set_text('CPU')
    plot1.legend(loc='upper right', borderaxespad=0.)

    plot2 = plt.subplot(312)
    plot2.plot(time_axis, saved_logs[:, 2], label='ram used')  # ram used
    plot2.plot(time_axis, saved_logs[:, 3], label='ram percent')  # ram percent
    plot2.title.set_text('Memory')
    plot2.legend(loc='upper right', borderaxespad=0.)

    plot3 = plt.subplot(313)
    plot3.plot(time_axis, saved_logs[:, 0], label='swap used')  # swap used
    plot3.plot(time_axis, saved_logs[:, 1], label='swap percent')  # swap percent
    plot3.title.set_text('SWAP')
    plot3.legend(loc='upper right', borderaxespad=0.)

    plt.show()


def main():
    plot()


main()
