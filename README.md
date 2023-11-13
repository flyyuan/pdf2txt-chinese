# pdf2txt-chinese

## English

### Description
`pdf2txt-chinese` is a Python script created to extract text from each page of a PDF file and consolidate it into a single text file. Its development was inspired by the need to convert photocopied books into text format, to be used as a knowledge base for AI models like GPTs. This tool is especially effective for processing scanned documents or PDFs that contain text in image format. It supports text recognition in both English and Simplified Chinese.

### Dependencies
- Python
- PyPDF2
- pdf2image
- Pillow (PIL Fork)
- pytesseract
- Tesseract OCR

### Installation
1. **Python**: Ensure Python is installed on your system. If not, download and install it from [python.org](https://www.python.org/).
2. **Libraries**: Install the required Python libraries by running:
   ```bash
   pip install PyPDF2 pdf2image Pillow pytesseract
   ```
3. **Tesseract OCR**: Install Tesseract OCR and its dependencies, including language support for English and Chinese, with these commands:
   ```bash
   sudo apt install tesseract-ocr
   sudo apt install libtesseract-dev
   sudo apt-get install tesseract-ocr-chi-sim
   ```

### Usage
Run the script in a Python environment, specifying the path to your PDF file in the script. The script processes each page and outputs the extracted text to `extracted_text.txt`.

---

## 中文

### 用途说明
`pdf2txt-chinese` 是一个旨在将PDF文件的每一页文本提取并汇总到一个文本文件中的Python脚本。该项目的灵感来源于将影印版图书转换为文本格式，以供AI模型如GPTs使用作为知识库。该工具对于处理扫描文档或包含图像格式文本的PDF特别有效。支持英文和简体中文的文本识别。

### 依赖安装
- Python
- PyPDF2
- pdf2image
- Pillow（PIL Fork）
- pytesseract
- Tesseract OCR

### 安装说明
1. **Python**：确保系统已安装Python。如果没有，请从[python.org](https://www.python.org/)下载并安装。
2. **库安装**：通过以下命令安装所需的Python库：
   ```bash
   pip install PyPDF2 pdf2image Pillow pytesseract
   ```
3. **Tesseract OCR**：使用以下命令安装Tesseract OCR及其依赖项，包括英文和中文的语言支持：
   ```bash
   sudo apt install tesseract-ocr
   sudo apt install libtesseract-dev
   sudo apt-get install tesseract-ocr-chi-sim
   ```

### 使用方法
在Python环境中运行脚本，脚本中需指定PDF文件的路径。脚本将处理每一页，并将提取的文本输出到`extracted_text.txt`。
