import cv2
import os
from imgaug import augmenters as iaa
import random

image_folder = r"C:\Users\SHEIKH NAIM\Desktop\Dataset\Train"
file_list = os.listdir(image_folder)
jpg_files = [file for file in file_list if file.endswith('.jpg')]

save_path = r"C:\Users\SHEIKH NAIM\Desktop\Dataset\Augment"

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

    augmentations = [
        ("Horizontal Flip", iaa.Fliplr(0.5)),
        ("Vertical Flip", iaa.Flipud(0.5)),
        ("Gaussian Blur", iaa.GaussianBlur(sigma=(0, 5.0))),
        ("Brightness Multiplication", iaa.Multiply((0.0, 5.0))),
        ("Additive Gaussian Noise", iaa.AdditiveGaussianNoise(scale=(0, 50))),
    ]

    augmentation_name, augmentation = random.choice(augmentations)

    images = cv2.imread(image_path)
    augmented_image = augmentation(image=images)

    # Save augmented image
    file_name = os.path.basename(image_path)
    augmented_image_path = os.path.join(save_path, f"augmented_{augmentation_name}_{file_name}")
    cv2.imwrite(augmented_image_path, augmented_image)

print(f"Augmented images saved to folder: {save_path}.")
