# JPG to PNG Converter

## Overview
This script, `JPGtoPNGconverter.py`, is designed to convert all JPEG images in a specified folder to PNG format and save them in a new directory. It's a simple and effective tool for batch image conversion.

## Requirements
- Python 3.x
- Pillow library

  To install Pillow, run: `pip install Pillow`

## Usage
To use this script, you need two arguments: the source folder containing JPG images and the destination folder for the converted PNG files. 

Example:
```
python JPGtoPNGconverter.py <source_folder> <destination_folder>
```

## How It Works
The script takes the source directory as an input, converts each JPEG image to PNG format, and saves them in the target directory. If the destination folder does not exist, it will be created automatically.

## Important Notes
- This script only processes files with a '.jpg' extension.
- Existing files in the destination folder will be overwritten if their names match the converted files.
