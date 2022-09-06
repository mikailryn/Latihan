# Ambil "fitur" argy 
from sys import argv

# beri variable ke argument argv (ex: script = argv[0] dan filename = argv[1])
script, filename = argv 
# buka variable filename (argv[1]) 
txt = open(filename)

print(" ")

# print filename
print(f"Here's your file {filename}:")
# baca variable txt
print(txt.read())

# tutp file txt
txt.close()

print(" ")

# print string
print("Type the filename again:")
# mengambil input dari user
file_again = input("> ")

print(" ")

# memasukan input user ke variable txt_again
txt_again = open(file_again)

# membuka variable txt_again
print(txt_again.read())

# tutup file txt_again
txt_again.close()

print(" ")