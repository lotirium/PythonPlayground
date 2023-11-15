import sys
import os
from PIL import Image

folder_name = sys.argv[1]
new_folder_name = sys.argv[2]

if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)

for filename in os.listdir(folder_name):
    img = Image.open(os.path.join(folder_name, filename))
    base_filename, file_extension = os.path.splitext(filename)
    save_path = os.path.join(new_folder_name, base_filename + '.png')
    img.save(save_path, 'png')
    print(f'Сonverted {filename} to PNG')

print('All done')
