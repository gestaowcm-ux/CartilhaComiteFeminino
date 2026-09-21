# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
p1 = re.search(r'id="page-1".*?<img src="([^"]+)"', content, re.DOTALL)
p19 = re.search(r'id="page-19".*?<img src="([^"]+)"', content, re.DOTALL)

print("Page 1 (Capa):", p1.group(1) if p1 else "Not found")
print("Page 19 (Contracapa):", p19.group(1) if p19 else "Not found")

assert p1.group(1) == 'ChatGPT Image Aug 31, 2026, 07_59_24 PM.png', "Capa incorreta!"
assert p19.group(1) == 'ChatGPT Image Aug 30, 2026, 10_42_56 AM.png', "Contracapa incorreta!"
print("\n>>> SUCESSO: Capa e Contracapa verificadas e corretas!")
