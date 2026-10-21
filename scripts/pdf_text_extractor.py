import pdfplumber

def extract_text_from_pdf(pdf_path):
    text_data = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_data += page.extract_text() + "\n"

    return text_data


if __name__ == "__main__":
    pdf_path = "data_raw/Placement-Statistics-for-Batch-2025.pdf"
    
    text = extract_text_from_pdf(pdf_path)

    with open("data_raw/extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Text extracted successfully.")