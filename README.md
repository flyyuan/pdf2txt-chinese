# pdf2txt-chinese

colab:
https://colab.research.google.com/drive/1ejSaK_-Y-_bI1IkVZbHDNGKJ79p30Xzm?usp=sharing

## 中文

### 用途说明
`pdf2txt-chinese` 是一个Python脚本，用于将PDF文件的每一页文本提取并汇总到一个文本文件中。该项目灵感来源于将影印版图书转换为文本格式，用作AI模型如GPTs的知识库。该工具特别适用于处理扫描文档或包含图像格式文本的PDF，支持英文和简体中文的文本识别。为了提升处理性能，脚本采用了多线程技术，并通过合理利用系统资源来优化处理速度和效率。

### 依赖安装
- Python
- PyPDF2
- pdf2image
- Pillow（PIL Fork）
- pytesseract
- tqdm（用于进度条）
- Tesseract OCR

### 安装说明
1. **Python**：确保系统已安装Python。如果没有，请从[python.org](https://www.python.org/)下载并安装。
2. **库安装**：通过以下命令安装所需的Python库：
   ```bash
   pip install PyPDF2 pdf2image Pillow pytesseract tqdm
   ```
3. **Tesseract OCR**：使用以下命令安装Tesseract OCR及其依赖项，包括英文和中文的语言支持：
   ```bash
   sudo apt install tesseract-ocr
   sudo apt install libtesseract-dev
   sudo apt-get install tesseract-ocr-chi-sim
   ```

### 使用方法
在Python环境中运行脚本，脚本中需指定PDF文件的路径。脚本将使用多线程处理每一页，并将提取的文本输出到`extracted_text.txt`，同时显示进度条并将识别到的文本打印到控制台。

---

## English

### Description
`pdf2txt-chinese` is a Python script designed to extract text from each page of a PDF file and consolidate it into a single text file. Inspired by the need to convert photocopied books into text format for use as a knowledge base for AI models like GPTs, this tool is particularly effective for scanned documents or PDFs containing text in image format. It supports text recognition in both English and Simplified Chinese. The script has been optimized for performance using multi-threading, effectively utilizing system resources to enhance processing speed and efficiency.

### Dependencies
- Python
- PyPDF2
- pdf2image
- Pillow (PIL Fork)
- pytesseract
- tqdm (for progress bar)
- Tesseract OCR

### Installation
1. **Python**: Ensure Python is installed on your system. If not, download and install it from [python.org](https://www.python.org/).
2. **Libraries**: Install the required Python libraries by running:
   ```bash
   pip install PyPDF2 pdf2image Pillow pytesseract tqdm
   ```
3. **Tesseract OCR**: Install Tesseract OCR and its dependencies, including language support for English and Chinese, with these commands:
   ```bash
   sudo apt install tesseract-ocr
   sudo apt install libtesseract-dev
   sudo apt-get install tesseract-ocr-chi-sim
   ```

### Usage
Run the script in a Python environment, specifying the path to your PDF file in the script. The script processes each page using multiple threads and outputs the extracted text to `extracted_text.txt`, while also displaying a progress bar and printing the recognized text to the console.
