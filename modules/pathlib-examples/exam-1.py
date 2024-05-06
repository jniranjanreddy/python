from pathlib import Path
# # Creating a path
# path = Path("/tmp/testdir2")

# # Check if the path exists
# if path.exists():
#     print("Directory exists")
# else:
#     print("Directory does not exist")

# path.mkdir(parents=True, exist_ok=True)

############################################
# Create a Path object for the directory
directory = Path("/tmp/testdir2", "a")

# Iterate through all files in the directory
# for file in directory
#     print(file)
#######################################
file_path = Path("/tmp/testdir2", "a")
print(file_path)

# Write to a file
with open(file_path, "w") as file:
    file.write("Hello, world!")

# Append to a file
with open(file_path, "a") as file:
    file.write("\nAppending new line!")

# Read the contents of the modified file
with open(file_path, "r") as file:
    contents = file.read()
    print(contents) 