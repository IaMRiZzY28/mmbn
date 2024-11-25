
with open('example.txt', 'w') as f:
    f.write("Hello, this is a sample text.\n")
    f.write("Python file operations are simple!")


with open('example.txt', 'r') as f:
    content = f.read()
    print("File Content:")
    print(content)


with open('example.txt', 'a') as f:
    f.write("\nAppending a new line to the file!")


with open('example.txt', 'r') as f:
    updated_content = f.read()
    print("\nUpdated File Content:")
    print(updated_content)

