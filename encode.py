import numpy as np
import math
from PIL import Image
import time


def encode(input_file):
  tmp_file = input_file + ".png"
  t1 = time.time()
  with open(input_file, "rb") as f:
      data = f.read()
  arr = np.zeros((math.ceil(len(data)**0.5)**2 + (math.ceil(len(data)**0.5)), 1), dtype=np.uint8)
  size_bytes = getByteSize(len(data))
  print(size_bytes)
  arr[0] = size_bytes[0]
  arr[1] = size_bytes[1]
  arr[2] = size_bytes[2]
  arr[3] = size_bytes[3]
  add = math.ceil(len(data)**0.5)
  for i, char in enumerate(data):
      if i % 1000000 == 0:
          print("{} of {}, {}p".format(i, len(data), float(i)/float(len(data))))
      arr[i + add] = int(char)
  arr = arr.reshape(math.ceil(len(data)**0.5) + 1, math.ceil(len(data)**0.5))
  im = Image.fromarray(np.uint8(arr), 'L')
  print("Writing file to image")
  im.save(tmp_file)
  print("time elapsed: {}".format(time.time() - t1))


def getByteSize(size):
    byte_four = int(size / (256**3))
    leftover = size - byte_four * (256**3)
    byte_three = int(leftover / (256**2))
    leftover = leftover - byte_three * (256**2)
    byte_two = int(leftover / (256**1))
    leftover = leftover - byte_two * (256**1)
    byte_one = int(leftover / (256**0))
    return (byte_four, byte_three, byte_two, byte_one)
