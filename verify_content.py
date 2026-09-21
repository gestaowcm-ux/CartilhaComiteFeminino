# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

checks = [
    'ChatGPT Image Aug 30, 2026, 10_42_56 AM.png',
    'ChatGPT Image Aug 31, 2026, 07_59_24 PM.png',
    'Mensagem da Presidente da ABRAMAN',
    'Mensagem do Comitê Feminino',
    'Capítulo 01',
    'Capítulo 02',
    'Capítulo 03',
    'Capítulo 04',
    'Capítulo 05',
    'Capítulo 06',
    'Capítulo 07',
    'Capítulo 08',
    'Capítulo 09',
    'Capítulo 10',
    'Capítulo 11',
    'Capítulo 12',
    'Capítulos 13',
    'Palavras Finais',
    'Broken Rung',
    '20,9%',
    'Maternidade Atípica',
    'Microagressões',
    'Homens como Aliados'
]

all_passed = True
for c in checks:
    present = c in content
    print(f'Checking "{c}": {"OK" if present else "MISSING"}')
    if not present:
        all_passed = False

print('\nTotal Status:', 'ALL PASSED!' if all_passed else 'SOME CHECKS FAILED')
