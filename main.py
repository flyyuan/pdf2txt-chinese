import pytesseract
from pdf2image import convert_from_path
from PIL import ImageOps
from PyPDF2 import PdfReader
from concurrent.futures import ThreadPoolExecutor

def get_num_pages(pdf_path):
    reader = PdfReader(pdf_path)
    return len(reader.pages)

def process_page(pdf_path, page_number):
    images = convert_from_path(pdf_path, dpi=300, first_page=page_number, last_page=page_number)
    image = images[0]
    gray_image = ImageOps.grayscale(image)
    text = pytesseract.image_to_string(gray_image, lang='chi_sim+eng')
    print(text)
    return text

def extract_text_from_pdf(pdf_path):
    num_pages = get_num_pages(pdf_path)
    all_text = ""

    with ThreadPoolExecutor() as executor:
        # Process each page in parallel
        results = executor.map(lambda page: process_page(pdf_path, page), range(1, num_pages + 1))

    for result in results:
        all_text += result + "\n"

    return all_text

# Specify the path to your PDF file
pdf_path = 'a.pdf'  # Replace with your PDF file path

# Extract text from all pages
extracted_text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a single TXT file
with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print("Text extraction and saving complete.")
