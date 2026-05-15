import os
from pypdf import PdfWriter

os.makedirs('tests/test_data', exist_ok=True)

# Generate a minimal valid PDF
writer = PdfWriter()
# adding a blank page is the easiest way to make a structurally valid PDF
writer.add_blank_page(width=200, height=200)

with open('tests/test_data/valid_doc.pdf', 'wb') as f:
    writer.write(f)

# Generate a corrupted PDF
with open('tests/test_data/corrupted_doc.pdf', 'wb') as f:
    f.write(b"This is definitely not a PDF file.")

print("Test files generated.")
