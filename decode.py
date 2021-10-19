from PIL import Image

input_path = "./input_data/"
output_path = "./output_data/"

def decodeGrayscale(nft_file):
  print("decoding")
  out_file ="rec-" + ".".join(nft_file.split(".")[:-1]) 
  with open(output_path + out_file, "wb") as f:
    im = Image.open(output_path + nft_file)
    num_cols = im.size[0]
    data = im.getdata()
    databytes = bytes(data)
    (byte_four, byte_three, byte_two, byte_one) = databytes[0:4]
    datasize = getFileSize((byte_four, byte_three, byte_two, byte_one))
    print("recovered file size: " + str(datasize))
    print("writing")
    f.write(databytes[num_cols: num_cols + datasize])


def decodeRGB(nft_file):
  out_file = output_path + "rec-" + ".".join(nft_file.split(".")[:-1])
  print(output_path + nft_file)
  im = Image.open(output_path + nft_file)

  data = im.getdata()
  size_bytes = getFileSize(data[0][0], data[0][1], data[0][2], data[1][2])
  
  sz = 3*len(im.getdata())
  arr = bytearray([0]*sz)
  i = 0
  print(size_bytes)
  for elem in data:
    arr[i] = elem[0]
    arr[i+1] = elem[1]
    arr[i+2] = elem[2]
    i = i + 3

  with open(out_file, "wb") as f:
    f.write(bytes(arr))


def getFileSize(size_bytes):
  (byte_four, byte_three, byte_two, byte_one) = size_bytes
  return byte_four * (256**3) + byte_three * (256**2) + byte_two * (256) + byte_one
