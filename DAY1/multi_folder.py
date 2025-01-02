import os

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


# Call the function with the base directory and number of days
create_folder(base_dir, dir_count, folder_name)

