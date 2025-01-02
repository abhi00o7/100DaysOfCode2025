import os
import errno
# Define the base directory where folders will be created
base_dir = 'C:/Users/abhis/Projects/100DaysOfCode2025/'
dir_count = 100
folder_name = 'DAY'

# Create folders for as many days as you want


def create_folder(base_dir, count, folder_name):
    print(f'Creating {count} folders in {base_dir} with name {folder_name}')
    for index in range(1, count+1):
        print(f'Creating folder: {folder_name + str(index)}')
        f_name = folder_name + str(index)
        folder_path = os.path.join(base_dir, f_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f'Created folder: {folder_path}')
    print('All folders created successfully!')

# Call the function with the base directory and number of days


def delete_empty_folders(base_dir, count, folder_name):
    error_flag = False
    print(
        f'Deleting {count} empty folders in {base_dir} with name {folder_name}')
    for index in range(1, count+1):
        f_name = folder_name + str(index)
        folder_path = os.path.join(base_dir, f_name)
        try:
            os.rmdir(folder_path)
        except OSError as e:
            if e.errno == errno.ENOTEMPTY:
                print(f'Folder not empty: {folder_path}')
            elif e.errno == errno.ENOENT:
                print(f'Folder not found: {folder_path}')
            else:
                print(f'Error deleting folder: {folder_path}')
                print(f'Error: {e}')
                error_flag = True
    if error_flag:
        print('Some folders could not be deleted!')
    else:
        print('All empty folders deleted successfully!')


# Call the function with the base directory and number of days
create_folder(base_dir, dir_count, folder_name)

# Call the function with the base directory and number of days
# delete_empty_folders(base_dir, dir_count, folder_name)
