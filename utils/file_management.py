import os
import shutil

def create_excel_copy(src_file_path, dest_folder_path):
    # Extract file name and extension
    filename, ext = os.path.splitext(os.path.basename(src_file_path))

    # Create a counter to append to filename if it already exists
    count = 1

    # Copy file to destination folder
    while True:
        # Construct destination file path with counter, if necessary
        dest_file_path = os.path.join(dest_folder_path, filename + f'_{count}' + ext)
        
        if not os.path.exists(dest_file_path):
            shutil.copy(src_file_path, dest_file_path)
            print(f'File copied to {dest_file_path}')
            return dest_file_path

        count += 1
