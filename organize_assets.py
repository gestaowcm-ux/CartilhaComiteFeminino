# -*- coding: utf-8 -*-
import shutil, os

os.makedirs('assets', exist_ok=True)

# Copy and rename docx extracted images to assets
mappings = {
    'extracted_images/docx_img_4.jpeg': 'assets/img_cap2_diversidade.jpg',
    'extracted_images/docx_img_2.png': 'assets/img_cap3_manutencao.png',
    'extracted_images/docx_img_1.png': 'assets/img_cap3_mensagem.png',
    'extracted_images/docx_img_0.jpeg': 'assets/img_cap7_maternidade_1.jpg',
    'extracted_images/docx_img_6.jpeg': 'assets/img_cap7_maternidade_2.jpg',
    'extracted_images/docx_img_5.jpeg': 'assets/img_cap8_maternidade_atipica_1.jpg',
    'extracted_images/docx_img_3.jpeg': 'assets/img_cap8_maternidade_atipica_2.jpg',
}

for src, dst in mappings.items():
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {src} -> {dst}")

print("Assets organized successfully!")
