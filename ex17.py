# import sys dan os
from genericpath import exists
import sys
import os.path
# script = sys.argv[0], from_file = sys.argv[1], to_file = sys.argv[2]
script, from_file, to_file = sys.argv

print(f"Copying form {from_file} to {to_file}")
# in_file = buka variable from_file, in_data = baca in_file
in_file = open(from_file)
in_data = in_file.read()
# mengambil input dari user
print(f"The input file is {len(in_data)} bytes long ")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
# out_file = buka to_file dan buat status jadi write
out_file = open(to_file, 'w')
# tulis isi variable in_data ke out_file
out_file.write(in_data)

print("Alright, all done.")
# tutup file
out_file.close()
in_file.close()