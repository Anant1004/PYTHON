import os

directory = "C:/Users/anant/Desktop/ind"
files = os.listdir(directory)
i = 1

for file in files:
    if file.endswith(".mp4"):
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, f"{i}.mp4")
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {file} to {i}..mp4")
            i += 1
        except Exception as e:
            print(f"Error renaming {file}: {str(e)}")
