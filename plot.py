import numpy as np
import matplotlib.pyplot as plt

samples = []


def plot():
    saved_logs = np.load('data.npy')
    print 'shape: ', saved_logs.shape

    time_axis = saved_logs[:, 0]

    plt.figure(figsize=(9, 3))

    plot1 = plt.subplot(311)
    for i in range(5, saved_logs.shape[-1]):
        plot1.plot(time_axis, saved_logs[:, i], label=''.join(['CPU', str(i - 4)]))  # cpu percent
    plot1.title.set_text('CPU')
    plot1.legend(loc='upper right', borderaxespad=0.)

    plot2 = plt.subplot(312)
    plot2.plot(time_axis, saved_logs[:, 2+1], label='used GB')  # ram used
    plot2.plot(time_axis, saved_logs[:, 3+1], label='ram percent')  # ram percent
    plot2.title.set_text('Memory')
    plot2.legend(loc='upper right', borderaxespad=0.)

    plot3 = plt.subplot(313)
    plot3.plot(time_axis, saved_logs[:, 0+1], label='used GB')  # swap used
    plot3.plot(time_axis, saved_logs[:, 1+1], label='swap percent')  # swap percent
    plot3.title.set_text('SWAP')
    plot3.legend(loc='upper right', borderaxespad=0.)

    plt.show()


def main():
    plot()


main()
