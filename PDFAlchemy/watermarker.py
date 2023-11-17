import PyPDF2

with open('super.pdf', 'rb') as content_file, open('wtr.pdf', 'rb') as watermark_file:
    reader = PyPDF2.PdfReader(content_file)
    watermark = PyPDF2.PdfReader(watermark_file)
    output = PyPDF2.PdfWriter()

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        watermark_page = watermark.pages[0]
        page.merge_page(watermark_page)
        output.add_page(page)

    with open('watermarked_output.pdf', 'wb') as output_file:
        output.write(output_file)
