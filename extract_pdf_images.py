import fitz # PyMuPDF
import os

pdf_path = "/Users/mayank/.gemini/antigravity/brain/c5dc02b9-842d-452f-8c0f-b834765bdd46/.user_uploaded/media_1791299075472.pdf"
out_dir = "/Users/mayank/.gemini/antigravity/brain/c5dc02b9-842d-452f-8c0f-b834765bdd46/scratch/pdf_images"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
img_count = 0
for i in range(len(doc)):
    page = doc[i]
    images = page.get_images()
    for img in images:
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_name = f"page_{i+1}_img_{img_count}.{image_ext}"
        with open(os.path.join(out_dir, img_name), "wb") as f:
            f.write(image_bytes)
        img_count += 1
        print(f"Extracted {img_name}")

print(f"Extracted {img_count} images in total.")
