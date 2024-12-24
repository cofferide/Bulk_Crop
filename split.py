import os
import shutil
from sklearn.model_selection import train_test_split

image_folder = r"C:\Users\SHEIKH NAIM\Desktop\Dataset\Split"
file_list = os.listdir(image_folder)
jpg_files = [file for file in file_list if file.endswith('.jpg')]

save_train = r"C:\Users\SHEIKH NAIM\Desktop\Dataset\Train"
save_test = r"C:\Users\SHEIKH NAIM\Desktop\Dataset\Test"
save_validation = r"C:\Users\SHEIKH NAIM\Desktop\Dataset\Validation"
save_folders = [save_train, save_test, save_validation]

for folders in save_folders:
    try:
        os.mkdir(folders)
        print(f"Directory '{folders}' created successfully.")
    except FileExistsError:
        print(f"Directory '{folders}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{folders}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# 60% training
train_files, temp_files = train_test_split(jpg_files, test_size=0.4, random_state=42)
# 20% validation, 20% test
validation_files, test_files = train_test_split(temp_files, test_size=0.5, random_state=42)

# Move files to the corresponding folders
for file in train_files:
    src_path = os.path.join(image_folder, file)
    dest_path = os.path.join(save_train, file)
    shutil.move(src_path, dest_path)

for file in validation_files:
    src_path = os.path.join(image_folder, file)
    dest_path = os.path.join(save_validation, file)
    shutil.move(src_path, dest_path)

for file in test_files:
    src_path = os.path.join(image_folder, file)
    dest_path = os.path.join(save_test, file)
    shutil.move(src_path, dest_path)

print(f"Data split into training folder: {save_train}, validation folder: {save_validation}, and test folder {save_test}.")