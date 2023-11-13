import easyocr
import pdf2image
from PyPDF2 import PdfReader
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import os
import numpy as np

def get_num_pages(pdf_path):
    reader = PdfReader(pdf_path)
    return len(reader.pages)

def process_pages(pdf_path, page_numbers):
    reader = easyocr.Reader(['en', 'ch_sim'], gpu=True)
    images = pdf2image.convert_from_path(pdf_path, dpi=250, first_page=page_numbers[0], last_page=page_numbers[-1])
    text_pages = {}

    for i, image in enumerate(images, start=page_numbers[0]):
        # Convert PIL Image to numpy array
        np_image = np.array(image)
        result = reader.readtext(np_image)
        text = ' '.join([res[1] for res in result])
        print(f"\nPage {i} Text:\n{text}")  # Print recognized text
        text_pages[i] = text + "\n"

    return text_pages

def extract_text_from_pdf(pdf_path, num_pages, batch_size=5):
    all_text_pages = {}
    max_workers = os.cpu_count() or 4

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for start_page in range(1, num_pages + 1, batch_size):
            page_numbers = list(range(start_page, min(start_page + batch_size, num_pages + 1)))
            futures.append(executor.submit(process_pages, pdf_path, page_numbers))

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Pages"):
            all_text_pages.update(future.result())

    all_text = "".join(all_text_pages[i] for i in sorted(all_text_pages))
    return all_text

pdf_path = '/content/drive/MyDrive/信息技术导论_14190358.pdf'  # Replace with your PDF file path
num_pages = get_num_pages(pdf_path)
extracted_text = extract_text_from_pdf(pdf_path, num_pages)

with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print("Text extraction and saving complete.")
