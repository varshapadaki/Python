import os

# Opening a file
file = open("example.txt", "w")

# Writing to the file
file.write("Hello, World!\nThis is a test file.\n")

# Appending to the file
file = open("example.txt", "a")
file.write("Appending new content.\n")

# Closing the file
file.close()

# Reopening the file for reading
file = open("example.txt", "r")

# Reading the entire file
content = file.read()
print("Content of the file:")
print(content)

# Moving the file pointer
file.seek(0)

# Reading a specific number of characters
partial_content = file.read(10)
print("\nPartial content (first 10 characters):")
print(partial_content)

# Reading a single line
line = file.readline()
print("\nFirst line of the file:")
print(line)

# Reading all lines into a list
file.seek(0)
lines = file.readlines()
print("\nAll lines of the file:")
print(lines)

# Checking if the file is closed
is_closed = file.closed
print("\nIs the file closed?", is_closed)

# Flushing buffered data to disk
file.flush()

# Renaming the file
os.rename("example.txt", "renamed_example.txt")

# Deleting the file
os.remove("renamed_example.txt")

# Checking if a file exists
file_exists = os.path.exists("renamed_example.txt")
print("\nDoes the file exist?", file_exists)

# Getting file information
file_info = os.stat("example.txt")
print("\nFile information:")
print(file_info)

# Closing the file
file.close()

