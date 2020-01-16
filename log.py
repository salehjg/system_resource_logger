import psutil
import time
import numpy as np


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
        self.ram_used = (obj.total - obj.available) / 1024.0 / 1024.0 / 1024.0
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


def scan():
    obj = log_obj()
    obj.set_swap(psutil.swap_memory())
    obj.set_ram(psutil.virtual_memory())
    obj.set_cpu(psutil.cpu_percent(percpu=True))
    return obj


samples = []


def start_logging():
    cnt = 0
    while True:
        cnt = cnt + 1
        sample = scan()
        samples.append(sample.get_log())
        if cnt % 60 == 0:
            print 'data dumped.'
            np.save('data.npy', samples)
        time.sleep(1)


def main():
    start_logging()


main()
