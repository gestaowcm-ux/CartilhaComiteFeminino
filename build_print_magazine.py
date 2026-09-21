# -*- coding: utf-8 -*-
"""
Print / A4 PDF Builder for Cartilha Comitê Feminino ABRAMAN
Embeds all real images and sets exact A4 pagination
"""

def generate_print_magazine():
    css_print = """
    @page {
        size: A4 portrait;
        margin: 0;
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        font-family: 'Inter', sans-serif;
        background: #FFFFFF;
        color: #1E293B;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
    }

    .print-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: #0B192C;
        color: white;
        padding: 12px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 9999;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    .print-btn {
        background: #E11D48;
        color: white;
        border: none;
        padding: 8px 18px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 14px;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }

    @media print {
        .print-bar {
            display: none !important;
        }
    }

    .print-container {
        width: 210mm;
        margin: 0 auto;
        padding-top: 60px;
    }

    @media print {
        .print-container {
            width: 210mm;
            padding-top: 0;
        }
    }

    .mag-page {
        width: 210mm;
        height: 297mm;
        max-height: 297mm;
        page-break-before: always;
        position: relative;
        background: white;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .mag-page:first-child {
        page-break-before: auto;
    }

    .mag-page.full-bleed-cover {
        padding: 0;
        background: #000;
    }

    .mag-page.full-bleed-cover img.cover-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .page-inner {
        padding: 16mm 18mm 14mm;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .page-editorial-header {
        display: flex;
        justify-content: space-between;
        border-bottom: 1.5px solid #FECDD3;
        padding-bottom: 3mm;
        margin-bottom: 4mm;
        font-size: 10px;
        font-weight: 700;
        color: #E11D48;
        text-transform: uppercase;
    }

    .chapter-badge {
        display: inline-block;
        background: #FFF1F2;
        border-left: 4px solid #E11D48;
        padding: 2mm 4mm;
        font-size: 9.5px;
        font-weight: 800;
        color: #9F1239;
        text-transform: uppercase;
        margin-bottom: 2mm;
    }

    .chapter-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 18px;
        font-weight: 800;
        color: #0B192C;
        line-height: 1.25;
        margin-bottom: 3mm;
    }

    .section-subtitle {
        font-family: 'Montserrat', sans-serif;
        font-size: 12px;
        font-weight: 700;
        color: #E11D48;
        margin-top: 2.5mm;
        margin-bottom: 1.5mm;
    }

    .quote-highlight {
        background: #FFF1F2;
        border-left: 4px solid #E11D48;
        padding: 3mm 4.5mm;
        border-radius: 0 6px 6px 0;
        margin: 2.5mm 0;
    }

    .quote-highlight p {
        font-family: 'Playfair Display', serif;
        font-size: 11.5px;
        font-style: italic;
        color: #0B192C;
        line-height: 1.45;
    }

    p.editorial-lead {
        font-size: 11px;
        line-height: 1.5;
        color: #334155;
        margin-bottom: 2mm;
        text-align: justify;
    }

    .cards-grid-2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3mm;
        margin: 2.5mm 0;
    }

    .cards-grid-3 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 2mm;
        margin: 2mm 0;
    }

    .info-card {
        border: 1px solid #E2E8F0;
        border-top: 3px solid #FB7185;
        border-radius: 6px;
        padding: 2.5mm;
        background: #FFFFFF;
    }

    .info-card-header {
        display: flex;
        align-items: center;
        gap: 1.5mm;
        margin-bottom: 1.5mm;
    }

    .info-card-icon {
        width: 16px;
        height: 16px;
        border-radius: 4px;
        background: #FFE4E6;
        color: #E11D48;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 9px;
        font-weight: bold;
    }

    .info-card-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 10.5px;
        font-weight: 700;
        color: #0B192C;
    }

    .info-card p {
        font-size: 9.5px;
        line-height: 1.35;
        color: #475569;
    }

    .editorial-img-card {
        border-radius: 6px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
        margin: 2.5mm 0;
    }

    .editorial-img-card img {
        width: 100%;
        height: auto;
        display: block;
    }

    .action-box {
        border-radius: 6px;
        padding: 3mm 4mm;
        margin: 2.5mm 0;
    }

    .action-box.box-leadership {
        background: #EFF6FF;
        border-left: 4px solid #1E3A8A;
    }

    .action-box.box-best-practices {
        background: #FFF1F2;
        border-left: 4px solid #E11D48;
    }

    .action-box.box-key-message {
        background: #0B192C;
        color: white;
    }

    .action-box.box-reflection {
        background: #FFFBEB;
        border-left: 4px solid #F59E0B;
    }

    .box-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 10.5px;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 1.5mm;
    }

    .action-list {
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: 1.2mm;
    }

    .action-list li {
        font-size: 10px;
        line-height: 1.3;
        color: #1E293B;
    }

    .checklist-item {
        display: flex;
        align-items: flex-start;
        gap: 1.5mm;
        margin-bottom: 1mm;
        font-size: 10px;
        color: #78350F;
    }

    .stat-banner {
        display: flex;
        align-items: center;
        gap: 3.5mm;
        background: #FFF1F2;
        border: 1px dashed #FDA4AF;
        border-radius: 6px;
        padding: 2.5mm;
        margin: 2mm 0;
    }

    .stat-number {
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 900;
        color: #E11D48;
        line-height: 1;
    }

    .stat-desc {
        font-size: 10px;
        line-height: 1.35;
        color: #0B192C;
    }

    .broken-rung-diagram {
        background: #0B192C;
        border-radius: 6px;
        padding: 3mm;
        color: white;
        margin: 2mm 0;
    }

    .broken-rung-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 11px;
        font-weight: 800;
        color: #FB7185;
        margin-bottom: 2mm;
        text-align: center;
    }

    .rung-bars {
        display: flex;
        flex-direction: column;
        gap: 1.5mm;
    }

    .rung-item {
        display: flex;
        align-items: center;
        gap: 2mm;
    }

    .rung-label {
        width: 120px;
        font-size: 9px;
        color: #CBD5E1;
        text-align: right;
    }

    .rung-progress-track {
        flex: 1;
        height: 14px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 7px;
        overflow: hidden;
    }

    .rung-progress-fill {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 2mm;
        font-size: 8.5px;
        font-weight: bold;
        color: white;
    }

    .page-editorial-footer {
        border-top: 1px solid #E2E8F0;
        padding-top: 2.5mm;
        display: flex;
        justify-content: space-between;
        font-size: 9px;
        color: #64748B;
    }

    .page-editorial-footer .page-number-tag {
        font-weight: 800;
        color: #E11D48;
        font-size: 10.5px;
    }
    """

    # Pages for A4 Print
    pages_print = []

    # Page 1: Capa (Full Bleed)
    pages_print.append("""
    <div class="mag-page full-bleed-cover">
        <img src="ChatGPT Image Aug 31, 2026, 07_59_24 PM.png" alt="Capa Oficial" class="cover-img">
    </div>
    """)

    # Page 2: Institucional
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header">
                <span><i class="fa-solid fa-ribbon"></i> ABRAMAN Mulher • DIA</span>
                <span>Apresentação Institucional</span>
            </div>

            <div style="text-align: center; margin-bottom: 3mm;">
                <span class="chapter-badge">Guia Oficial de Boas Práticas</span>
                <h1 class="chapter-title" style="font-size: 16px; margin-bottom: 2mm;">Diversidade de Gênero na Manutenção e Gestão de Ativos</h1>
                <p style="font-size: 10.5px; font-weight: 700; color: #E11D48;">Guia para Lideranças e Organizações</p>
            </div>

            <div class="action-box box-leadership">
                <div class="box-title">Mensagem da Presidente da ABRAMAN</div>
                <p class="editorial-lead">A manutenção e a gestão de ativos vivem um momento de transformação impulsionado pela inovação, pela digitalização e pelo desenvolvimento de pessoas. Nesse cenário, ampliar a diversidade de perspectivas é fundamental para fortalecer a capacidade das organizações de responder aos desafios atuais e futuros.</p>
                <p class="editorial-lead">Acreditamos que promover ambientes inclusivos significa criar condições para que talentos diversos possam contribuir plenamente para a segurança, a confiabilidade e a sustentabilidade dos nossos ativos.</p>
                <p class="editorial-lead" style="font-weight: 600; color: #1E3A8A;">Esta cartilha representa mais um passo do compromisso da ABRAMAN com a valorização das pessoas e o fortalecimento das lideranças.</p>
            </div>

            <div class="action-box box-best-practices">
                <div class="box-title">Mensagem do Comitê Feminino</div>
                <p class="editorial-lead">O Comitê Feminino da ABRAMAN nasceu com o propósito de ampliar a participação das mulheres na manutenção e na gestão de ativos, promovendo espaços de diálogo, desenvolvimento profissional e compartilhamento de experiências.</p>
                <p class="editorial-lead">Por meio do Subcomitê DIA, buscamos estimular reflexões e disseminar boas práticas que contribuam para ambientes de trabalho mais inclusivos, respeitosos e colaborativos.</p>
                <p class="editorial-lead" style="font-weight: 600; color: #BE123C;">Construir ambientes mais diversos é uma responsabilidade compartilhada e um caminho para organizações mais preparadas para o futuro.</p>
            </div>

            <div class="page-editorial-footer">
                <span>Comitê Feminino ABRAMAN • Subcomitê DIA</span>
                <span class="page-number-tag">02</span>
            </div>
        </div>
    </div>
    """)

    # Page 3: Sumário
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header">
                <span><i class="fa-solid fa-list-ol"></i> Sumário</span>
                <span>Índice Geral</span>
            </div>

            <span class="chapter-badge">Sumário Executivo</span>
            <h2 class="chapter-title" style="margin-bottom: 3mm;">Conteúdo da Cartilha</h2>

            <div class="cards-grid-2" style="gap: 2mm;">
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">01</span><h4 class="info-card-title">Por que esta cartilha?</h4></div><p>Transformação estratégica e inovação.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">02</span><h4 class="info-card-title">Entendendo a Diversidade</h4></div><p>Diversidade, Inclusão, Equidade e Pertencimento.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">03</span><h4 class="info-card-title">Manutenção & Ativos</h4></div><p>Impacto nas decisões técnicas e confiabilidade.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">04</span><h4 class="info-card-title">Diversidade em Números</h4></div><p>Diferenças salariais e o Broken Rung.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">05</span><h4 class="info-card-title">Desafios das Mulheres</h4></div><p>Obstáculos, liderança inclusiva e boas práticas.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">06</span><h4 class="info-card-title">Carreira & Sucessão</h4></div><p>Fatores de propulsão e critérios claros.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">07</span><h4 class="info-card-title">Maternidade</h4></div><p>Preservação de talentos e acolhimento.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">08</span><h4 class="info-card-title">Maternidade Atípica</h4></div><p>Apoio às famílias com necessidades específicas.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">09</span><h4 class="info-card-title">Barreiras Físicas</h4></div><p>EPIs adaptados, ergonomia e instalações.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">10/11</span><h4 class="info-card-title">Cultura & Microagressões</h4></div><p>Combate a vieses e ações no cotidiano.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">12</span><h4 class="info-card-title">Homens como Aliados</h4></div><p>Papel ativo da liderança masculina.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">13-14</span><h4 class="info-card-title">Comitê, Futuro & Manifesto</h4></div><p>Compromisso com o futuro e palavras finais.</p></div>
            </div>

            <div class="page-editorial-footer">
                <span>Sumário Geral da Publicação</span>
                <span class="page-number-tag">03</span>
            </div>
        </div>
    </div>
    """)

    # Page 4: Cap 1
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 01</span><span>Visão Estratégica</span></div>
            <span class="chapter-badge">Introdução</span>
            <h2 class="chapter-title">Por que esta cartilha?</h2>
            <p class="editorial-lead">As organizações vivem um momento de profundas transformações. Novas tecnologias, mudanças no perfil da força de trabalho, maior complexidade operacional e a necessidade crescente de inovação exigem ambientes capazes de reunir diferentes conhecimentos, experiências e perspectivas.</p>
            <p class="editorial-lead">Nesse contexto, a diversidade de gênero deixa de ser apenas uma pauta relacionada à responsabilidade social para tornar-se um <strong>elemento estratégico</strong> para o fortalecimento das organizações.</p>
            <div style="background: #FFF1F2; border: 1px solid #FECDD3; border-radius: 6px; padding: 2.5mm; margin: 2mm 0;">
                <div class="cards-grid-2" style="margin:0; gap:2mm;">
                    <div>💡 <strong>Inovação Contínua:</strong> soluções multidisciplinares.</div>
                    <div>🛡️ <strong>Segurança Operacional:</strong> mitigação de riscos.</div>
                    <div>⚙️ <strong>Confiabilidade de Ativos:</strong> decisão consistente.</div>
                    <div>💖 <strong>Valorização Humana:</strong> cultura inclusiva.</div>
                </div>
            </div>
            <p class="editorial-lead">Esta cartilha foi desenvolvida pelo Subcomitê DIA do Comitê Feminino da ABRAMAN com o objetivo de compartilhar práticas que contribuam para que a diversidade fortaleça pessoas, processos e resultados.</p>
            <div class="action-box box-key-message">
                <div class="box-title">Nosso Propósito</div>
                <p>Contribuir para que a diversidade seja compreendida como uma estratégia viva para fortalecer pessoas, processos e resultados.</p>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 01 • Por que esta cartilha?</span><span class="page-number-tag">04</span></div>
        </div>
    </div>
    """)

    # Page 5: Cap 2 com Foto Oficial
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 02</span><span>Conceitos Fundamentais</span></div>
            <span class="chapter-badge">Fundamentos</span>
            <h2 class="chapter-title">Entendendo a Diversidade de Gênero</h2>
            <p class="editorial-lead"><strong>Diversidade de gênero</strong> refere-se ao reconhecimento e ao respeito às diferentes identidades e expressões de gênero, assegurando oportunidades de participação, desenvolvimento e crescimento profissional.</p>
            
            <div class="editorial-img-card" style="max-height: 55mm; overflow:hidden;">
                <img src="assets/img_cap2_diversidade.jpg" alt="Diversidade na Prática" style="height: 55mm; object-fit: cover;">
            </div>

            <div class="cards-grid-2" style="gap: 2mm;">
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">1</span><h4 class="info-card-title">Diversidade</h4></div><p>Presença de diferentes trajetórias. <em>"Quem faz parte?"</em></p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">2</span><h4 class="info-card-title">Inclusão</h4></div><p>Condições para participar ativamente. <em>"Quem participa?"</em></p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">3</span><h4 class="info-card-title">Equidade</h4></div><p>Apoio compatível com necessidades reais de cada pessoa.</p></div>
                <div class="info-card"><div class="info-card-header"><span class="info-card-icon">4</span><h4 class="info-card-title">Acessibilidade</h4></div><p>Eliminação de barreiras físicas e comunicacionais.</p></div>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 02 • Entendendo a Diversidade</span><span class="page-number-tag">05</span></div>
        </div>
    </div>
    """)

    # Page 6: Cap 3 com Imagem Oficial
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 03</span><span>Impacto Setorial</span></div>
            <span class="chapter-badge">Relevância Operacional</span>
            <h2 class="chapter-title">Diversidade na Manutenção & Ativos</h2>
            <p class="editorial-lead">Os setores de manutenção e gestão de ativos desempenham papel estratégico na continuidade operacional das organizações. Suas decisões influenciam diretamente a disponibilidade dos ativos, a segurança das pessoas, a gestão de riscos e os custos operacionais.</p>
            
            <div class="editorial-img-card" style="max-height: 50mm; overflow:hidden;">
                <img src="assets/img_cap3_manutencao.png" alt="Gestão de Ativos" style="height: 50mm; object-fit: cover;">
            </div>

            <div class="action-box box-reflection">
                <div class="box-title">Para refletir</div>
                <p style="font-size: 10.5px; font-weight: 600; color: #78350F;">"Sua organização possui diversidade suficiente para enfrentar problemas complexos sob diferentes perspectivas?"</p>
            </div>
            <div class="action-box box-key-message">
                <div class="box-title">Mensagem-chave</div>
                <p>"A diversidade fortalece pessoas. Pessoas fortalecem processos. Processos fortalecem resultados."</p>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 03 • Diversidade na Manutenção</span><span class="page-number-tag">06</span></div>
        </div>
    </div>
    """)

    # Page 7: Cap 4 Números
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 04</span><span>Panorama de Dados</span></div>
            <span class="chapter-badge">Estatísticas</span>
            <h2 class="chapter-title">Diversidade de Gênero em Números</h2>
            <div class="stat-banner">
                <div class="stat-number">-20,9%</div>
                <div class="stat-desc"><strong>Diferença Salarial no Brasil:</strong> Segundo o 3º Relatório de Transparência Salarial (RAIS 2024), mulheres recebem em média 20,9% menos em empresas com 100+ empregados.</div>
            </div>
            <div class="broken-rung-diagram">
                <div class="broken-rung-title">O Fenômeno "Broken Rung" (Degrau Quebrado)</div>
                <div class="rung-bars">
                    <div class="rung-item"><div class="rung-label">Homens promovidos a gestor:</div><div class="rung-progress-track"><div class="rung-progress-fill" style="width: 100%; background: #1E3A8A;">100</div></div></div>
                    <div class="rung-item"><div class="rung-label">Mulheres promovidas:</div><div class="rung-progress-track"><div class="rung-progress-fill" style="width: 81%; background: #F43F5E;">81</div></div></div>
                    <div class="rung-item"><div class="rung-label">Mulheres Negras promovidas:</div><div class="rung-progress-track"><div class="rung-progress-fill" style="width: 53%; background: #BE123C;">53</div></div></div>
                    <div class="rung-item"><div class="rung-label">Alta Liderança Feminina:</div><div class="rung-progress-track"><div class="rung-progress-fill" style="width: 29%; background: #F59E0B;">29%</div></div></div>
                </div>
            </div>
            <p class="editorial-lead">Os dados demonstram que a principal barreira ocorre logo no início da trajetória gerencial e não está ligada à competência, mas aos obstáculos acumulados.</p>
            <div class="page-editorial-footer"><span>Capítulo 04 • Diversidade em Números</span><span class="page-number-tag">07</span></div>
        </div>
    </div>
    """)

    # Page 8: Cap 5 Desafios
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 05</span><span>Desafios Cotidianos (1/2)</span></div>
            <span class="chapter-badge">Barreiras Estruturais</span>
            <h2 class="chapter-title">Os Desafios das Mulheres no Trabalho</h2>
            <div class="quote-highlight">
                <p>"Os maiores desafios para a equidade nem sempre são visíveis. Muitos estão presentes nas decisões cotidianas e nos vieses que influenciam como avaliamos pessoas."</p>
            </div>
            <div class="cards-grid-3">
                <div class="info-card"><h5 class="info-card-title">Pouca Representatividade</h5><p>Pouca presença feminina em campo e equipes técnicas.</p></div>
                <div class="info-card"><h5 class="info-card-title">Estereótipos</h5><p>Crenças sobre papéis "mais adequados".</p></div>
                <div class="info-card"><h5 class="info-card-title">Viés Inconsciente</h5><p>Atalhos mentais que influenciam avaliações.</p></div>
                <div class="info-card"><h5 class="info-card-title">Desigualdade</h5><p>Acesso reduzido a projetos estratégicos.</p></div>
                <div class="info-card"><h5 class="info-card-title">Maternidade</h5><p>Pressupostos sobre disponibilidade.</p></div>
                <div class="info-card"><h5 class="info-card-title">Barreiras Físicas</h5><p>Falta de EPIs adaptados e vestiários.</p></div>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 05 • Desafios das Mulheres</span><span class="page-number-tag">08</span></div>
        </div>
    </div>
    """)

    # Page 9: Cap 5 Liderança
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 05</span><span>Ações Práticas (2/2)</span></div>
            <span class="chapter-badge">Práticas de Liderança</span>
            <h2 class="chapter-title">Liderança Inclusiva & Boas Práticas</h2>
            <div class="action-box box-leadership">
                <div class="box-title">Liderança Inclusiva na Prática</div>
                <ul class="action-list">
                    <li>• Distribuir oportunidades com base em competências e desempenho;</li>
                    <li>• Estimular a participação técnica de todas e dar feedbacks objetivos;</li>
                    <li>• Agir rapidamente diante de comportamentos discriminatórios.</li>
                </ul>
            </div>
            <div class="action-box box-best-practices">
                <div class="box-title">Boas Práticas Organizacionais</div>
                <ul class="action-list">
                    <li>• Processos transparentes de recrutamento e promoção;</li>
                    <li>• Capacitação contínua sobre liderança inclusiva e canais seguros.</li>
                </ul>
            </div>
            <div class="action-box box-reflection">
                <div class="box-title">Para refletir — Sua organização:</div>
                <div class="checklist-item">☐ Acompanha indicadores de diversidade?</div>
                <div class="checklist-item">☐ Possui mulheres em funções técnicas e operacionais?</div>
                <div class="checklist-item">☐ Oferece oportunidades iguais de desenvolvimento?</div>
                <div class="checklist-item">☐ Monitora promoções por gênero e liderança?</div>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 05 • Liderança Inclusiva</span><span class="page-number-tag">09</span></div>
        </div>
    </div>
    """)

    # Page 10: Cap 6 Carreira
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 06</span><span>Carreira & Sucessão</span></div>
            <span class="chapter-badge">Ascensão Profissional</span>
            <h2 class="chapter-title">Desenvolvimento & Carreira</h2>
            <div class="quote-highlight">
                <p>"O talento abre portas. A equidade garante que todas as pessoas tenham a oportunidade de atravessá-las."</p>
            </div>
            <div class="cards-grid-2">
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 10px; font-weight:600;">📁 Projetos estratégicos & campo</div>
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 10px; font-weight:600;">🎓 Treinamentos e certificações</div>
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 10px; font-weight:600;">🤝 Mentoria & patrocínio</div>
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 10px; font-weight:600;">⚖️ Critérios transparentes</div>
            </div>
            <div class="action-box box-reflection">
                <div class="box-title">Para refletir:</div>
                <div class="checklist-item">☐ Mulheres participam dos principais projetos?</div>
                <div class="checklist-item">☐ Existe equilíbrio na distribuição de treinamentos?</div>
                <div class="checklist-item">☐ Há mulheres no plano de sucessão técnica e gerencial?</div>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 06 • Desenvolvimento Profissional</span><span class="page-number-tag">10</span></div>
        </div>
    </div>
    """)

    # Page 11: Cap 7 Maternidade com Fotos Reais
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 07</span><span>Parentalidade & Retenção</span></div>
            <span class="chapter-badge">Acolhimento</span>
            <h2 class="chapter-title">Maternidade</h2>
            <p style="font-size: 10.5px; font-weight: 700; color: #E11D48;">Valorizando pessoas e preservando talentos</p>
            <div class="quote-highlight">
                <p>"A maternidade não reduz o potencial de uma profissional. Organizações inclusivas reconhecem diferentes momentos da vida sem limitar oportunidades."</p>
            </div>
            <div class="cards-grid-2">
                <div class="editorial-img-card" style="height: 48mm; overflow:hidden;"><img src="assets/img_cap7_maternidade_1.jpg" alt="Maternidade" style="height: 48mm; object-fit: cover;"></div>
                <div class="editorial-img-card" style="height: 48mm; overflow:hidden;"><img src="assets/img_cap7_maternidade_2.jpg" alt="Acolhimento" style="height: 48mm; object-fit: cover;"></div>
            </div>
            <div class="action-box box-best-practices">
                <div class="box-title">Boas Práticas</div>
                <ul class="action-list">
                    <li>• Programas de retorno e salas de apoio à amamentação;</li>
                    <li>• <strong>Suporte Psicológico</strong> e <strong>corresponsabilidade parental</strong>.</li>
                </ul>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 07 • Maternidade</span><span class="page-number-tag">11</span></div>
        </div>
    </div>
    """)

    # Page 12: Cap 8 Maternidade Atípica com Fotos Reais
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 08</span><span>Inclusão Especializada</span></div>
            <span class="chapter-badge">Equidade Real</span>
            <h2 class="chapter-title">Maternidade Atípica</h2>
            <div class="quote-highlight">
                <p>"Equidade começa quando compreendemos que pessoas diferentes enfrentam desafios diferentes e precisam de apoios distintos."</p>
            </div>
            <p class="editorial-lead">Refere-se à experiência de mães que cuidam de filhos com deficiência, neurodivergência ou condições crônicas de saúde.</p>
            <div class="cards-grid-2">
                <div class="editorial-img-card" style="height: 48mm; overflow:hidden;"><img src="assets/img_cap8_maternidade_atipica_1.jpg" alt="Maternidade Atípica" style="height: 48mm; object-fit: cover;"></div>
                <div class="editorial-img-card" style="height: 48mm; overflow:hidden;"><img src="assets/img_cap8_maternidade_atipica_2.jpg" alt="Apoio" style="height: 48mm; object-fit: cover;"></div>
            </div>
            <div class="action-box box-reflection">
                <div class="box-title">Para refletir:</div>
                <div class="checklist-item">☐ Reconhece a maternidade atípica como tema de inclusão?</div>
                <div class="checklist-item">☐ Possui flexibilidade e ambiente psicologicamente seguro?</div>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 08 • Maternidade Atípica</span><span class="page-number-tag">12</span></div>
        </div>
    </div>
    """)

    # Page 13: Cap 9 Barreiras Físicas
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 09</span><span>Infraestrutura & Segurança</span></div>
            <span class="chapter-badge">Acessibilidade</span>
            <h2 class="chapter-title">Barreiras Físicas</h2>
            <div class="quote-highlight">
                <p>"Um ambiente inclusivo não exige que as pessoas se adaptem ao espaço. É o espaço que deve estar preparado para acolher a diversidade."</p>
            </div>
            <div class="action-box box-best-practices">
                <div class="box-title">Boas Práticas Organizacionais</div>
                <ul class="action-list">
                    <li>• <strong>EPIs adaptados:</strong> tamanhos, modelagens e biotipos adequados;</li>
                    <li>• <strong>Vestiários & sanitários:</strong> conforto, privacidade e segurança;</li>
                    <li>• <strong>Ferramentas ergonômicas</strong> e critérios inclusivos em novos projetos industriais.</li>
                </ul>
            </div>
            <div class="action-box box-reflection">
                <div class="box-title">Para refletir:</div>
                <div class="checklist-item">☐ Possui EPIs desenvolvidos para diferentes biotipos?</div>
                <div class="checklist-item">☐ As instalações oferecem conforto e segurança a todas?</div>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 09 • Barreiras Físicas</span><span class="page-number-tag">13</span></div>
        </div>
    </div>
    """)

    # Page 14: Cap 10 Barreiras Culturais
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 10</span><span>Cultura Organizacional</span></div>
            <span class="chapter-badge">Comportamento</span>
            <h2 class="chapter-title">Barreiras Culturais</h2>
            <div class="quote-highlight">
                <p>"As barreiras mais difíceis nem sempre são visíveis. Muitas estão presentes nas crenças e decisões diárias."</p>
            </div>
            <div class="cards-grid-2">
                <div class="info-card"><h4 class="info-card-title">Liderança Inclusiva</h4><p>Promove segurança psicológica e combate preconceitos.</p></div>
                <div class="info-card"><h4 class="info-card-title">Capacitação</h4><p>Treinamentos sobre vieses e critérios objetivos.</p></div>
            </div>
            <div class="action-box box-reflection">
                <div class="box-title">Para refletir:</div>
                <p style="font-size: 10.5px; font-weight: 600; color: #78350F;">"Suas decisões são pautadas em competências comprovadas ou em pressupostos inconscientes?"</p>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 10 • Barreiras Culturais</span><span class="page-number-tag">14</span></div>
        </div>
    </div>
    """)

    # Page 15: Cap 11 Microagressões
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 11</span><span>Relações & Respeito</span></div>
            <span class="chapter-badge">Conscientização</span>
            <h2 class="chapter-title">Microagressões</h2>
            <div class="quote-highlight">
                <p>"Nem todo comportamento inadequado é intencional. Mas todo comportamento gera impacto."</p>
            </div>
            <div class="cards-grid-2">
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 9.5px;">⚠️ Interromper em reuniões.</div>
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 9.5px;">⚠️ Presumir função de apoio.</div>
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 9.5px;">⚠️ Surpresa com competência técnica.</div>
                <div style="background: #FFF1F2; padding: 2mm; border-radius: 4px; font-size: 9.5px;">⚠️ Focar na aparência.</div>
            </div>
            <div class="cards-grid-2">
                <div class="action-box box-leadership"><div class="box-title">Se presenciar:</div><p style="font-size: 9.5px;">Interrompa com respeito e devolva a palavra.</p></div>
                <div class="action-box box-best-practices"><div class="box-title">Se praticou:</div><p style="font-size: 9.5px;">Escute sem defensividade e reconheça o impacto.</p></div>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 11 • Microagressões</span><span class="page-number-tag">15</span></div>
        </div>
    </div>
    """)

    # Page 16: Cap 12 Aliados
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulo 12</span><span>Alianças & Liderança</span></div>
            <span class="chapter-badge">Engajamento</span>
            <h2 class="chapter-title">Homens como Aliados</h2>
            <div class="quote-highlight">
                <p>"Construir ambientes inclusivos não é responsabilidade de um grupo específico. É um compromisso coletivo."</p>
            </div>
            <div class="cards-grid-3">
                <div class="info-card"><h5 class="info-card-title">Ouvir</h5><p>Escutar experiências sem desmerecer.</p></div>
                <div class="info-card"><h5 class="info-card-title">Patrocinar</h5><p>Compartilhar oportunidades em campo.</p></div>
                <div class="info-card"><h5 class="info-card-title">Posicionar-se</h5><p>Não tolerar atitudes desrespeitosas.</p></div>
            </div>
            <div class="action-box box-leadership">
                <div class="box-title">Liderança Masculina na Prática</div>
                <ul class="action-list">
                    <li>• Distribuir posições técnicas com imparcialidade;</li>
                    <li>• Estimular a formação de novas lideranças femininas;</li>
                    <li>• Tornar reuniões e campo espaços seguros para todos.</li>
                </ul>
            </div>
            <div class="page-editorial-footer"><span>Capítulo 12 • Homens como Aliados</span><span class="page-number-tag">16</span></div>
        </div>
    </div>
    """)

    # Page 17: Cap 13 & 14 com Banner Oficial
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Capítulos 13 & 14</span><span>Visão Institucional</span></div>
            <div class="cards-grid-2">
                <div style="background: #FFF1F2; border-radius: 6px; padding: 2mm;"><h4 style="font-size: 10.5px; color: #0B192C;">Comitê Feminino & DIA</h4><p style="font-size: 9.5px;">Espaço permanente de diálogo, capacitação e estudos técnicos.</p></div>
                <div style="background: #EFF6FF; border-radius: 6px; padding: 2mm;"><h4 style="font-size: 10.5px; color: #0B192C;">Compromisso Futuro</h4><p style="font-size: 9.5px;">Transformação contínua para a excelência na gestão de ativos.</p></div>
            </div>
            <div class="editorial-img-card" style="margin: 2mm 0;"><img src="BannerFeminino.jpg" alt="Comitê Feminino ABRAMAN"></div>
            <div class="action-box box-best-practices">
                <div class="box-title">Compromissos</div>
                <ul class="action-list">
                    <li>• Fortalecer políticas e indicadores de diversidade;</li>
                    <li>• Ampliar a participação feminina em todas as áreas e níveis.</li>
                </ul>
            </div>
            <div class="page-editorial-footer"><span>Capítulos 13 e 14 • O Papel do Comitê & Futuro</span><span class="page-number-tag">17</span></div>
        </div>
    </div>
    """)

    # Page 18: Palavras Finais
    pages_print.append("""
    <div class="mag-page">
        <div class="page-inner">
            <div class="page-editorial-header"><span>Mensagem Final</span><span>Encerramento</span></div>
            <span class="chapter-badge">Mensagem Final</span>
            <h2 class="chapter-title">Palavras Finais</h2>
            <p class="editorial-lead">A diversidade de gênero não representa apenas uma oportunidade de ampliar a representatividade feminina. Ela representa a possibilidade de construir organizações mais inovadoras, colaborativas, resilientes e preparadas para responder aos desafios de um setor em constante transformação.</p>
            <p class="editorial-lead">Na manutenção e gestão de ativos, onde decisões técnicas impactam diretamente a segurança das pessoas, a confiabilidade dos ativos e a sustentabilidade dos negócios, ampliar a diversidade significa fortalecer a capacidade de aprender, inovar e evoluir continuamente.</p>
            <div class="quote-highlight">
                <p>"Construir ambientes inclusivos não é responsabilidade exclusiva de um grupo. É um compromisso compartilhado por todos que acreditam que equipes diversas produzem soluções mais completas e organizações mais fortes."</p>
            </div>
            <p class="editorial-lead" style="font-weight: 600;">Que esta cartilha seja um convite à reflexão, mas, sobretudo, à ação.</p>
            <div class="page-editorial-footer"><span>Comitê Feminino ABRAMAN • Palavras Finais</span><span class="page-number-tag">18</span></div>
        </div>
    </div>
    """)

    # Page 19: Contracapa (Full Bleed)
    pages_print.append("""
    <div class="mag-page full-bleed-cover">
        <img src="ChatGPT Image Aug 30, 2026, 10_42_56 AM.png" alt="Contracapa Oficial" class="cover-img">
    </div>
    """)

    joined_print_pages = "\n".join(pages_print)

    html_print_doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Revista Digital ABRAMAN Mulher • Versão Impressão / PDF A4</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Montserrat:wght@500;600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        {css_print}
    </style>
</head>
<body>
    <div class="print-bar">
        <div style="display: flex; align-items: center; gap: 10px;">
            <i class="fa-solid fa-print" style="color: #FB7185; font-size: 18px;"></i>
            <strong>Revista Digital: Comitê Feminino ABRAMAN • Exportação PDF A4</strong>
        </div>
        <button class="print-btn" onclick="window.print()">
            <i class="fa-solid fa-download"></i> Imprimir / Salvar em PDF (Ctrl + P)
        </button>
    </div>

    <div class="print-container">
        {joined_print_pages}
    </div>
</body>
</html>
"""

    with open("print_magazine.html", "w", encoding="utf-8") as f:
        f.write(html_print_doc)
    print("Updated print_magazine.html with all real images and A4 formatting!")

if __name__ == '__main__':
    generate_print_magazine()
