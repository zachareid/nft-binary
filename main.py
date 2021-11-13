import decode
import encode

input_file = "bible.txt"
output_file_format = ".png"
encode.encodeGrayscale(input_file)
decode.decodeGrayscale(input_file + output_file_format)