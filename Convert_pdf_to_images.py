import fitz
import os

dpi = 300
zoom = dpi/72
magnify = fitz.Matrix(zoom, zoom)

path = "114-10174.pdf"
count = 0

doc = fitz.open(path)

for page in doc:
    count+=1
    pix = page.get_pixmap(matrix=magnify)
    pix.save(f"./image/114_{count}.png")