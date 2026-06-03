import os
from pathlib import Path

ROOT_DIR = r"C:\\"  # zmień na np. D:\\ jeśli chcesz inny dysk
TOP_N = 30

largest_files = []

for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        try:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)

            largest_files.append((size, full_path))

            # Trzymaj tylko największe TOP_N plików
            if len(largest_files) > TOP_N * 5:
                largest_files.sort(reverse=True)
                largest_files = largest_files[:TOP_N]

        except (PermissionError, FileNotFoundError, OSError):
            pass

largest_files.sort(reverse=True)
largest_files = largest_files[:TOP_N]

print(f"\nTOP {TOP_N} największych plików:\n")
for i, (size, path) in enumerate(largest_files, start=1):
    print(f"{i:2}. {size / (1024**3):8.2f} GB  {path}")
