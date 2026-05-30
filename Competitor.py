# Zechen Tian 1723669
# I implemented this file independently for assignment.

class CompetitorArray:
  def __init__(self, capacity = 10**6):
    self.A = [0] * capacity
    self.cnt = 0 # The current number of elements
    self.imax = -1 # The index of the largest element, -1 means empty
    self.capacity = capacity

#  counter cnt and the maximum value subscript imax are maintained
  def push(self, key):
    self.A[self.cnt] = key
    if self.imax == -1 or self.A[self.imax] < self.A[self.cnt]:
      self.imax = self.cnt
    self.cnt += 1
# push to the end of the array, update the imax

  def pop(self):
    if self.imax == -1:
      return None
    keymax = self.A[self.imax]
    self.A[self.imax] = self.A[self.cnt - 1]
    self.cnt -= 1 # Move the last element to imax and delete imax
    if self.cnt == 0:
      self.imax = -1
    else:
      new_imax = 0
      # linear scan finds the maximum value
      for i in range(self.cnt):
        if self.A[i] > self.A[new_imax]:
          new_imax = i
      self.imax = new_imax
    return keymax

  def getTop(self):
    if self.imax == -1:
      return None
    keymax = self.A[self.imax]
    return keymax
# Returns the largest element without removing it

  def reset(self):
    self.cnt = 0
    self.imax = -1