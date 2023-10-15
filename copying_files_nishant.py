import shutil
import os

file_to_copy = "This PC/Anant's M51/Internal storage/Download"
destination_directory = 'F:/delete'

if os.path.exists(file_to_copy):
    try:
        shutil.copytree(file_to_copy, destination_directory)   
        print("File copied successfully.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"The source file '{file_to_copy}' does not exist.")




