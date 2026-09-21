# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

checks = [
    'ChatGPT Image Aug 31, 2026, 07_59_24 PM.png', # Capa
    'ChatGPT Image Aug 30, 2026, 10_42_56 AM.png', # Contracapa
    'spread-container',
    'magazine-book',
    'magazine-page page-left',
    'magazine-page page-right',
    'spread-bottom-bar',
    'spread-dot',
    'toggleTTS',
    'toggleTOC',
    'Mensagem da Presidente da ABRAMAN',
    'Mensagem do Comitê Feminino',
    'Broken Rung',
    '20,9%',
    'Maternidade Atípica',
    'Barreiras Físicas',
    'Microagressões',
    'Homens como Aliados',
    'Palavras Finais',
    'Manifesto Institucional'
]

all_passed = True
for c in checks:
    present = c in content
    print(f'Checking "{c}": {"OK" if present else "MISSING"}')
    if not present:
        all_passed = False

print('\nTotal Status:', 'ALL PASSED!' if all_passed else 'SOME CHECKS FAILED')
