import pandas as pd
from bs4 import BeautifulSoup

# === 1. INPUT: HTML source ===
# Option A: local saved HTML file
input_file = "input.html"

with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Option B (alternative): use a URL instead
# import requests
# html = requests.get("https://example.com").text

# === 2. PARSE HTML ===
soup = BeautifulSoup(html, "html.parser")

# Find first table (can be adjusted if needed)
table = soup.find("table")

# === 3. EXTRACT DATA ===
rows = table.find_all("tr")

data = []

for row in rows:
    cols = row.find_all(["td", "th"])  # handles headers too
    values = [col.get_text(strip=True) for col in cols]

    if values:
        data.append(values)

# === 4. CREATE DATAFRAME ===
df = pd.DataFrame(data)

# Optional: set first row as header
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# === 5. CLEAN DATA (optional) ===
# Remove non-numeric characters from numeric columns if needed
for col in df.columns:
    df[col] = df[col].astype(str)

# === 6. EXPORT TO EXCEL ===
output_file = "output.xlsx"
df.to_excel(output_file, index=False)

print(f"Excel file created: {output_file}")
