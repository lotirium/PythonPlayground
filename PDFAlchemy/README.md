# PDFAlchemy

PDFAlchemy is a Python toolkit for manipulating PDF files. It uses the `PyPDF2` library to provide various functionalities like merging PDFs, rotating pages, and adding watermarks.

## Features

- **Merge PDFs**: Combine multiple PDF files into one.
- **Rotate PDF**: Rotate the pages of a PDF file.
- **Watermark PDF**: Add a watermark to each page of a PDF file.

## Getting Started

### Prerequisites

- Python 3
- PyPDF2 (Install via `pip install PyPDF2`)

### Usage

#### Merge PDFs
- `python merge_pdf.py file1.pdf file2.pdf`
- Merges `file1.pdf` and `file2.pdf` into `super.pdf`.

#### Rotate PDF
- `python rotate_pdf.py`
- Rotates the first page of `dummy.pdf` by 90 degrees and saves it as `tilt.pdf`.

#### Watermark PDF
- `python watermarker.py`
- Adds the watermark from `wtr.pdf` to `super.pdf` and saves it as `watermarked_output.pdf`.

## Contributing

Feel free to fork, modify, and contribute to this project. Submit pull requests or open issues for any improvements or bug fixes.
