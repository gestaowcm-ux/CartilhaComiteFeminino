#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script construtor para a Cartilha & Revista Digital em Modo Leitura A4 (Print/PDF)
Comitê Feminino ABRAMAN
Gera 'print_magazine.html' e compila 'Cartilha Comitê Feminino ABRAMAN.pdf' na raiz.
"""

import os
import subprocess

def build_a4_magazine():
    print("Iniciando geração do Modo Leitura A4...")

    css = """
    :root {
        --abraman-navy: #0B192C;
        --abraman-blue: #1E3A8A;
        --abraman-cyan: #0284C7;
        --rose-accent: #E11D48;
        --rose-light: #FFF1F2;
        --rose-border: #FECDD3;
        --text-dark: #0F172A;
        --text-body: #334155;
        --text-muted: #64748B;
        --bg-light: #F8FAFC;
        --gold-accent: #D97706;
    }

    @page {
        size: 210mm 297mm;
        margin: 0mm !important;
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
    }

    html, body {
        margin: 0 !important;
        padding: 0 !important;
        width: 210mm !important;
        background: #EAEEF3;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: var(--text-dark);
        -webkit-font-smoothing: antialiased;
    }

    /* Container de cada Página A4 */
    .a4-page {
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        min-height: 297mm !important;
        page-break-after: always !important;
        break-after: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        position: relative !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
        background: #FFFFFF !important;
        margin: 0 auto 10mm auto;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }

    @media print {
        body {
            background: #FFFFFF !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        .a4-page {
            margin: 0 !important;
            box-shadow: none !important;
        }
        .no-print-bar {
            display: none !important;
        }
        .page-wrapper {
            padding: 0 !important;
            margin: 0 !important;
        }
    }

    @media screen {
        .page-wrapper {
            padding-top: 60px;
            padding-bottom: 30px;
        }
    }

    /* Capa e Contracapa Full-Bleed */
    .a4-page.full-bleed {
        padding: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
        background: #000000 !important;
    }

    .a4-page.full-bleed img {
        width: 210mm !important;
        height: 297mm !important;
        object-fit: fill !important;
        display: block !important;
    }

    /* Páginas de Conteúdo Editorial A4 */
    .a4-page.content-page {
        padding: 14mm 16mm 12mm 16mm !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
    }

    /* Cabeçalho Editorial Superior */
    .page-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1.5px solid #E2E8F0;
        padding-bottom: 2.5mm;
        margin-bottom: 4mm;
    }

    .page-header-left {
        display: flex;
        align-items: center;
        gap: 2.5mm;
    }

    .chapter-pill {
        background: var(--rose-accent);
        color: white;
        font-size: 8pt;
        font-weight: 700;
        padding: 1mm 2.8mm;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .chapter-category {
        font-size: 8.5pt;
        font-weight: 600;
        color: var(--abraman-blue);
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    .page-header-right {
        font-size: 8pt;
        color: var(--text-muted);
        font-weight: 500;
    }

    /* Título do Capítulo */
    .chapter-title-group {
        margin-bottom: 3.5mm;
    }

    .chapter-badge-top {
        display: inline-block;
        font-size: 8pt;
        font-weight: 700;
        color: var(--rose-accent);
        text-transform: uppercase;
        letter-spacing: 0.6px;
        margin-bottom: 1mm;
    }

    .chapter-main-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 17pt;
        font-weight: 800;
        color: var(--abraman-navy);
        line-height: 1.25;
        letter-spacing: -0.3px;
    }

    .chapter-subtitle {
        font-size: 9.5pt;
        font-weight: 600;
        color: var(--rose-accent);
        margin-top: 1mm;
    }

    /* Lead Editorial */
    .editorial-lead {
        font-size: 9.5pt;
        line-height: 1.55;
        color: var(--text-body);
        margin-bottom: 3.5mm;
        text-align: justify;
    }

    .editorial-lead strong {
        color: var(--abraman-navy);
    }

    .editorial-body-p {
        font-size: 9pt;
        line-height: 1.5;
        color: var(--text-body);
        margin-bottom: 3mm;
        text-align: justify;
    }

    /* Caixas Editoriais */
    .editorial-box {
        border-radius: 6px;
        padding: 3mm 4mm;
        margin-bottom: 3mm;
        box-sizing: border-box;
    }

    .box-title {
        font-size: 9pt;
        font-weight: 700;
        margin-bottom: 1.5mm;
        display: flex;
        align-items: center;
        gap: 2mm;
    }

    /* Caixa Para Refletir */
    .box-reflection {
        background: #FEF3C7;
        border-left: 3.5px solid #D97706;
        color: #78350F;
    }

    .box-reflection .box-title {
        color: #92400E;
    }

    /* Caixa Boas Práticas */
    .box-practices {
        background: #F0FDF4;
        border-left: 3.5px solid #16A34A;
        color: #166534;
    }

    .box-practices .box-title {
        color: #15803D;
    }

    /* Caixa Mensagem-Chave */
    .box-quote {
        background: var(--rose-light);
        border-left: 3.5px solid var(--rose-accent);
        color: #881337;
    }

    .box-quote .box-title {
        color: #9F1239;
    }

    /* Caixa Conceitual / Info */
    .box-info {
        background: #F0F9FF;
        border-left: 3.5px solid var(--abraman-cyan);
        color: #0369A1;
    }

    .box-info .box-title {
        color: #0284C7;
    }

    /* Grids e Colunas */
    .grid-2-col {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3.5mm;
        margin-bottom: 3mm;
    }

    .grid-3-col {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 2.5mm;
        margin-bottom: 3mm;
    }

    .grid-4-col {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 2mm;
        margin-bottom: 3mm;
    }

    /* Cards de Conceitos */
    .concept-card {
        background: var(--bg-light);
        border: 1px solid #E2E8F0;
        border-radius: 6px;
        padding: 2.5mm 3mm;
    }

    .concept-card-header {
        display: flex;
        align-items: center;
        gap: 2mm;
        margin-bottom: 1mm;
    }

    .concept-num {
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: var(--abraman-blue);
        color: white;
        font-size: 7.5pt;
        font-weight: 700;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .concept-title {
        font-size: 8.5pt;
        font-weight: 700;
        color: var(--abraman-navy);
    }

    .concept-desc {
        font-size: 8pt;
        line-height: 1.35;
        color: var(--text-body);
    }

    /* Imagens Editoriais A4 */
    .editorial-img-container {
        border-radius: 6px;
        overflow: hidden;
        border: 1px solid #CBD5E1;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        background: #0F172A;
    }

    .editorial-img-container img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
    }

    .editorial-img-caption {
        font-size: 7.5pt;
        color: var(--text-muted);
        background: #F8FAFC;
        padding: 1.5mm 3mm;
        border-top: 1px solid #E2E8F0;
        font-style: italic;
    }

    /* Rodapé Editorial */
    .page-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 1.5px solid #E2E8F0;
        padding-top: 2.5mm;
        margin-top: auto;
    }

    .footer-left {
        font-size: 8pt;
        font-weight: 600;
        color: var(--abraman-blue);
        letter-spacing: 0.3px;
    }

    .footer-center {
        font-size: 7.5pt;
        color: var(--text-muted);
    }

    .footer-page-num {
        font-size: 9pt;
        font-weight: 800;
        color: var(--rose-accent);
        background: var(--rose-light);
        padding: 0.8mm 2.8mm;
        border-radius: 4px;
        border: 1px solid var(--rose-border);
    }

    /* Listas com Marcadores */
    ul.editorial-list {
        list-style: none;
        padding: 0;
        margin: 1.5mm 0;
    }

    ul.editorial-list li {
        font-size: 8.5pt;
        line-height: 1.45;
        color: var(--text-body);
        position: relative;
        padding-left: 4.5mm;
        margin-bottom: 1.5mm;
    }

    ul.editorial-list li::before {
        content: "■";
        position: absolute;
        left: 0;
        color: var(--rose-accent);
        font-size: 6pt;
        top: 0.5mm;
    }

    /* Barra de Ação Superior na Web */
    .no-print-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 50px;
        background: #0B192C;
        color: white;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        z-index: 9999;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }

    .print-btn {
        background: var(--rose-accent);
        color: white;
        border: none;
        padding: 8px 18px;
        border-radius: 6px;
        font-weight: 700;
        cursor: pointer;
        font-size: 13px;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: background 0.2s;
    }

    .print-btn:hover {
        background: #BE123C;
    }
    """

    pages = []

    # ==========================================
    # PÁGINA 01: CAPA OFICIAL (Full-Bleed)
    # ==========================================
    pages.append("""
    <!-- PÁGINA 01: CAPA -->
    <div class="a4-page full-bleed">
        <img src="ChatGPT Image Aug 31, 2026, 07_59_24 PM.png" alt="Capa Oficial - Cartilha Comitê Feminino ABRAMAN">
    </div>
    """)

    # ==========================================
    # PÁGINA 02: MENSAGENS INSTITUCIONAIS
    # ==========================================
    pages.append("""
    <!-- PÁGINA 02: MENSAGENS INSTITUCIONAIS -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Institucional</span>
                    <span class="chapter-category">Comitê Feminino ABRAMAN</span>
                </div>
                <div class="page-header-right">Abertura Oficial</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Compromisso com o Futuro</span>
                <h1 class="chapter-main-title">Mensagens Institucionais</h1>
                <p class="chapter-subtitle">Liderança, Equidade e Transformação na Gestão de Ativos</p>
            </div>

            <!-- Mensagem Presidente -->
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid var(--abraman-blue); border-radius: 6px; padding: 3.5mm 4.5mm; margin-bottom: 4mm;">
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2mm;">
                    <h3 style="font-size: 10.5pt; font-weight: 800; color: var(--abraman-navy); margin: 0;">Mensagem da Presidente da ABRAMAN</h3>
                    <span style="font-size: 8pt; font-weight: 700; color: var(--abraman-blue);">Diretoria Executiva</span>
                </div>
                <p class="editorial-body-p" style="margin-bottom: 2mm;">
                    A Associação Brasileira de Manutenção e Gestão de Ativos (ABRAMAN) tem a honra de apresentar esta Cartilha, fruto do dedicado trabalho do nosso <strong>Comitê Feminino</strong> e do <strong>Subcomitê DIA</strong> (Diversidade, Inclusão e Acessibilidade).
                </p>
                <p class="editorial-body-p" style="margin-bottom: 2mm;">
                    Acreditamos firmemente que o avanço técnico da engenharia brasileira caminha lado a lado com a valorização do capital humano. Promover a diversidade de gênero não é apenas um imperativo ético e social, mas uma estratégia indispensável para a sustentabilidade, segurança operacional e excelência competitiva das nossas indústrias.
                </p>
                <p style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy); text-align: right; margin: 0;">
                    — Paula Granha, Presidente da ABRAMAN
                </p>
            </div>

            <!-- Mensagem Comitê Feminino -->
            <div style="background: var(--rose-light); border: 1px solid var(--rose-border); border-left: 4px solid var(--rose-accent); border-radius: 6px; padding: 3.5mm 4.5mm; margin-bottom: 4mm;">
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2mm;">
                    <h3 style="font-size: 10.5pt; font-weight: 800; color: #9F1239; margin: 0;">Mensagem do Comitê Feminino & Subcomitê DIA</h3>
                    <span style="font-size: 8pt; font-weight: 700; color: var(--rose-accent);">Gestão 2026-2028</span>
                </div>
                <p class="editorial-body-p" style="margin-bottom: 2mm; color: #881337;">
                    Historicamente vistos como ambientes estritamente masculinos, os setores de manutenção, confiabilidade e gestão de ativos vivem uma profunda e necessária transformação. As mulheres estão ocupando postos técnicos, operacionais e de liderança, agregando competência, inovação e novas perspectivas na resolução de problemas complexos.
                </p>
                <p class="editorial-body-p" style="margin-bottom: 2mm; color: #881337;">
                    Esta cartilha foi concebida como um <em>Guia Prático</em> para apoiar líderes, profissionais e organizações na construção de ambientes seguros, inclusivos e inspiradores. Convidamos você a refletir, disseminar e aplicar estas boas práticas no seu dia a dia.
                </p>
                <p style="font-size: 8.5pt; font-weight: 700; color: #9F1239; text-align: right; margin: 0;">
                    — Coordenação do Comitê Feminino ABRAMAN
                </p>
            </div>

            <!-- Destaque em 3 Pilares -->
            <div class="grid-3-col" style="margin-top: 2mm;">
                <div class="concept-card" style="text-align: center; background: #FFFFFF; border-top: 3px solid var(--abraman-blue);">
                    <div style="font-size: 13pt; font-weight: 900; color: var(--abraman-navy); margin-bottom: 1mm;">INCLUSÃO</div>
                    <p style="font-size: 7.5pt; color: var(--text-muted);">Garantir que todas as vozes sejam ouvidas e respeitadas na operação.</p>
                </div>
                <div class="concept-card" style="text-align: center; background: #FFFFFF; border-top: 3px solid var(--rose-accent);">
                    <div style="font-size: 13pt; font-weight: 900; color: var(--rose-accent); margin-bottom: 1mm;">EQUIDADE</div>
                    <p style="font-size: 7.5pt; color: var(--text-muted);">Oferecer condições justas e proporcionais de crescimento profissional.</p>
                </div>
                <div class="concept-card" style="text-align: center; background: #FFFFFF; border-top: 3px solid var(--gold-accent);">
                    <div style="font-size: 13pt; font-weight: 900; color: var(--gold-accent); margin-bottom: 1mm;">INOVAÇÃO</div>
                    <p style="font-size: 7.5pt; color: var(--text-muted);">Equipes diversas geram decisões melhores e ativos mais confiáveis.</p>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">ABRAMAN • Diversidade de Gênero na Manutenção</span>
            <span class="footer-center">Mensagens Institucionais</span>
            <span class="footer-page-num">02</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 03: SUMÁRIO EDITORIAL
    # ==========================================
    pages.append("""
    <!-- PÁGINA 03: SUMÁRIO EDITORIAL -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Estrutura</span>
                    <span class="chapter-category">Sumário da Publicação</span>
                </div>
                <div class="page-header-right">Guia Completo</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Visão Geral dos Conteúdos</span>
                <h1 class="chapter-main-title">Sumário Temático</h1>
                <p class="chapter-subtitle">Diversidade de Gênero na Manutenção e Gestão de Ativos</p>
            </div>

            <div class="grid-2-col" style="gap: 4mm; margin-bottom: 4mm;">
                <!-- Coluna 1 -->
                <div style="display: flex; flex-direction: column; gap: 2.5mm;">
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">01 • Por que esta cartilha?</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 04</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">02 • Entendendo a Diversidade</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 05</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">03 • Diversidade na Manutenção & Ativos</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 06</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">04 • Panorama de Dados (RAIS & Broken Rung)</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 07</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">05 • Desafios das Mulheres no Setor</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 08</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">06 • O Papel da Liderança Inclusiva</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 09</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">07 • Maternidade & Retenção de Talentos</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 10</span>
                    </div>
                </div>

                <!-- Coluna 2 -->
                <div style="display: flex; flex-direction: column; gap: 2.5mm;">
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">08 • Maternidade Atípica & Apoio Real</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 11</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">09 • Barreiras Físicas & Estruturais (EPIs/NR)</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 12</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">10 • Barreiras Culturais & Comportamentais</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 13</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">11 • Microagressões & Vieses Inconscientes</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 14</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">12 • Homens como Aliados na Equidade</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 15</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">13 • O Papel do Comitê Feminino</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 16</span>
                    </div>
                    <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 2mm 3mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8.5pt; font-weight: 700; color: var(--abraman-navy);">14 • Como sua Organização Pode Mudar</span>
                        <span style="font-size: 8pt; font-weight: 800; color: var(--rose-accent);">Pág. 17</span>
                    </div>
                </div>
            </div>

            <!-- Caixa de Utilização -->
            <div class="editorial-box box-info" style="margin-top: 2mm;">
                <div class="box-title"><i class="fa-solid fa-lightbulb"></i> Como utilizar este guia na sua organização</div>
                <p style="font-size: 8.5pt; line-height: 1.45; margin: 0;">
                    Esta publicação foi estruturada para ser consultada tanto por líderes e gestores de manutenção quanto por profissionais de recursos humanos, equipes de campo e comitês de diversidade. Utilize os quadros <strong>Para Refletir</strong> e <strong>Boas Práticas</strong> para debater ações práticas em suas reuniões de equipe e DDS.
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">ABRAMAN • Diversidade de Gênero na Manutenção</span>
            <span class="footer-center">Sumário Temático</span>
            <span class="footer-page-num">03</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 04: CAPÍTULO 1 - POR QUE ESTA CARTILHA?
    # ==========================================
    pages.append("""
    <!-- PÁGINA 04: CAPÍTULO 1 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 01</span>
                    <span class="chapter-category">Contexto & Propósito</span>
                </div>
                <div class="page-header-right">Guia de Boas Práticas</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Transformação do Setor</span>
                <h1 class="chapter-main-title">Por que esta cartilha?</h1>
                <p class="chapter-subtitle">O Valor Estratégico da Diversidade na Gestão de Ativos</p>
            </div>

            <p class="editorial-lead">
                As organizações contemporâneas enfrentam um cenário de profundas transformações. A digitalização industrial, as novas tecnologias de monitoramento de ativos, a crescente complexidade operacional e a busca por excelência exigem ambientes capazes de reunir <strong>múltiplos conhecimentos, experiências e formas de pensar</strong>.
            </p>

            <p class="editorial-body-p">
                Nesse contexto, a diversidade de gênero deixa de ser apenas uma pauta de responsabilidade social ou cumprimento de cotas para consolidar-se como um <strong>pilar estratégico de competitividade</strong>. No setor de manutenção, onde segurança, confiabilidade e tomada de decisão ágil são prioritárias, construir equipes diversas amplia a capacidade analítica e reduz pontos cegos operacionais.
            </p>

            <!-- 4 Pilares da Transformação -->
            <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 3mm 4mm; margin-bottom: 3.5mm;">
                <h4 style="font-size: 9pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 2mm;">
                    Pilares da Transformação Estratégica na Manutenção:
                </h4>
                <div class="grid-2-col" style="gap: 2.5mm; margin: 0;">
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--abraman-blue); display: block;">1. Segurança Operacional</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Ambientes abertos estimulam o reporte proativo de falhas e riscos.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--rose-accent); display: block;">2. Tomada de Decisão</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Perspectivas plurais evitam o pensamento de manada (*groupthink*).</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--abraman-cyan); display: block;">3. Confiabilidade de Ativos</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Soluções multidisciplinares aumentam a disponibilidade e MTBF.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: #16A34A; display: block;">4. Valorização Humana</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Cultura de respeito eleva o engajamento e a retenção de talentos.</span>
                    </div>
                </div>
            </div>

            <p class="editorial-body-p">
                Esta cartilha foi desenvolvida pelo <strong>Subcomitê DIA</strong> do Comitê Feminino da ABRAMAN com o propósito de incentivar reflexões e compartilhar práticas para que a diversidade fortaleça pessoas, processos e resultados.
            </p>

            <div class="editorial-box box-quote" style="margin-top: 2mm;">
                <div class="box-title">Nosso Propósito Central</div>
                <p style="font-size: 9pt; font-weight: 600; line-height: 1.4; margin: 0;">
                    Contribuir para que a diversidade seja compreendida não apenas como um valor organizacional, mas como uma estratégia viva para fortalecer pessoas, processos e resultados industriais.
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 01 • Por que esta cartilha?</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">04</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 05: CAPÍTULO 2 - ENTENDENDO A DIVERSIDADE
    # ==========================================
    pages.append("""
    <!-- PÁGINA 05: CAPÍTULO 2 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 02</span>
                    <span class="chapter-category">Conceitos Fundamentais</span>
                </div>
                <div class="page-header-right">Fundamentos</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Alinhamento Conceitual</span>
                <h1 class="chapter-main-title">Entendendo a Diversidade de Gênero</h1>
                <p class="chapter-subtitle">Conceitos Essenciais: Diversidade, Inclusão, Equidade e Pertencimento</p>
            </div>

            <p class="editorial-lead">
                <strong>Diversidade de gênero</strong> refere-se ao reconhecimento e ao respeito às diferentes identidades e expressões de gênero, assegurando oportunidades equitativas de participação, desenvolvimento e liderança na engenharia e na manutenção.
            </p>

            <!-- Layout Split 2 Colunas: Imagem Completa + Conceitos -->
            <div style="display: flex; gap: 4mm; align-items: stretch; margin-bottom: 3.5mm;">
                <!-- Coluna Esquerda: Imagem Completa Original sem cortes -->
                <div style="flex: 0 0 44%; display: flex; flex-direction: column;">
                    <div class="editorial-img-container" style="flex: 1; display: flex; flex-direction: column;">
                        <img src="assets/img_cap2_diversidade.jpg" alt="Diversidade e Inclusão na Prática">
                        <div class="editorial-img-caption">
                            Mulheres na Liderança Técnica
                        </div>
                    </div>
                </div>

                <!-- Coluna Direita: Os 5 Conceitos -->
                <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; gap: 1.8mm;">
                    <div class="concept-card">
                        <div class="concept-card-header">
                            <span class="concept-num">1</span>
                            <span class="concept-title">Diversidade</span>
                        </div>
                        <p class="concept-desc">Presença de diferentes trajetórias e identidades. <em>"Quem faz parte da organização?"</em></p>
                    </div>

                    <div class="concept-card">
                        <div class="concept-card-header">
                            <span class="concept-num">2</span>
                            <span class="concept-title">Inclusão</span>
                        </div>
                        <p class="concept-desc">Condições reais para atuação ativa nos processos e decisões. <em>"Quem participa?"</em></p>
                    </div>

                    <div class="concept-card">
                        <div class="concept-card-header">
                            <span class="concept-num">3</span>
                            <span class="concept-title">Equidade</span>
                        </div>
                        <p class="concept-desc">Apoio proporcional às necessidades reais de cada pessoa para oportunidades justas.</p>
                    </div>

                    <div class="concept-card">
                        <div class="concept-card-header">
                            <span class="concept-num">4</span>
                            <span class="concept-title">Acessibilidade</span>
                        </div>
                        <p class="concept-desc">Eliminação de barreiras físicas, comunicacionais e atitudinais em campo.</p>
                    </div>

                    <div class="concept-card" style="background: var(--rose-light); border-color: var(--rose-border);">
                        <div class="concept-card-header">
                            <span class="concept-num" style="background: var(--rose-accent);">5</span>
                            <span class="concept-title" style="color: #9F1239;">Pertencimento</span>
                        </div>
                        <p class="concept-desc" style="color: #881337;">Sentir-se valorizado, seguro e respeitado por suas competências técnicas.</p>
                    </div>
                </div>
            </div>

            <!-- Síntese Editorial -->
            <div class="editorial-box box-quote" style="margin-top: 1mm;">
                <p style="font-size: 8.5pt; font-weight: 700; line-height: 1.4; text-align: center; margin: 0;">
                    <em>"Diversidade é convidar para a equipe. Inclusão é garantir que todos participem com plenitude."</em>
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 02 • Entendendo a Diversidade</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">05</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 06: CAPÍTULO 3 - DIVERSIDADE NA MANUTENÇÃO
    # ==========================================
    pages.append("""
    <!-- PÁGINA 06: CAPÍTULO 3 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 03</span>
                    <span class="chapter-category">Impacto Setorial</span>
                </div>
                <div class="page-header-right">Relevância Operacional</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Excelência Operacional</span>
                <h1 class="chapter-main-title">Diversidade na Manutenção & Ativos</h1>
                <p class="chapter-subtitle">Segurança, Confiabilidade e Sustentabilidade dos Processos</p>
            </div>

            <p class="editorial-lead">
                Os setores de manutenção e gestão de ativos desempenham papel vital na continuidade operacional das organizações. Suas decisões influenciam diretamente a disponibilidade dos equipamentos, a integridade física dos trabalhadores, a gestão de riscos e os custos operacionais.
            </p>

            <!-- Imagem Técnica Oficial -->
            <div class="editorial-img-container" style="max-height: 65mm; margin-bottom: 3.5mm;">
                <img src="assets/img_cap3_manutencao.png" alt="Gestão de Ativos e Manutenção">
                <div class="editorial-img-caption">
                    Excelência Técnica e Multidisciplinaridade na Manutenção
                </div>
            </div>

            <p class="editorial-body-p">
                Equipes homogêneas tendem a abordar problemas sob os mesmos ângulos consolidados. A presença feminina traz novas abordagens para a análise de causas-raiz (RCA), planejamento de paradas, ergonomia de postos de trabalho e liderança de campo.
            </p>

            <div class="editorial-box box-reflection">
                <div class="box-title"><i class="fa-solid fa-magnifying-glass"></i> Para refletir na sua equipe</div>
                <p style="font-size: 8.5pt; font-weight: 600; line-height: 1.4; margin: 0;">
                    "Sua organização possui diversidade suficiente para enfrentar falhas complexas e desafios tecnológicos sob diferentes perspectivas?"
                </p>
            </div>

            <div class="editorial-box box-quote">
                <div class="box-title">Mensagem-chave</div>
                <p style="font-size: 9pt; font-weight: 700; text-align: center; margin: 0;">
                    "A diversidade fortalece pessoas. Pessoas fortalecem processos. Processos fortalecem resultados."
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 03 • Diversidade na Manutenção</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">06</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 07: CAPÍTULO 4 - PANORAMA DE DADOS
    # ==========================================
    pages.append("""
    <!-- PÁGINA 07: CAPÍTULO 4 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 04</span>
                    <span class="chapter-category">Panorama de Dados</span>
                </div>
                <div class="page-header-right">Estatísticas & Evidências</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Diagnóstico do Mercado</span>
                <h1 class="chapter-main-title">Diversidade de Gênero em Números</h1>
                <p class="chapter-subtitle">O Cenário no Brasil e o Fenômeno do "Broken Rung"</p>
            </div>

            <p class="editorial-lead">
                Compreender o cenário atual a partir de dados consolidados é o primeiro passo para construir políticas efetivas de equidade e reter talentos técnicos qualificados.
            </p>

            <!-- Banner Estatístico RAIS -->
            <div style="background: linear-gradient(135deg, #0B192C 0%, #1E3A8A 100%); color: white; border-radius: 6px; padding: 4mm 5mm; display: flex; align-items: center; gap: 5mm; margin-bottom: 3.5mm;">
                <div style="font-size: 26pt; font-weight: 900; color: #FB7185; line-height: 1;">-20,9%</div>
                <div>
                    <strong style="font-size: 9.5pt; color: #FFFFFF; display: block; margin-bottom: 1mm;">Diferença Salarial Média no Brasil</strong>
                    <span style="font-size: 8pt; color: #CBD5E1; line-height: 1.35; display: block;">
                        Segundo o <em>3º Relatório de Transparência Salarial</em> (Ministério do Trabalho e Emprego / RAIS 2024), mulheres recebem em média 20,9% a menos do que homens em empresas com 100+ funcionários. Em cargos de liderança técnica e gerência, essa disparidade atinge <strong>25,2%</strong>.
                    </span>
                </div>
            </div>

            <!-- O Fenômeno Broken Rung -->
            <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 3.5mm 4.5mm; margin-bottom: 3.5mm;">
                <h4 style="font-size: 9.5pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 1.5mm;">
                    O Fenômeno do "Broken Rung" (Degrau Quebrado)
                </h4>
                <p class="editorial-body-p" style="margin-bottom: 2mm;">
                    O estudo global <em>Women in the Workplace</em> (McKinsey & Co. e LeanIn.Org) demonstra que o maior obstáculo para mulheres não está no teto de vidro, mas no <strong>primeiro degrau para a liderança</strong>:
                </p>
                <div style="display: flex; justify-content: space-around; background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2.5mm; margin-bottom: 2mm;">
                    <div style="text-align: center;">
                        <span style="font-size: 16pt; font-weight: 900; color: var(--abraman-blue);">100</span>
                        <span style="font-size: 7.5pt; color: var(--text-muted); display: block;">Homens promovidos a gerente</span>
                    </div>
                    <div style="font-size: 18pt; color: #CBD5E1; font-weight: 300;">vs</div>
                    <div style="text-align: center;">
                        <span style="font-size: 16pt; font-weight: 900; color: var(--rose-accent);">81</span>
                        <span style="font-size: 7.5pt; color: var(--text-muted); display: block;">Mulheres promovidas no mesmo nível</span>
                    </div>
                </div>
                <p style="font-size: 7.5pt; color: var(--text-muted); margin: 0;">
                    Na engenharia e manutenção, esse descompasso inicial reduz drasticamente o contingente feminino disponível para cargos de superintendência e diretoria.
                </p>
            </div>

            <div class="editorial-box box-reflection">
                <div class="box-title">Para refletir</div>
                <p style="font-size: 8.5pt; font-weight: 600; margin: 0;">
                    "Como está a taxa de promoção de técnicas e engenheiras para a primeira liderança na sua empresa?"
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 04 • Panorama de Dados</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">07</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 08: CAPÍTULO 5 - DESAFIOS DAS MULHERES
    # ==========================================
    pages.append("""
    <!-- PÁGINA 08: CAPÍTULO 5 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 05</span>
                    <span class="chapter-category">Desafios & Barreiras</span>
                </div>
                <div class="page-header-right">Mapeamento de Realidade</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Superação e Acolhimento</span>
                <h1 class="chapter-main-title">Desafios Enfrentados pelas Mulheres</h1>
                <p class="chapter-subtitle">Fatores que Impactam a Carreira e a Permanência no Setor</p>
            </div>

            <p class="editorial-lead">
                Para além das competências técnicas, as profissionais de manutenção enfrentam barreiras invisíveis que exigem maior esforço para comprovação de autoridade e geram sobrecarga emocional.
            </p>

            <!-- Grid com os 4 Grandes Desafios -->
            <div class="grid-2-col" style="gap: 3mm; margin-bottom: 3.5mm;">
                <div class="concept-card" style="border-left: 3.5px solid var(--rose-accent);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: #9F1239; margin-bottom: 1mm;">1. Prova Contínua de Competência</h4>
                    <p class="concept-desc">Necessidade constante de demonstrar conhecimentos técnicos e validação redobrada em decisões operacionais e pareceres.</p>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--abraman-blue);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 1mm;">2. Sobrecarga e Dupla Jornada</h4>
                    <p class="concept-desc">Acúmulo de responsabilidades de cuidado familiar e tarefas domésticas, impactando disponibilidade para escalas de sobreaviso.</p>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--abraman-cyan);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: #0369A1; margin-bottom: 1mm;">3. Escassez de Modelos e Mentorias</h4>
                    <p class="concept-desc">Poucas referências femininas em cargos de gerência de planta e diretoria, limitando redes de apoio e patrocínio profissional.</p>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--gold-accent);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: #92400E; margin-bottom: 1mm;">4. Isolamento em Equipes Operacionais</h4>
                    <p class="concept-desc">Sensação de não pertencimento ao ser frequentemente a única mulher na oficina, no turno ou no setor de engenharia.</p>
                </div>
            </div>

            <div class="editorial-box box-practices">
                <div class="box-title">O que a organização pode fazer</div>
                <ul class="editorial-list">
                    <li>Implementar programas estruturados de <strong>mentoria e apadrinhamento (sponsorship)</strong> para mulheres;</li>
                    <li>Estabelecer critérios transparentes e objetivos para promoções técnicas e liderança;</li>
                    <li>Criar grupos de afinidade e canais seguros para escuta ativa e acolhimento.</li>
                </ul>
            </div>

            <div class="editorial-box box-quote">
                <div class="box-title">Princípio Fundamental</div>
                <p style="font-size: 8.5pt; font-weight: 600; text-align: center; margin: 0;">
                    Ambientes seguros psicologicamente permitem que todos os profissionais dediquem 100% de sua energia à excelência do trabalho.
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 05 • Desafios das Mulheres</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">08</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 09: CAPÍTULO 6 - LIDERANÇA INCLUSIVA
    # ==========================================
    pages.append("""
    <!-- PÁGINA 09: CAPÍTULO 6 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 06</span>
                    <span class="chapter-category">Papel da Liderança</span>
                </div>
                <div class="page-header-right">Gestão & Cultura</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Liderança que Transforma</span>
                <h1 class="chapter-main-title">O Papel da Liderança Inclusiva</h1>
                <p class="chapter-subtitle">Como Gestores e Coordenadores Podem Impulsionar a Equidade</p>
            </div>

            <p class="editorial-lead">
                A cultura organizacional não muda por decretos, mas pelo <strong>comportamento diário das lideranças</strong>. Os gestores são os guardiões do clima de respeito e os principais viabilizadores de oportunidades.
            </p>

            <!-- 4 Atitudes do Líder Inclusivo -->
            <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 3.5mm 4mm; margin-bottom: 3.5mm;">
                <h4 style="font-size: 9pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 2mm;">
                    Pilares da Liderança Inclusiva na Operação:
                </h4>
                <div class="grid-2-col" style="gap: 2.5mm; margin: 0;">
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--abraman-blue); display: block;">1. Exemplo e Tolerância Zero</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Não tolerar piadas depreciativas, comentários machistas ou desrespeito.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--rose-accent); display: block;">2. Escuta Ativa e Empatia</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Ouvir genuinamente os desafios da equipe sem minimizar relatos.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--abraman-cyan); display: block;">3. Distribuição Equitativa</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Designar projetos estratégicos e de alta visibilidade com equidade.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: #16A34A; display: block;">4. Gestão por Métricas</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Acompanhar indicadores de atração, retenção e equidade salarial.</span>
                    </div>
                </div>
            </div>

            <div class="editorial-box box-reflection">
                <div class="box-title">Para autoavaliação da liderança</div>
                <ul class="editorial-list">
                    <li>Você costuma interromper comportamentos inadequados imediatamente quando ocorrem na sua presença?</li>
                    <li>As oportunidades de treinamento externo e participação em comissões técnicas são distribuídas de forma transparente?</li>
                    <li>Sua equipe se sente confortável para apontar vieses e sugerir melhorias?</li>
                </ul>
            </div>

            <div class="editorial-box box-quote">
                <p style="font-size: 8.5pt; font-weight: 700; text-align: center; margin: 0;">
                    "Liderar para a diversidade é criar pontes onde antes existiam barreiras."
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 06 • Papel da Liderança</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">09</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 10: CAPÍTULO 7 - MATERNIDADE
    # ==========================================
    pages.append("""
    <!-- PÁGINA 10: CAPÍTULO 7 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 07</span>
                    <span class="chapter-category">Parentalidade & Retenção</span>
                </div>
                <div class="page-header-right">Acolhimento de Talentos</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Valorização da Vida</span>
                <h1 class="chapter-main-title">Maternidade</h1>
                <p class="chapter-subtitle">Valorizando Pessoas e Preservando Talentos Técnicos</p>
            </div>

            <div class="editorial-box box-quote" style="margin-bottom: 3.5mm;">
                <p style="font-size: 8.5pt; font-weight: 600; line-height: 1.4; margin: 0;">
                    "A maternidade não reduz o potencial nem o compromisso de uma profissional. Organizações inclusivas acolhem os diferentes ciclos de vida sem limitar trajetórias de carreira."
                </p>
            </div>

            <!-- Grid de Fotos Reais da Proposta -->
            <div class="grid-2-col" style="gap: 3.5mm; margin-bottom: 3.5mm;">
                <div class="editorial-img-container" style="height: 44mm;">
                    <img src="assets/img_cap7_maternidade_1.jpg" alt="Acolhimento à Maternidade" style="object-fit: cover;">
                </div>
                <div class="editorial-img-container" style="height: 44mm;">
                    <img src="assets/img_cap7_maternidade_2.jpg" alt="Preservação de Talentos" style="object-fit: cover;">
                </div>
            </div>

            <!-- Boas Práticas Organizacionais -->
            <div class="editorial-box box-practices">
                <div class="box-title">Boas Práticas para Empresas e Gestores:</div>
                <ul class="editorial-list">
                    <li><strong>Plano de Retorno Gradual:</strong> Reintegração planejada com reuniões de atualização técnica e redistribuição de metas no pós-licença;</li>
                    <li><strong>Espaços Adequados:</strong> Instalação de salas de apoio à amamentação e coleta segura de leite nas plantas industriais;</li>
                    <li><strong>Corresponsabilidade Parental:</strong> Incentivo ativo ao uso da licença-paternidade estendida e apoio aos pais;</li>
                    <li><strong>Flexibilidade de Jornada:</strong> Adaptação temporária de escalas operacionais e turnos quando viável.</li>
                </ul>
            </div>

            <div class="editorial-box box-reflection">
                <div class="box-title">Para refletir</div>
                <p style="font-size: 8pt; font-weight: 600; margin: 0;">
                    "Sua empresa mantém os mesmos planos de promoção e capacitação para profissionais que retornam da licença-maternidade?"
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 07 • Maternidade</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">10</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 11: CAPÍTULO 8 - MATERNIDADE ATÍPICA
    # ==========================================
    pages.append("""
    <!-- PÁGINA 11: CAPÍTULO 8 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 08</span>
                    <span class="chapter-category">Inclusão Especializada</span>
                </div>
                <div class="page-header-right">Equidade Real</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Apoio e Empatia</span>
                <h1 class="chapter-main-title">Maternidade Atípica</h1>
                <p class="chapter-subtitle">Inclusão, Empatia e Apoio Real às Mães de Filhos com Necessidades Especiais</p>
            </div>

            <div class="editorial-box box-quote" style="margin-bottom: 3.5mm;">
                <p style="font-size: 8.5pt; font-weight: 600; line-height: 1.4; margin: 0;">
                    "Equidade começa quando compreendemos que pessoas diferentes enfrentam desafios diferentes e necessitam de apoios distintos."
                </p>
            </div>

            <p class="editorial-lead">
                <strong>Maternidade atípica</strong> refere-se à vivência de mães de crianças com deficiência, neurodivergências (como Autismo e TDAH) ou doenças raras que demandam rotinas intensas de terapias, consultas médicas e cuidados constantes.
            </p>

            <!-- Grid de Fotos Reais da Proposta -->
            <div class="grid-2-col" style="gap: 3.5mm; margin-bottom: 3.5mm;">
                <div class="editorial-img-container" style="height: 44mm;">
                    <img src="assets/img_cap8_maternidade_atipica_1.jpg" alt="Maternidade Atípica" style="object-fit: cover;">
                </div>
                <div class="editorial-img-container" style="height: 44mm;">
                    <img src="assets/img_cap8_maternidade_atipica_2.jpg" alt="Apoio e Cuidados" style="object-fit: cover;">
                </div>
            </div>

            <!-- Ações Concretas -->
            <div class="editorial-box box-practices">
                <div class="box-title">Como as organizações podem apoiar:</div>
                <ul class="editorial-list">
                    <li><strong>Flexibilidade de Horários e Banco de Horas:</strong> Viabilizar o acompanhamento em terapias sem prejuízo na avaliação profissional;</li>
                    <li><strong>Segurança Psicológica:</strong> Ambiente livre de julgamentos sobre saídas de emergência e faltas justificadas;</li>
                    <li><strong>Extensão de Benefícios:</strong> Planos de saúde com cobertura ampla para terapias multidisciplinares (fonoaudiologia, TO, psicologia).</li>
                </ul>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 08 • Maternidade Atípica</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">11</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 12: CAPÍTULO 9 - BARREIRAS FÍSICAS E ESTRUTURAIS
    # ==========================================
    pages.append("""
    <!-- PÁGINA 12: CAPÍTULO 9 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 09</span>
                    <span class="chapter-category">Infraestrutura & Ergonomia</span>
                </div>
                <div class="page-header-right">Adequação de Campo</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Condições de Trabalho</span>
                <h1 class="chapter-main-title">Barreiras Físicas e Estruturais</h1>
                <p class="chapter-subtitle">Adequação de EPIs, Instalações e Ergonomia Industrial</p>
            </div>

            <p class="editorial-lead">
                A inclusão feminina na manutenção exige que as instalações e os equipamentos de proteção individual (EPIs) sejam adequados à antropometria das mulheres, garantindo segurança operacional e dignidade.
            </p>

            <div class="grid-2-col" style="gap: 3mm; margin-bottom: 3.5mm;">
                <div class="concept-card" style="border-left: 3.5px solid var(--rose-accent);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: #9F1239; margin-bottom: 1mm;">1. EPIs com Modelagem Feminina</h4>
                    <p class="concept-desc">Calçados de segurança em numerações menores (33 a 36), luvas ergonômicas, cintos de segurança para trabalho em altura e uniformes com corte adequado.</p>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--abraman-blue);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 1mm;">2. Vestiários e Sanitários Dignos</h4>
                    <p class="concept-desc">Instalações sanitárias exclusivas, limpas, seguras e próximas aos postos de trabalho de campo e oficinas operacionais.</p>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--abraman-cyan);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: #0369A1; margin-bottom: 1mm;">3. Ergonomia e Ferramental</h4>
                    <p class="concept-desc">Disponibilização de ferramentas ergonômicas com alavancas adequadas, dispositivos de içamento e bancadas ajustáveis que beneficiam toda a equipe.</p>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--gold-accent);">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: #92400E; margin-bottom: 1mm;">4. Conformidade com a NR-1 e NR-24</h4>
                    <p class="concept-desc">Cumprimento rigoroso das normas regulamentadoras que exigem condições sanitárias e de conforto nos locais de trabalho.</p>
                </div>
            </div>

            <div class="editorial-box box-practices">
                <div class="box-title">Recomendações Práticas:</div>
                <ul class="editorial-list">
                    <li>Realizar censo ergonômico e consulta direta às técnicas de campo antes de adquirir lotes de EPIs;</li>
                    <li>Garantir privacidade e segurança nos trajetos até os vestiários industriais.</li>
                </ul>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 09 • Barreiras Físicas</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">12</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 13: CAPÍTULO 10 - BARREIRAS CULTURAIS
    # ==========================================
    pages.append("""
    <!-- PÁGINA 13: CAPÍTULO 10 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 10</span>
                    <span class="chapter-category">Cultura & Comportamento</span>
                </div>
                <div class="page-header-right">Transformação Cultural</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Superação de Vieses</span>
                <h1 class="chapter-main-title">Barreiras Culturais e Comportamentais</h1>
                <p class="chapter-subtitle">Desconstruindo Estereótipos Históricos na Manutenção</p>
            </div>

            <p class="editorial-lead">
                Durante décadas, áreas técnicas consolidaram uma cultura baseada em estereótipos que associavam manutenção exclusivamente à força física e comportamentos masculinos tradicionais.
            </p>

            <div class="editorial-box box-info" style="margin-bottom: 3.5mm;">
                <div class="box-title">Estereótipos que precisam ser superados:</div>
                <ul class="editorial-list">
                    <li><strong>"Manutenção exige apenas força bruta":</strong> Hoje a gestão moderna depende de análise de vibração, termografia, lubrificação de precisão, confiabilidade e gestão de dados;</li>
                    <li><strong>"Mulheres são frágeis para a área operacional":</strong> Competência técnica, disciplina metodológica e foco em segurança independem de gênero;</li>
                    <li><strong>"Elas não se adaptam ao ambiente de oficina":</strong> O ambiente industrial deve ser profissional, respeitoso e acolhedor para qualquer pessoa.</li>
                </ul>
            </div>

            <div class="grid-2-col" style="gap: 3mm; margin-bottom: 3.5mm;">
                <div class="concept-card">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 1mm;">Comunicação Inclusiva</h4>
                    <p class="concept-desc">Eliminar vocabulário depreciativo e piadas de cunho sexista em treinamentos, diálogos diários de segurança (DDS) e reuniões.</p>
                </div>
                <div class="concept-card">
                    <h4 style="font-size: 8.5pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 1mm;">Engajamento de Pares</h4>
                    <p class="concept-desc">Envolver técnicos e encarregados em workshops sobre respeito e colaboração mútua no chão de fábrica.</p>
                </div>
            </div>

            <div class="editorial-box box-quote">
                <p style="font-size: 8.5pt; font-weight: 700; text-align: center; margin: 0;">
                    "A verdadeira força da manutenção está na inteligência coletiva e no respeito mútuo."
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 10 • Barreiras Culturais</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">13</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 14: CAPÍTULO 11 - MICROAGRESSÕES
    # ==========================================
    pages.append("""
    <!-- PÁGINA 14: CAPÍTULO 11 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 11</span>
                    <span class="chapter-category">Relações no Trabalho</span>
                </div>
                <div class="page-header-right">Vieses Inconscientes</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Identificação e Combate</span>
                <h1 class="chapter-main-title">Microagressões e Vieses</h1>
                <p class="chapter-subtitle">Reconhecendo e Eliminando Comportamentos Sutis de Exclusão</p>
            </div>

            <p class="editorial-lead">
                <strong>Microagressões</strong> são atitudes, falas ou gestos cotidianos — muitas vezes não intencionais — que transmitem desvalorização, descrédito ou estereótipos sobre a capacidade profissional de mulheres.
            </p>

            <!-- 4 Tipos Comuns de Microagressões -->
            <div class="grid-2-col" style="gap: 3mm; margin-bottom: 3.5mm;">
                <div class="concept-card" style="border-left: 3.5px solid var(--rose-accent);">
                    <strong style="font-size: 8.5pt; color: #9F1239; display: block;">Mansplaining</strong>
                    <span class="concept-desc">Homem explicando de forma didática e paternalista um assunto técnico para uma especialista que já domina o tema.</span>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--abraman-blue);">
                    <strong style="font-size: 8.5pt; color: var(--abraman-navy); display: block;">Manterrupting</strong>
                    <span class="concept-desc">Interrupção sistemática e desnecessária da fala de uma mulher em reuniões técnicas antes que ela conclua seu raciocínio.</span>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--abraman-cyan);">
                    <strong style="font-size: 8.5pt; color: #0369A1; display: block;">Bropriating</strong>
                    <span class="concept-desc">Apropriação da ideia técnica apresentada por uma mulher, recebendo os créditos após repeti-la com outras palavras.</span>
                </div>

                <div class="concept-card" style="border-left: 3.5px solid var(--gold-accent);">
                    <strong style="font-size: 8.5pt; color: #92400E; display: block;">Questionamento de Autoridade</strong>
                    <span class="concept-desc">Pedir confirmação a outro colega homem após uma diretriz técnica dada por uma engenheira responsável.</span>
                </div>
            </div>

            <div class="editorial-box box-practices">
                <div class="box-title">Como agir ao presenciar uma microagressão:</div>
                <ul class="editorial-list">
                    <li><strong>Intervenha com naturalidade:</strong> <em>"Gostaria de ouvir o restante da conclusão da engenheira Fulana antes de prosseguirmos"</em>;</li>
                    <li><strong>Valide a autoria:</strong> <em>"Excelente ponto levantado originalmente pela colega Ciclana"</em>;</li>
                    <li><strong>Evite julgamentos defensivos:</strong> Use a situação como oportunidade educativa para o grupo.</li>
                </ul>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 11 • Microagressões</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">14</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 15: CAPÍTULO 12 - HOMENS COMO ALIADOS
    # ==========================================
    pages.append("""
    <!-- PÁGINA 15: CAPÍTULO 12 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 12</span>
                    <span class="chapter-category">Alianças Estratégicas</span>
                </div>
                <div class="page-header-right">Engajamento Coletivo</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Corresponsabilidade</span>
                <h1 class="chapter-main-title">Homens como Aliados na Equidade</h1>
                <p class="chapter-subtitle">O Protagonismo Masculino na Construção de Espaços Justos</p>
            </div>

            <p class="editorial-lead">
                A promoção da equidade de gênero não é uma pauta exclusiva das mulheres. Como os homens ocupam a maioria das posições de liderança e supervisão no setor, seu <strong>engajamento ativo como aliados</strong> é indispensável para acelerar as transformações.
            </p>

            <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 3.5mm 4mm; margin-bottom: 3.5mm;">
                <h4 style="font-size: 9pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 2mm;">
                    Comportamentos de um Aliado Ativo:
                </h4>
                <div class="grid-2-col" style="gap: 2.5mm; margin: 0;">
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--abraman-blue); display: block;">1. Ceder Espaço e Dar Visibilidade</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Recomendar colegas mulheres para apresentações técnicas e projetos de destaque.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--rose-accent); display: block;">2. Confrontar Vieses entre Pares</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Posicionar-se firmemente em conversas informais quando presenciar preconceito.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: var(--abraman-cyan); display: block;">3. Praticar a Escuta Humilde</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Buscar compreender os desafios específicos vividos pelas profissionais sem tentar justificar.</span>
                    </div>
                    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 4px; padding: 2mm 2.5mm;">
                        <strong style="font-size: 8.5pt; color: #16A34A; display: block;">4. Apoiar Políticas Institucionais</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Defender ativamente metas de inclusão, equidade salarial e adequação estrutural.</span>
                    </div>
                </div>
            </div>

            <div class="editorial-box box-quote">
                <p style="font-size: 9pt; font-weight: 700; text-align: center; margin: 0;">
                    "Aliados não são espectadores. São agentes ativos da evolução da engenharia."
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 12 • Homens como Aliados</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">15</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 16: CAPÍTULO 13 - O COMITÊ FEMININO
    # ==========================================
    pages.append("""
    <!-- PÁGINA 16: CAPÍTULO 13 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 13</span>
                    <span class="chapter-category">Rede & Conexão</span>
                </div>
                <div class="page-header-right">Iniciativa ABRAMAN</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Comunidade & Liderança</span>
                <h1 class="chapter-main-title">O Papel do Comitê Feminino</h1>
                <p class="chapter-subtitle">Conectando Profissionais e Transformando o Setor</p>
            </div>

            <p class="editorial-lead">
                O Comitê Feminino da ABRAMAN é uma rede colaborativa dedicada a apoiar, capacitar e inspirar mulheres que atuam na manutenção e gestão de ativos em todo o Brasil.
            </p>

            <!-- Banner Oficial do Comitê -->
            <div class="editorial-img-container" style="max-height: 55mm; margin-bottom: 3.5mm;">
                <img src="BannerFeminino.jpg" alt="Comitê Feminino ABRAMAN">
            </div>

            <div class="grid-3-col" style="margin-bottom: 3mm;">
                <div class="concept-card" style="text-align: center; border-top: 3px solid var(--abraman-blue);">
                    <strong style="font-size: 8.5pt; color: var(--abraman-navy); display: block; margin-bottom: 1mm;">Capacitação</strong>
                    <p style="font-size: 7.5pt; color: var(--text-body);">Webinars técnicos, minicursos e publicações voltadas ao desenvolvimento de competências.</p>
                </div>
                <div class="concept-card" style="text-align: center; border-top: 3px solid var(--rose-accent);">
                    <strong style="font-size: 8.5pt; color: var(--rose-accent); display: block; margin-bottom: 1mm;">Networking</strong>
                    <p style="font-size: 7.5pt; color: var(--text-body);">Troca contínua de experiências entre profissionais de diversas indústrias e regiões do país.</p>
                </div>
                <div class="concept-card" style="text-align: center; border-top: 3px solid var(--abraman-cyan);">
                    <strong style="font-size: 8.5pt; color: #0369A1; display: block; margin-bottom: 1mm;">Pesquisa & Dados</strong>
                    <p style="font-size: 7.5pt; color: var(--text-body);">Levantamento de estatísticas e diagnósticos do setor industrial nacional.</p>
                </div>
            </div>

            <div class="editorial-box box-quote">
                <p style="font-size: 8.5pt; font-weight: 700; text-align: center; margin: 0;">
                    Junte-se ao Comitê Feminino ABRAMAN e participe ativamente dessa transformação!
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 13 • Comitê Feminino ABRAMAN</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">16</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 17: CAPÍTULO 14 - COMO SUA ORGANIZAÇÃO PODE MUDAR
    # ==========================================
    pages.append("""
    <!-- PÁGINA 17: CAPÍTULO 14 -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Capítulo 14</span>
                    <span class="chapter-category">Plano de Ação</span>
                </div>
                <div class="page-header-right">Guia de Implementação</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Da Teoria à Prática</span>
                <h1 class="chapter-main-title">Como sua Organização Pode Fazer a Diferença</h1>
                <p class="chapter-subtitle">Roteiro Prático em 5 Passos para Implementar a Diversidade</p>
            </div>

            <p class="editorial-lead">
                A implementação de práticas inclusivas não precisa ser um processo complexo. Pequenas decisões estruturadas geram grande impacto no engajamento e nos resultados operacionais.
            </p>

            <!-- Roteiro em 5 Passos -->
            <div style="display: flex; flex-direction: column; gap: 2mm; margin-bottom: 3.5mm;">
                <div style="background: var(--bg-light); border-left: 4px solid var(--abraman-blue); border-radius: 4px; padding: 2mm 3mm; display: flex; gap: 3mm; align-items: center;">
                    <span style="font-size: 11pt; font-weight: 900; color: var(--abraman-blue);">1</span>
                    <div>
                        <strong style="font-size: 8.5pt; color: var(--abraman-navy); display: block;">Diagnóstico Interno</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Mapear o percentual de mulheres em cargos operacionais, técnicos e de liderança.</span>
                    </div>
                </div>

                <div style="background: var(--bg-light); border-left: 4px solid var(--rose-accent); border-radius: 4px; padding: 2mm 3mm; display: flex; gap: 3mm; align-items: center;">
                    <span style="font-size: 11pt; font-weight: 900; color: var(--rose-accent);">2</span>
                    <div>
                        <strong style="font-size: 8.5pt; color: #9F1239; display: block;">Adequação Estrutural</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Garantir vestiários dignos e EPIs modelados para o público feminino.</span>
                    </div>
                </div>

                <div style="background: var(--bg-light); border-left: 4px solid var(--abraman-cyan); border-radius: 4px; padding: 2mm 3mm; display: flex; gap: 3mm; align-items: center;">
                    <span style="font-size: 11pt; font-weight: 900; color: #0369A1; display: block;">3</span>
                    <div>
                        <strong style="font-size: 8.5pt; color: #0369A1; display: block;">Sensibilização da Liderança</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Capacitar supervisores e encarregados sobre liderança inclusiva e respeito.</span>
                    </div>
                </div>

                <div style="background: var(--bg-light); border-left: 4px solid var(--gold-accent); border-radius: 4px; padding: 2mm 3mm; display: flex; gap: 3mm; align-items: center;">
                    <span style="font-size: 11pt; font-weight: 900; color: #92400E; display: block;">4</span>
                    <div>
                        <strong style="font-size: 8.5pt; color: #92400E; display: block;">Processos Seletivos e Promoções</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Assegurar listas de candidatos com representatividade em todos os níveis técnicos.</span>
                    </div>
                </div>

                <div style="background: var(--bg-light); border-left: 4px solid #16A34A; border-radius: 4px; padding: 2mm 3mm; display: flex; gap: 3mm; align-items: center;">
                    <span style="font-size: 11pt; font-weight: 900; color: #16A34A;">5</span>
                    <div>
                        <strong style="font-size: 8.5pt; color: #166534; display: block;">Acompanhamento Contínuo</strong>
                        <span style="font-size: 7.5pt; color: var(--text-body);">Monitorar pesquisas de clima, taxas de retenção e evolução salarial.</span>
                    </div>
                </div>
            </div>

            <div class="editorial-box box-quote">
                <p style="font-size: 8.5pt; font-weight: 700; text-align: center; margin: 0;">
                    "O futuro da manutenção é sustentável, tecnológico e profundamente humano."
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Capítulo 14 • Como sua Organização Pode Mudar</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">17</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 18: PALAVRAS FINAIS E AGRADECIMENTOS
    # ==========================================
    pages.append("""
    <!-- PÁGINA 18: PALAVRAS FINAIS -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Encerramento</span>
                    <span class="chapter-category">Palavras Finais</span>
                </div>
                <div class="page-header-right">Agradecimentos</div>
            </div>

            <div class="chapter-title-group">
                <span class="chapter-badge-top">Compromisso Permanente</span>
                <h1 class="chapter-main-title">Palavras Finais</h1>
                <p class="chapter-subtitle">Construindo Juntos o Amanhã da Gestão de Ativos</p>
            </div>

            <p class="editorial-lead">
                A publicação desta cartilha representa um marco no compromisso da ABRAMAN com a modernização das relações de trabalho e com a excelência técnica na gestão de ativos industriais.
            </p>

            <p class="editorial-body-p">
                Agradecemos profundamente a cada profissional, líder e organização associada que dedicou tempo, depoimentos e expertise para a elaboração deste material. Cada boa prática aqui descrita ganha vida quando aplicada no chão de fábrica, nas salas de engenharia e nos conselhos diretivos.
            </p>

            <div class="editorial-box box-quote" style="padding: 4mm 5mm; margin: 4mm 0;">
                <p style="font-size: 10pt; font-weight: 800; color: #9F1239; text-align: center; line-height: 1.45; margin: 0;">
                    "Que este guia seja uma ferramenta viva de consulta, reflexão e inspiração para que a diversidade de gênero consolide-se definitivamente como uma força propulsora da indústria brasileira."
                </p>
            </div>

            <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 3.5mm 4mm; margin-top: 3mm;">
                <h4 style="font-size: 9pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 2mm;">
                    Agradecimentos Especiais:
                </h4>
                <ul class="editorial-list">
                    <li>À Diretoria Executiva da ABRAMAN pelo apoio irrestrito às iniciativas de diversidade;</li>
                    <li>Às integrantes do Comitê Feminino e do Subcomitê DIA pela autoria e dedicação editorial;</li>
                    <li>A todas as mulheres pioneiras que desbravaram caminhos na manutenção nacional.</li>
                </ul>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Palavras Finais & Agradecimentos</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">18</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 19: MANIFESTO & EXPEDIENTE
    # ==========================================
    pages.append("""
    <!-- PÁGINA 19: MANIFESTO & EXPEDIENTE -->
    <div class="a4-page content-page">
        <div>
            <div class="page-header">
                <div class="page-header-left">
                    <span class="chapter-pill">Manifesto</span>
                    <span class="chapter-category">ABRAMAN Mulher</span>
                </div>
                <div class="page-header-right">Expediente Oficial</div>
            </div>

            <!-- Manifesto ABRAMAN Mulher -->
            <div style="background: linear-gradient(135deg, #0B192C 0%, #1E3A8A 100%); color: white; border-radius: 6px; padding: 4mm 5mm; margin-bottom: 4mm;">
                <h2 style="font-family: 'Montserrat', sans-serif; font-size: 13pt; font-weight: 800; color: #FB7185; margin-bottom: 2mm; text-align: center;">
                    Manifesto ABRAMAN Mulher
                </h2>
                <p style="font-size: 8pt; line-height: 1.5; color: #E2E8F0; text-align: justify; margin-bottom: 1.5mm;">
                    Acreditamos em uma engenharia sem barreiras, onde a competência técnica e a paixão pela excelência operacional sejam os únicos critérios de valorização.
                </p>
                <p style="font-size: 8pt; line-height: 1.5; color: #E2E8F0; text-align: justify; margin: 0;">
                    Comprometemo-nos a abrir caminhos, acolher talentos e transformar as indústrias brasileiras em ambientes plurais, inovadores e seguros para todas as gerações.
                </p>
            </div>

            <!-- Ficha Técnica / Expediente -->
            <div style="background: var(--bg-light); border: 1px solid #E2E8F0; border-radius: 6px; padding: 3.5mm 4.5mm;">
                <h3 style="font-size: 9.5pt; font-weight: 800; color: var(--abraman-navy); margin-bottom: 2mm; border-bottom: 1px solid #CBD5E1; padding-bottom: 1.5mm;">
                    Expediente Editorial
                </h3>
                <div style="font-size: 7.5pt; line-height: 1.5; color: var(--text-body);">
                    <p style="margin-bottom: 1.5mm;"><strong>Realização:</strong> Associação Brasileira de Manutenção e Gestão de Ativos (ABRAMAN)</p>
                    <p style="margin-bottom: 1.5mm;"><strong>Coordenação:</strong> Comitê Feminino ABRAMAN & Subcomitê DIA (Diversidade, Inclusão e Acessibilidade)</p>
                    <p style="margin-bottom: 1.5mm;"><strong>Presidente da ABRAMAN:</strong> Paula Granha</p>
                    <p style="margin-bottom: 1.5mm;"><strong>Edição e Diagramação:</strong> Equipe de Comunicação & Projetos Digitais ABRAMAN</p>
                    <p style="margin-bottom: 1.5mm;"><strong>Ano de Publicação:</strong> 2026 • 1ª Edição Oficial</p>
                    <p style="margin: 0;"><strong>Contato & Redes:</strong> comitefeminino@abraman.org.br • www.abraman.org.br</p>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-left">Manifesto Institucional & Expediente</span>
            <span class="footer-center">Comitê Feminino ABRAMAN</span>
            <span class="footer-page-num">19</span>
        </div>
    </div>
    """)

    # ==========================================
    # PÁGINA 20: CONTRACAPA OFICIAL (Full-Bleed)
    # ==========================================
    pages.append("""
    <!-- PÁGINA 20: CONTRACAPA -->
    <div class="a4-page full-bleed">
        <img src="ChatGPT Image Aug 30, 2026, 10_42_56 AM.png" alt="Contracapa Oficial - Comitê Feminino ABRAMAN">
    </div>
    """)

    # HTML Completo
    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cartilha Comitê Feminino ABRAMAN • Modo Leitura A4</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Montserrat:wght@500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
{css}
    </style>
</head>
<body>
    <div class="no-print-bar">
        <div style="font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 8px;">
            <i class="fa-solid fa-book-open" style="color: #FB7185;"></i>
            <span>Cartilha Comitê Feminino ABRAMAN • Visualização A4 (Modo Leitura)</span>
        </div>
        <button class="print-btn" onclick="window.print()">
            <i class="fa-solid fa-print"></i> Imprimir / Salvar em PDF
        </button>
    </div>

    <div class="page-wrapper">
        {"".join(pages)}
    </div>
</body>
</html>
"""

    with open("print_magazine.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Gerado com sucesso: print_magazine.html")

    # Compilar para PDF via Chrome Headless
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    pdf_output_name = "Cartilha Comitê Feminino ABRAMAN.pdf"
    html_abs_path = os.path.abspath("print_magazine.html")
    pdf_abs_path = os.path.abspath(pdf_output_name)

    print(f"Executando Chrome Headless para compilar: '{pdf_output_name}'...")
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_abs_path}",
        html_abs_path
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_abs_path):
        size_mb = os.path.getsize(pdf_abs_path) / (1024 * 1024)
        print(f"PDF gerado com sucesso na raiz: '{pdf_output_name}' ({size_mb:.2f} MB)")
    else:
        print(f"Erro ao gerar PDF: {res.stderr}")

if __name__ == "__main__":
    build_a4_magazine()
