msg = "Hello world!"
file = open("newfile.txt", "w") # open instead of file.open; "w" instead of w;
amount_written = file.write(msg)
print(amount_written)
file.close()