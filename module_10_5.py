import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_time1 = time.perf_counter()  # начало отсчета времени

    for filename in filenames:
        read_info(filename)

    end_time1 = time.perf_counter()  # конец отсчета времени
    print(end_time1 - start_time1)

    with Pool() as pool1:
        start_time2 = time.perf_counter()
        results = pool1.map(read_info, filenames)
        end_time2 = time.perf_counter()
    print(end_time2 - start_time2)
