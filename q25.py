#Write a program that copies the contents of one text file to another


source_file_path = 'python.txt'

# Destination file path
destination_file_path = 'new__python.txt'


with open(source_file_path, 'r') as source_file, open(destination_file_path, 'w') as destination_file:
   
    contents = source_file.read()
    
   
    destination_file.write(contents)

print(f"Contents from '{source_file_path}' have been copied to '{destination_file_path}'.")
