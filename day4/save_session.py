# Open file, write data, close file
file = open("data.txt", "w")
file.write("Some text")
file.close()
# Better way auto closes
with open("data.txt", "w") as file:
    file.write("Some text")

