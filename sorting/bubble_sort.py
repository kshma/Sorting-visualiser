from sorting.Data import Data
from copy import deepcopy


def bubble_sort(data):
    frames = [data]
    new_data = deepcopy(data)
    for i in range(Data.length):
        for j in range(0, Data.length-i-1):
            updated_data = deepcopy(new_data)
            updated_data[j+1].set_color('#CFCECA')
            updated_data[j].set_color('#A7D9C9')
            frames.append(updated_data)
            if new_data[j].value > new_data[j+1].value:
                new_data[j].value, new_data[j+1].value = new_data[j+1].value, new_data[j].value
                new_data[j].set_color('#AC8181')
                new_data[j+1].set_color('#C9A959')
                
                
        new_data[Data.length-i-1].set_color('#253D5B')
    frames.append(new_data)
    return frames
