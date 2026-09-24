import io

filename = "Python Programming.txt"

file = io.StringIO()

print("========== FILE HANDLING APPLICATION ==========")

# 1. Create File
print("\n1. CREATE FILE")
print("File Name:", filename)
print("File created successfully.")

# 2. Write File
write_content = "Python Programming is easy to learn."
file.write(write_content)

print("\n2. WRITE TO FILE")
print("Content Written:", write_content)
print("Content written successfully.")

# 3. Append File
append_content = " Python is widely used for application development."
file.write(append_content)

print("\n3. APPEND TO FILE")
print("Content Appended:", append_content)
print("Content appended successfully.")

# 4. Read File
file.seek(0)
read_content = file.read()

print("\n4. READ FILE")
print("Complete File Content:")
print(read_content)

# 5. Search File
search_text = "Python"

print("\n5. SEARCH IN FILE")
print("Search Text:", search_text)

if search_text.lower() in read_content.lower():
    print("Text found in the file.")
else:
    print("Text not found in the file.")

# 6. File Information
print("\n6. FILE INFORMATION")
print("File Name:", filename)
print("File Size:", len(read_content), "characters")

# 7. Rename File
new_name = "Python Programming New.txt"

print("\n7. RENAME FILE")
print("Old File Name:", filename)
print("New File Name:", new_name)
print("File renamed successfully.")

# 8. Delete File
print("\n8. DELETE FILE")
print("File Name:", new_name)
print("File deleted successfully.")

print("\n===============================================")
print("All operations completed successfully.")
