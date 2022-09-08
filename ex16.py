# import argv
from sys import argv
# script = sys.argv[0], filename = sys.argv[1]
script, filename = argv
# print command
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN.")
input("?")

print("Opening the file...")
# variable target = buka filename dan buat status jadi write+
target = open(filename, 'w+')


print("Truncating the file. Goodbye!")
# hapus isi variable target
target.truncate()

print("Now i'm going to ask you for three lines.")
# mengambil iput dari user
line1 = input("Line ")
line2 = input("Line ")
line3 = input("Line ")

print("I'm going to write these to the file.")
# menulis isi variable ke filename
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# tutup target
target.close()