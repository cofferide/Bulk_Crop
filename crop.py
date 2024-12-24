import cv2
import os
import matplotlib.pyplot as plt

image_folder = r"C:\Users\SHEIKH NAIM\Desktop\Dataset"
file_list = os.listdir(image_folder)
jpg_files = [file for file in file_list if file.endswith('.jpg')]

save_path = r"C:\Users\SHEIKH NAIM\Desktop\Dataset\Split"

try:
    os.mkdir(save_path)
    print(f"Directory '{save_path}' created successfully.")
except FileExistsError:
    print(f"Directory '{save_path}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{save_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")

for jpg_file in jpg_files:
    image_path = os.path.join(image_folder, jpg_file)

    file_size_kb = os.path.getsize(image_path) / 1024  # Convert bytes to kilobytes
    if file_size_kb <= 1000:
        print(f"Skipping {jpg_file} as it is smaller than 1MB.")
        continue

    image = cv2.imread(image_path)
    height, width, _ = image.shape
    slice_height, slice_width = height // 2, width // 2

    sections = [
        ("q1", image[0:slice_height, 0:slice_width]),
        ("q2", image[0:slice_height, slice_width:width]),
        ("q3", image[slice_height:height, 0:slice_width]),
        ("q4", image[slice_height:height, slice_width:width])
    ]

    '''
    plt.figure(figsize=(5, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(q1, cv2.COLOR_BGR2RGB))
    plt.title("Top_Left")

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(q2, cv2.COLOR_BGR2RGB))
    plt.title("Top_Right")

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(q3, cv2.COLOR_BGR2RGB))
    plt.title("Bot_Right")

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(q4, cv2.COLOR_BGR2RGB))
    plt.title("Bot_Left")

    plt.tight_layout()
    plt.draw()
    # Wait for a key press and check if the key is '0'
    if plt.waitforbuttonpress():
        if plt.get_current_fig_manager().toolbar.mode == 'x':
            plt.close()
    '''
    for section_name, cropped_image in sections:
        file_name = os.path.splitext(jpg_file)[0]
        augmented_image_path = os.path.join(save_path, f"{file_name}_{section_name}.jpg")
        cv2.imwrite(augmented_image_path, cropped_image)

print(f"Images saved to {save_path}")