class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left

        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right

        if max_index != i:
            self.swap(i, max_index)
            self._heapify_down(max_index)

    def __str__(self):
        return str(self.heap)

# Example usage
if __name__ == "__main__":
    heap = MaxHeap()
    
    # Insert elements
    heap.insert(4)
    heap.insert(10)
    heap.insert(8)
    heap.insert(5)
    heap.insert(1)

    print("Heap after insertions:", heap)
    print("Maximum element:", heap.get_max())

    # Delete the maximum element
    max_val = heap.delete()
    print("Deleted maximum element:", max_val)
    print("Heap after deletion:", heap)

    # Insert more elements
    heap.insert(6)
    heap.insert(9)

    print("Heap after more insertions:", heap)
    print("Maximum element:", heap.get_max())

