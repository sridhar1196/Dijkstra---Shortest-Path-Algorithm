class HeapSort:
    def __init__(self):
        self.heap = []
        self.last_index = 0
        pass


    def insert(self, new_val):
        self.heap.insert(self.last_index, new_val)
        self.last_index += 1
        i = self.last_index
        while (i > 1):
            print("Heap:", self.heap)
            print("Index:", self.last_index)
            print("I:", i)
            if (i <= 0):
                break
            # elif ((i % 2) == 0):
            #     print(int(i / 2))
            #     if (self.heap[int(i / 2)] <= self.heap[i]):
            #         break
            #     else:
            #         temp = self.heap[i]
            #         self.heap[i] = self.heap [int(i / 2)]
            #         self.heap[int(i / 2)] = temp
            #         i = int(i / 2)
            else:
                if (self.heap[int((i)/2) - 1] <= self.heap[i - 1]):
                    break
                else:
                    temp = self.heap[i - 1]
                    self.heap[i - 1] = self.heap[int(i/2 - 1)]
                    self.heap[int(i/2) - 1] = temp
                    i = int(i/2)

    def remove_min(self):
        print(len(self.heap))
        print(self.last_index)
        if(len(self.heap) > 0 ):
            if(len(self.heap) == 1):
                return self.heap.pop(self.last_index - 1)
            else:
                min_element = self.heap[0]
                self.heap[0] = self.heap.pop(self.last_index - 1)
                self.last_index = self.last_index - 1
                i = 1
                min_ind = i
                while (i <= self.last_index):
                    if (((2 * i) <= self.last_index) and (self.heap[(2 * i) - 1] < self.heap[min_ind - 1])):
                        min_ind = 2 * i
                    if ((((i * 2) + 1) <= self.last_index) and (self.heap[i * 2] < self.heap[min_ind - 1])):
                        min_ind = (i * 2) + 1
                    if (min_ind != i):
                        temp = self.heap[i - 1]
                        self.heap[i - 1] = self.heap[min_ind - 1]
                        self.heap[min_ind - 1] = temp
                        i = min_ind
                    else:
                        break
                return min_element
        else:
            return None

if(__name__ == "__main__"):
    heap = HeapSort()
    heap.insert(3)
    heap.insert(2)
    heap.insert(5)
    heap.insert(10)
    heap.insert(7)
    heap.insert(4)
    heap.insert(1)
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    heap.remove_min()
    print(heap.heap)
    pass