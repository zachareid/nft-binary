import decode
import encode

input_file = "bitcoin-22.0.tar.gz"
encode.encode(input_file)
decode.decode(input_file + ".png")




"""
print(decode.getFileSize(encode.getByteSize(1)))
print(decode.getFileSize(encode.getByteSize(255)))
print(decode.getFileSize(encode.getByteSize(256)))
print(decode.getFileSize(encode.getByteSize(40)))
print(decode.getFileSize(encode.getByteSize(123456)))
print(decode.getFileSize(encode.getByteSize(4294967295)))
print(decode.getFileSize(encode.getByteSize(4294967294)))
print(decode.getFileSize(encode.getByteSize(429496729)))
"""
