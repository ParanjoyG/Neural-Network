import numpy as np

class Save_filter :

    def __init__(self) :
        self.array = []
        self.x = 0

    def create_array(self, width, height) :
        for x in range (height) :
            self.array.append([])
            for y in range (width) :
                self.array[x].append(0)
        self.array = np.array(self.array)
        return self.array

    def store_filter(self, fill) :
        with open (f'filter {self.x}.npy', 'wb') as file :
            np.save(file, fill)
        self.x += 1