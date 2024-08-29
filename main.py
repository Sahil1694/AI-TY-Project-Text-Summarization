import PyPDF2

# Open the PDF file
with open('Application.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)  # Use PdfReader instead of PdfFileReader
    number_of_pages = len(reader.pages)
    
    # Create a new text file to save the extracted text
    with open('output.txt', 'w') as text_file:
        # Loop through each page in the PDF
        for page_num in range(number_of_pages):
            # Get the text from the page
            page = reader.pages[page_num]
            text = page.extract_text()
            
            # Write the text to the text file
            text_file.write(f'Page {page_num + 1}')
            text_file.write(text)
            text_file.write('\n' + '-'*40 + '\n')  # Separator between pages

print("PDF content has been written to output.txt")
