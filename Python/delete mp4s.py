import os

# Specify the directory where you want to delete MP4 files
directory = 'C:/Users/Admin'

# Loop through the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.mp4'):
        file_path = os.path.join(directory, filename)
        try:
            os.remove(file_path)  # Delete the file
            print(f'Deleted: {file_path}')
        except Exception as e:
            print(f'Error deleting {file_path}: {e}')

print("Deletion completed!")
