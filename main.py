import pytesseract
from pdf2image import convert_from_path
from PIL import ImageOps
from PyPDF2 import PdfReader
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import os
import psutil

def get_num_pages(pdf_path):
    reader = PdfReader(pdf_path)
    return len(reader.pages)

def process_pages(pdf_path, start_page, end_page):
    images = convert_from_path(pdf_path, dpi=300, first_page=start_page, last_page=end_page)
    text_pages = {}

    for i, image in enumerate(images, start=start_page):
        gray_image = ImageOps.grayscale(image)
        text = pytesseract.image_to_string(gray_image, lang='chi_sim+eng')
        print(f"\nPage {i} Text:\n{text}")  # Print recognized text
        text_pages[i] = text + "\n"

    return text_pages

def extract_text_from_pdf(pdf_path, num_pages):
    all_text_pages = {}
    max_workers = os.cpu_count() or 4
    memory = psutil.virtual_memory()

    # Adjust batch_size based on available memory
    batch_size = max(1, int(memory.available / (500 * 1024 * 1024)))  # 500MB per batch

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for start_page in range(1, num_pages + 1, batch_size):
            end_page = min(start_page + batch_size - 1, num_pages)
            futures.append(executor.submit(process_pages, pdf_path, start_page, end_page))

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Pages"):
            all_text_pages.update(future.result())

    # Sort and concatenate the text
    all_text = "".join(all_text_pages[i] for i in sorted(all_text_pages))

    return all_text

pdf_path = 'a.pdf'  # Replace with your PDF file path
num_pages = get_num_pages(pdf_path)
extracted_text = extract_text_from_pdf(pdf_path, num_pages)

with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print("Text extraction and saving complete.")
