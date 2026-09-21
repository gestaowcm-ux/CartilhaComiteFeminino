# -*- coding: utf-8 -*-
import os
import pypdf

reader = pypdf.PdfReader('CARTILHA_Proposta 2.pdf')
print("Total PDF pages:", len(reader.pages))

for idx, p in enumerate(reader.pages):
    txt = p.extract_text()
    first_line = txt.split('\n')[0] if txt else ''
    imgs = list(p.images.keys())
    if imgs or 'sugest' in txt.lower() or 'imagem' in txt.lower():
        print(f"Page {idx+1}: Images={imgs} | Text sample: {txt[:120].strip().replace(chr(10), ' ')}")
