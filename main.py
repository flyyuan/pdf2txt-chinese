import pytesseract
from pdf2image import convert_from_path
from PIL import ImageOps
from PyPDF2 import PdfReader
from concurrent.futures import ThreadPoolExecutor

def get_num_pages(pdf_path):
    reader = PdfReader(pdf_path)
    return len(reader.pages)

def process_pages(pdf_path, start_page, end_page):
    images = convert_from_path(pdf_path, dpi=250, first_page=start_page, last_page=end_page)
    text = ""

    for image in images:
        gray_image = ImageOps.grayscale(image)
        text += pytesseract.image_to_string(gray_image, lang='chi_sim+eng') + "\n"
    print(text)    
    return text

def extract_text_from_pdf(pdf_path, num_pages, batch_size=5):
    all_text = ""
    with ThreadPoolExecutor(max_workers=8) as executor:  # Adjust max_workers based on your CPU
        futures = []
        for start_page in range(1, num_pages + 1, batch_size):
            end_page = min(start_page + batch_size - 1, num_pages)
            futures.append(executor.submit(process_pages, pdf_path, start_page, end_page))

        for future in futures:
            all_text += future.result()

    return all_text

pdf_path = 'a.pdf'  # Replace with your PDF file path
num_pages = get_num_pages(pdf_path)
extracted_text = extract_text_from_pdf(pdf_path, num_pages)

with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print("Text extraction and saving complete.")
