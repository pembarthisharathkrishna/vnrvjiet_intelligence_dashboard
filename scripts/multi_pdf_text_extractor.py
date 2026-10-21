import pdfplumber
import os

input_folder = "data_raw/auto_downloaded"
output_folder = "data_raw/extracted_texts"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):

    if filename.lower().endswith(".pdf"):

        pdf_path = os.path.join(input_folder, filename)
        text_data = ""

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text_data += extracted + "\n"

        txt_name = filename.replace(".pdf", ".txt")
        txt_path = os.path.join(output_folder, txt_name)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text_data)

        print(f"Extracted -> {txt_name}")

print("Multi PDF text extraction completed successfully.")