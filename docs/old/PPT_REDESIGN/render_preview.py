#!/usr/bin/env python3
# pptx -> pdf (LibreOffice) -> preview/NN.png (PyMuPDF)
import pathlib, subprocess, fitz

D = pathlib.Path(__file__).parent
PPTX = D / "Cloud_Alpacas_Presentation_Redesign.pptx"
PREV = D / "preview"; PREV.mkdir(exist_ok=True)
SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", str(D), str(PPTX)],
               check=True, capture_output=True)
pdf = D / (PPTX.stem + ".pdf")
doc = fitz.open(pdf)
zoom = 1920 / (13.333 * 72)
mat = fitz.Matrix(zoom, zoom)
for i, page in enumerate(doc, 1):
    page.get_pixmap(matrix=mat, alpha=False).save(str(PREV / f"{i:02d}.png"))
doc.close()
print(f"{len(list(PREV.glob('*.png')))} preview PNGs -> {PREV}")
