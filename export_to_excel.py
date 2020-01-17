import xlwt
import numpy as np
from tqdm import tqdm
from mine_logged_data import generate_cpu_core_used

def convert2excel():
    saved_log = np.load('data.npy')
    core_usage_cnt = generate_cpu_core_used(saved_log, 10.0)
    print 'shape: ', saved_log.shape

    wb = xlwt.Workbook()
    ws = wb.add_sheet('logged data')

    ws.write(0, 0, "minutes")
    ws.write(0, 1, "swap_used_GB")
    ws.write(0, 2, "swap_percent")

    ws.write(0, 3, "ram_used_GB")
    ws.write(0, 4, "ram_percent")

    for q in range(saved_log.shape[1] - 5):
        ws.write(0, 5 + q, ''.join(['CPU', str(q)]))

    ws.write(0, saved_log.shape[1], "used_core_count")

    for i in tqdm(range(saved_log.shape[0])):
        ws.write(i + 1, 0, saved_log[i, 0])
        ws.write(i + 1, 1, saved_log[i, 0 + 1])
        ws.write(i + 1, 2, saved_log[i, 1 + 1])

        ws.write(i + 1, 3, saved_log[i, 2 + 1])
        ws.write(i + 1, 4, saved_log[i, 3 + 1])

        for q in range(5, saved_log.shape[-1]):
            ws.write(i + 1, q, saved_log[i, q])
        
        ws.write(i + 1, saved_log.shape[1], core_usage_cnt[i])

    wb.save('data.xls')


def main():
    convert2excel()


main()
