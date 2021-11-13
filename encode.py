import numpy as np
import math
from PIL import Image
import time

input_path = "./input_data/"
output_path = "./output_data/"

def encodeGrayscale(input_file):
  with open(input_path + input_file, "rb") as f:
      data = f.read()
  arr = np.zeros((math.ceil(len(data)**0.5)**2 + (math.ceil(len(data)**0.5)), 1), dtype=np.uint8)
  size_bytes = getByteSize(len(data))
  (arr[0], arr[1], arr[2], arr[3]) = size_bytes
  add = math.ceil(len(data)**0.5)
  for i, char in enumerate(data):
      arr[i + add] = int(char)
  arr = arr.reshape(math.ceil(len(data)**0.5) + 1, math.ceil(len(data)**0.5))
  im = Image.fromarray(np.uint8(arr), 'L')
  tmp_file = output_path + input_file + ".png"
  im.save(tmp_file)


def getByteSize(size):
    byte_four = int(size / (256**3))
    leftover = size - byte_four * (256**3)
    byte_three = int(leftover / (256**2))
    leftover = leftover - byte_three * (256**2)
    byte_two = int(leftover / (256**1))
    leftover = leftover - byte_two * (256**1)
    byte_one = int(leftover / (256**0))
    return (byte_four, byte_three, byte_two, byte_one)
