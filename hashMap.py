import hashlib

class HashMap():
  def __init__(self, size=4):
    self.reset(size)

  def reset(self, size):
    self.size = size
    self.store = [ [] for _ in range(size) ]
    self.count = 0

  def getIndex(self, key):
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % self.size

  def insert(self, key, val):
    index = self.getIndex(key)
    bucket = self.store[index]
    for tup in bucket:
      if tup[0] == key:
        tup[1] = val
        return False
    bucket.append([key, val])
    self.count += 1
    if self.count >= self.size / 2:
      self.resize(self.size * 2)
    return True

  def retrieve(self, key):
    index = self.getIndex(key)
    bucket = self.store[index]
    for tup in bucket:
      if tup[0] == key:
        return tup[1]

  def remove(self, key):
    index = self.getIndex(key)
    bucket = self.store[index]
    for i, tup in enumerate(bucket):
      if tup[0] == key:
        del bucket[i]
        self.count -= 1
        if self.size > 4 and self.count < self.size / 4:
          self.resize(int(self.size / 2))
        return True
    return False
  
  def resize(self, newSize):
    oldStore = self.store
    self.reset(newSize)
    for bucket in oldStore:
      for tup in bucket:
        self.insert(tup[0], tup[1])
