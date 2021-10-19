import numpy as np
import math
from PIL import Image
import time

input_path = "./input_data/"
output_path = "./output_data/"

def encodeGrayscale(input_file):
  t1 = time.time()
  with open(input_path + input_file, "rb") as f:
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
  tmp_file = output_path + input_file + ".png"
  im.save(tmp_file)
  print("time elapsed: {}".format(time.time() - t1))


def encodeRGB(input_file):
  tmp_file = input_file + ".png"
  print("Writing file to image")
  t1 = time.time()
  with open(input_path + input_file, "rb") as f:
      data = f.read()
  data_sz = len(data) + 4
  rowlen = math.ceil((data_sz/3.0)**.5)
  arr = np.zeros((3*(rowlen**2), 1), dtype=np.uint8)
  size_bytes = getByteSize(len(data))
  print(size_bytes)
  arr[0] = size_bytes[0]
  arr[1] = size_bytes[1]
  arr[2] = size_bytes[2]
  arr[3] = size_bytes[3]
  i = 4

  for char in data:
    arr[i] = int(char)
    if i % 1000000 == 0:
        print("{} of {}, {}p".format(i, data_sz, float(i)/float(data_sz)))
    i = i + 1
  arr = arr.reshape(rowlen, rowlen, 3)
  im = Image.fromarray(np.uint8(arr), 'RGB')
  im.save(output_path + tmp_file)
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
