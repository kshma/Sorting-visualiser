from sorting.Data import Data
from copy import deepcopy


def selection_sort(data):
    frames = [data]
    new_data = deepcopy(data)
    for i in range(0, Data.length - 1):
        min_idx = i
        for j in range(i + 1, Data.length):
            updated_data = deepcopy(new_data)
            updated_data[i].set_color('#CFCECA')
            updated_data[j].set_color('#AC8181')
            frames.append(updated_data)
            if new_data[min_idx].value > new_data[j].value:
                new_data[min_idx].set_color('#C9A959')
                new_data[j].set_color('#A7D9C9')
                min_idx = j
        new_data[i], new_data[min_idx] = new_data[min_idx], new_data[i]
        new_data[i].set_color('#253D5B')
    new_data[-1].set_color('#253D5B')
    frames.append(new_data)
    return frames