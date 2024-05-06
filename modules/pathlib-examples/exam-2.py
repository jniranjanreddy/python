from pathlib import Path

myPATH = Path("/tmp", "test")
print(myPATH)

with open(myPATH, "w") as file:
   file.write("Hello Wor")


with open(myPATH, "a") as file:
   file.write("Appending new line")

with open(myPATH, "r") as file:
   content = file.read()
   contents = file.readlines()

   print(content)
   print(contents)