class Heap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def parentIndex(self, index):
        return (index - 1) // 2

    def leftChildIndex(self, index):
        return 2 * index + 1

    def rightChildIndex(self, index):
        return 2 * index + 2

    def leftChild(self, index):
        idx = self.leftChildIndex(index)
        return self.heapList[idx] if idx < self.size else -1

    def rightChild(self, index):
        idx = self.rightChildIndex(index)
        return self.heapList[idx] if idx < self.size else -1

    def maximumChildIndex(self, idx):
        left = self.leftChild(idx)
        right = self.rightChild(idx)
        if right == -1 or left > right:
            return self.leftChildIndex(idx)
        else:
            return self.rightChildIndex(idx)

    def interchangeTopWithBottom(self):
        '''
        Interchange first and last element of heap
        :return:
        '''
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[self.size - 1]
        self.heapList[self.size - 1] = tmp
        self.size -= 1
        self.percolateDown(0)

    def buildHeap(self, lista):
        self.size = len(lista)
        self.heapList = lista[:]
        i = len(lista) // 2
        while i >= 0:
            self.percolateDown(i)
            i -= 1

    def percolateDown(self, i):
        pass  

class MaxHeap(Heap):
    def percolateDown(self, i):
        while self.leftChildIndex(i) < self.size:
            maxIdx = self.maximumChildIndex(i)
            if self.heapList[i] < self.heapList[maxIdx]:
                self.heapList[i], self.heapList[maxIdx] = self.heapList[maxIdx], self.heapList[i]
            i = maxIdx

if __name__ == "__main__":
    list = [10, 3, 9, 1, 2, 7, 8, 12, 465, 7767, 2, 45]

    print("====== Array Unsorted =======")
    print(list)

    heap = MaxHeap()
    heap.buildHeap(list)

    print("========== Heaps ============")
    print(heap.heapList)

    print("======- Start Sorted ========")
    for i in range(len(heap.heapList)):
        print("--- Extract %d number -----" % (i + 1))
        heap.interchangeTopWithBottom()
        print(heap.heapList)

    print("======- Array Sorted ========")
    print(heap.heapList)