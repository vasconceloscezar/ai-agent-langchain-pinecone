import PyPDF2

# Open the PDF file in read-binary mode
pdf_file_obj = open("./memory/files/test.pdf", "rb")

# Create a PdfReader object to read the PDF file
pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Open the output TXT file in write mode
with open("output.txt", "w", encoding="utf-8") as txt_file:
    # Iterate through the pages of the PDF file
    for page_num in range(num_pages):
        # Get the page object
        page_obj = pdf_reader.pages[page_num]
        # Extract the text from the page object
        text = page_obj.extract_text()
        # Write the extracted text to the output TXT file
        txt_file.write(text)

# Close the PDF file object
pdf_file_obj.close()
