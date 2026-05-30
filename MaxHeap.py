# Zechen Tian 1723669
# I implemented this file independently for assignment.

class MaxHeap:

  def __init__(self, capacity = 10**6):
    self.data = [0] * (capacity + 1)
    self.size = 0
    self.capacity = capacity

# parent node: i // 2, left child node: 2 * i, right child node: 2 * i + 1
  def bubble_up(self, i):
    while i > 1 and self.data[i] > self.data[i // 2]:
      self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
      i = i // 2
# If node i is larger than the parent, it is swapped until the heap property is satisfied

  def bubble_down(self, i):
    while True:
      largest = i
      left = 2 * i
      right = 2 * i + 1
      if left <= self.size and self.data[left] > self.data[largest]:
        largest = left
      if right <= self.size and self.data[right] > self.data[largest]:
        largest = right
      if largest == i:
        break
      
      self.data[i], self.data[largest] = self.data[largest], self.data[i]
      i = largest
# If node i is smaller than the child, it is swapped with the largest child

  def push(self, key):
    self.size += 1
    self.data[self.size] = key
    self.bubble_up(self.size)
# push a new element

  def pop(self):
    if self.size == 0:
      return None
    top = self.data[1]
    # Move the last element to the root, and bubble down
    self.data[1] = self.data[self.size]
    self.size -= 1
    if self.size > 0:
      self.bubble_down(1)
    return top
# pop the largest element and remove it

  def getTop(self):
    if self.size == 0:
      return None
    return self.data[1]
# return the largest element

  def isEmpty(self):
    return self.size == 0

  def heapify(self, keys):
    self.size = len(keys)
    for i in range (self.size):
      self.data[i + 1] = keys[i]
    for i in range(self.size // 2, 0, -1):
      self.bubble_down(i)
# bubble down one by one, starting from the last non-leaf node

  def reset(self):
    self.size = 0