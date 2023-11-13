import pytesseract
from pdf2image import convert_from_path
from PIL import ImageOps
from PyPDF2 import PdfReader

def get_num_pages(pdf_path):
    # Open the PDF and determine the number of pages
    reader = PdfReader(pdf_path)
    return len(reader.pages)

def extract_text_from_pdf(pdf_path, num_pages):
    # Initialize an empty string to hold all text
    all_text = ""

    # Process each page
    for page_number in range(1, num_pages + 1):
        # Convert the specific PDF page to an image with higher DPI
        images = convert_from_path(pdf_path, dpi=300, first_page=page_number, last_page=page_number)

        # Assuming there's only one image since we're converting one page
        image = images[0]

        # Convert image to grayscale for better OCR accuracy
        gray_image = ImageOps.grayscale(image)

        # Apply OCR using Tesseract with Chinese and English language support
        text = pytesseract.image_to_string(gray_image, lang='chi_sim+eng')
        print(text)

        # Append the text of the current page to the all_text string
        all_text += text + "\n"

    return all_text

# Specify the path to your PDF file
pdf_path = 'a.pdf'  # Replace with your PDF file path

# Get the number of pages in the PDF
num_pages = get_num_pages(pdf_path)

# Extract text from all pages
extracted_text = extract_text_from_pdf(pdf_path, num_pages)

# Save the extracted text to a single TXT file
with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print("Text extraction and saving complete.")
