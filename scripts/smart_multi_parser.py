import os
import re
import pandas as pd

input_folder = "data_raw/extracted_texts"
output_folder = "extracted_data"

os.makedirs(output_folder, exist_ok=True)

sector_keywords = [
    "IT", "BFSI", "CORE", "Core", "Analytics",
    "ITES", "Product", "Consulting", "Service"
]

for txtfile in os.listdir(input_folder):

    if txtfile.endswith(".txt"):

        file_path = os.path.join(input_folder, txtfile)
        records = []

        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()

            if re.match(r'^\d+', line):

                parts = line.split()

                try:
                    sector_index = None

                    for i, p in enumerate(parts):
                        if p in sector_keywords:
                            sector_index = i
                            break

                    if sector_index is None:
                        # fallback: detect first decimal number as CTC
                        for i, p in enumerate(parts):
                            if re.match(r'^\d+\.\d+$', p):
                                sector_index = i - 1
                                break

                    if sector_index is None or sector_index < 2:
                        continue

                    company_name = " ".join(parts[1:sector_index-1])
                    stipend_raw = parts[sector_index-1]
                    sector = parts[sector_index]
                    ctc = float(parts[sector_index+1]) if sector_index+1 < len(parts) else float(parts[sector_index])
                    total_offers = int(parts[-1])

                    records.append([company_name, stipend_raw, sector, ctc, total_offers])

                except:
                    continue

        df = pd.DataFrame(records, columns=["Company", "StipendRaw", "Sector", "CTC_LPA", "Offers"])

        save_name = txtfile.replace(".txt", ".csv")
        save_path = os.path.join(output_folder, save_name)

        df.to_csv(save_path, index=False)

        print(f"Parsed -> {save_name} | Rows: {len(df)}")

print("Universal smart brochure parsing completed successfully.")