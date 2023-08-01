import cv2
import os

folder_path = "/path/folder"
output_folder = os.path.join(folder_path, "cropped")

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

print("Start")

for filename in os.listdir(folder_path):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        file_path = os.path.join(folder_path, filename)
        img = cv2.imread(file_path)
        height, width = img.shape[:2]

        size = 1920  // size

        x = (width - size) // 2
        y = (height - size) // 2
        cropped = img[y:y+size, x:x+size]
        new_filename = os.path.splitext(filename)[0] + '_cropped.png'
        new_file_path = os.path.join(output_folder, new_filename)
        cv2.imwrite(new_file_path, cropped)

print("Finish")
