import os

directory = "E:/AK programs/.vscode/python/png_files"
files = os.listdir(directory)
i = 1

for file in files:
    if file.endswith(".png"):
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, f"{i}.png")
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {file} to {i}.png")
            i += 1
        except Exception as e:
            print(f"Error renaming {file}: {str(e)}")
