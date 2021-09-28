from PIL import Image

output_path = "./output_data/"
def decode(nft_file):
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


def getFileSize(size_bytes):
  (byte_four, byte_three, byte_two, byte_one) = size_bytes
  return byte_four * (256**3) + byte_three * (256**2) + byte_two * (256) + byte_one
