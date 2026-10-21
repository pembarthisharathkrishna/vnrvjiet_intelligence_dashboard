import re
import pandas as pd

input_file = "data_raw/extracted_text.txt"

records = []

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()

    # detect rows starting with serial number
    if re.match(r'^\d+', line):

        parts = line.split()

        try:
            serial_no = parts[0]

            # detect sector keywords
            sector_index = None
            for i, p in enumerate(parts):
                if p in ["IT", "BFSI", "Core", "CORE", "Analytics"]:
                    sector_index = i
                    break

            if sector_index is None:
                continue

            company_name = " ".join(parts[1:sector_index-1])
            stipend_raw = parts[sector_index-1]
            sector = parts[sector_index]
            ctc = float(parts[sector_index+1])

            total_offers = int(parts[-1])

            records.append([company_name, stipend_raw, sector, ctc, total_offers])

        except:
            continue

df = pd.DataFrame(records, columns=["Company", "StipendRaw", "Sector", "CTC_LPA", "Offers"])

df.to_csv("extracted_data/auto_parsed_2021_25.csv", index=False)

print(df.head(20))
print("Automatic placement parsing completed successfully.")