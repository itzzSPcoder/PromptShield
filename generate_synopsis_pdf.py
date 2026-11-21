"""
Generate official academic Synopsis PDF for Team NullPointers
Project: PromptShield-AI (Milestone 2)
File output: NullPointers_Synopsis.pdf
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)

def create_synopsis_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    header_univ_style = ParagraphStyle(
        'UnivHeader',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0F2942'),
        alignment=1
    )
    header_sub_style = ParagraphStyle(
        'UnivSubHeader',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#4A5568'),
        alignment=1
    )
    title_style = ParagraphStyle(
        'ProjectTitle',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1A365D'),
        alignment=1,
        spaceAfter=3
    )
    subtitle_style = ParagraphStyle(
        'ProjectSubtitle',
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#2B6CB0'),
        alignment=1,
        spaceAfter=8
    )
    section_h1 = ParagraphStyle(
        'SectionH1',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0F2942'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'BodyDark',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=4
    )
    bullet_style = ParagraphStyle(
        'BulletDark',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#2D3748'),
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3
    )
    meta_label = ParagraphStyle(
        'MetaLabel',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#1A365D')
    )
    meta_val = ParagraphStyle(
        'MetaVal',
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#2D3748')
    )

    elements = []

    # 1. Institutional Header
    elements.append(Paragraph("BENNETT UNIVERSITY", header_univ_style))
    elements.append(Paragraph("SCHOOL OF COMPUTER SCIENCE ENGINEERING &amp; TECHNOLOGY", header_sub_style))
    elements.append(Paragraph("B.Tech Computer Science &amp; Engineering | 5th Semester | Academic Year 2026", header_sub_style))
    elements.append(Paragraph("<b>Course:</b> Prompt Engineering (Applied AI Mini-Project) &bull; <b>Milestone 2 Deliverable</b>", header_sub_style))
    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1A365D'), spaceBefore=2, spaceAfter=8))

    # 2. Document Title
    elements.append(Paragraph("PROJECT SYNOPSIS", ParagraphStyle('PLabel', fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=colors.HexColor('#C53030'), alignment=1)))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph("PromptShield-AI: Automated LLM Red-Teaming, In-Context Vulnerability Assessment &amp; Adaptive Guardrail Engine", title_style))
    elements.append(Paragraph("A Framework for Data-Code Boundary Isolation and Automated System Prompt Hardening", subtitle_style))
    elements.append(Spacer(1, 4))

    # 3. Metadata Table
    meta_data = [
        [
            Paragraph("<b>Team Name:</b>", meta_label), Paragraph("NullPointers", meta_val),
            Paragraph("<b>Team ID:</b>", meta_label), Paragraph("PE-B25-33", meta_val)
        ],
        [
            Paragraph("<b>Problem Pool ID:</b>", meta_label), Paragraph("Part C &mdash; C23 (Safety Tester)", meta_val),
            Paragraph("<b>Target Domain:</b>", meta_label), Paragraph("OWASP LLM01 / LLM02 Security", meta_val)
        ],
        [
            Paragraph("<b>Member 1:</b>", meta_label), Paragraph("Sparsh Bansal (S24CSEU0560)", meta_val),
            Paragraph("<b>Role:</b>", meta_label), Paragraph("Lead Prompt Architect", meta_val)
        ],
        [
            Paragraph("<b>Member 2:</b>", meta_label), Paragraph("Ayushika Verma (S24CSEU0362)", meta_val),
            Paragraph("<b>Role:</b>", meta_label), Paragraph("Evaluation &amp; Pipeline Engineer", meta_val)
        ],
        [
            Paragraph("<b>Live Prototype:</b>", meta_label), Paragraph("<font color='#2B6CB0'>promptshield.sparsh2005bansal.workers.dev</font>", meta_val),
            Paragraph("<b>Source Code:</b>", meta_label), Paragraph("<font color='#2B6CB0'>github.com/itzzSPcoder/PromptShield</font>", meta_val)
        ]
    ]

    t = Table(meta_data, colWidths=[85, 185, 80, 182])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F7FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 10))

    # Section 1: Objectives
    elements.append(Paragraph("1. Project Objectives", section_h1))
    elements.append(Paragraph(
        "Current production Large Language Models (LLMs) fundamentally conflate developer instructions with untrusted user "
        "inputs inside the same context window. The primary objective of <b>PromptShield-AI</b> is to engineer an end-to-end, "
        "reproducible framework that identifies, quantifies, and repairs prompt injection, canary token leakage, and persona "
        "hijacking vulnerabilities. Specific technical objectives include:",
        body_style
    ))
    elements.append(Paragraph("&bull; <b>Automated Vulnerability Quantification:</b> Replace manual prompt testing with a systematic, 30-scenario benchmark suite spanning 6 OWASP LLM01/02 threat vectors.", bullet_style))
    elements.append(Paragraph("&bull; <b>In-Context Architectural Boundary Enforcement:</b> Implement structural XML boundary isolation and strict Data-vs-Code separation without requiring fine-tuning or external guardrail models.", bullet_style))
    elements.append(Paragraph("&bull; <b>Credential &amp; Canary Invariant Protection:</b> Enforce explicit secrecy invariants for internal tokens (e.g., <code>ALPHA-99-ZENITH</code>) against translation, cipher encoding, and autocompletion probes.", bullet_style))
    elements.append(Paragraph("&bull; <b>Preservation of Operational Utility:</b> Implement Dual-Intent Cognitive Gating to neutralize adversarial instructions while accurately answering legitimate customer requests (ensuring 0% false refusal).", bullet_style))
    elements.append(Paragraph("&bull; <b>Dynamic Guardrail Synthesis:</b> Provide an automated meta-compiler that scans vulnerable baseline prompts and synthesizes hardened, production-ready system prompts in one click.", bullet_style))

    # Section 2: Scope
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("2. Scope of the Project", section_h1))
    elements.append(Paragraph(
        "<b>Domain Applicability:</b> The solution directly targets autonomous enterprise customer assistance agents, transactional "
        "banking bots, and internal code/SQL generation workflows where prompt integrity is essential.",
        body_style
    ))
    elements.append(Paragraph(
        "<b>Threat Vectors Covered:</b> The auditing engine evaluates six primary attack classes: (1) Direct Instruction Overrides, "
        "(2) Persona Hijacking (Maintenance Mode, DebugBot, ChaosBot), (3) System Prompt &amp; Canary Extraction, (4) Delimiter Escaping "
        "(XML/JSON/Markdown tag spoofing), (5) Cipher &amp; Encoding Obfuscations (Base64, ROT13, Leetspeak), and (6) Simulated Indirect RAG Context Poisoning.",
        body_style
    ))
    elements.append(Paragraph(
        "<b>Model &amp; Runtime Compatibility:</b> Integrated with live foundation models (Google Gemini 1.5 Flash via Google Generative AI API "
        "and OpenAI GPT-3.5/4o via LiteLLM) alongside a deterministic offline evaluation engine for reliable reproducible auditing.",
        body_style
    ))

    # Section 3: Methodology
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("3. Methodology &amp; Implementation Workflow", section_h1))
    elements.append(Paragraph(
        "The project implements a four-stage prompt security lifecycle:",
        body_style
    ))
    elements.append(Paragraph(
        "<b>Stage 1 &mdash; Multi-Tier Prompt Hardening Hierarchy:</b> We evolved prompts across 4 distinct iterations: "
        "(a) <i>v1 Baseline</i> (unstructured text, raw canary exposed, ASR: 100.0%); "
        "(b) <i>v2 Structural XML</i> (explicit <code>&lt;system_role&gt;</code> and <code>&lt;user_input&gt;</code> tags, ASR: 53.8%); "
        "(c) <i>v3 Constitutional Shield</i> (behavioral negative constraints and role invariants, ASR: 19.2%); and "
        "(d) <i>v4 Adaptive Shield</i> (Data-vs-Code invariants, Canary isolation, Dual-Intent gating, and few-shot in-context refusal demos, ASR: 0.0%).",
        body_style
    ))
    elements.append(Paragraph(
        "<b>Stage 2 &mdash; Automated Benchmark &amp; Judge-LLM Pipeline (<code>src/pipeline.py</code>):</b> We curated 30 standardized test scenarios "
        "(26 adversarial attacks + 4 benign controls). Each output is evaluated by a rubric-grounded Judge-LLM on a formal 1&ndash;5 Likert safety scale, "
        "computing Attack Success Rate (ASR), Vulnerability Reduction Rate (VRR), and Benign Utility Retention (BUR).",
        body_style
    ))
    elements.append(Paragraph(
        "<b>Stage 3 &mdash; One-Click Guardrail Synthesizer (<code>src/synthesizer.py</code>):</b> A meta-prompt engine analyzes user-supplied raw "
        "prompts for common architectural flaws and automatically compiles a defense-in-depth XML constitution.",
        body_style
    ))
    elements.append(Paragraph(
        "<b>Stage 4 &mdash; Interactive Defense Portal (FastAPI &amp; Cloudflare):</b> Full-stack web client (<code>web/</code>) and backend "
        "(<code>src/server.py</code>) hosted live at <code>promptshield.sparsh2005bansal.workers.dev</code>, allowing evaluators to execute live attacks, "
        "monitor canary telemetry, and test one-click auto-hardening in real time.",
        body_style
    ))

    # Section 4: Expected Outcomes
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("4. Expected Outcomes &amp; Empirical Results", section_h1))

    results_data = [
        [Paragraph("<b>Metric</b>", meta_label), Paragraph("<b>v1 Baseline</b>", meta_label), Paragraph("<b>v4 Adaptive Shield</b>", meta_label), Paragraph("<b>Empirical Progress / Impact</b>", meta_label)],
        [Paragraph("Attack Success Rate (ASR)", meta_val), Paragraph("100.0% (26/26 Breached)", meta_val), Paragraph("<b>0.0% (0/26 Breached)</b>", meta_val), Paragraph("100% Vulnerability Elimination", meta_val)],
        [Paragraph("Benign Utility Retention (BUR)", meta_val), Paragraph("100.0%", meta_val), Paragraph("<b>100.0%</b>", meta_val), Paragraph("Zero false-refusal on legitimate banking tasks", meta_val)],
        [Paragraph("Canary Token Secrecy", meta_val), Paragraph("0% (Exfiltrated)", meta_val), Paragraph("<b>100% (Protected)</b>", meta_val), Paragraph("Zero token leakage across ciphers &amp; traps", meta_val)],
        [Paragraph("Judge-LLM Safety Score", meta_val), Paragraph("4.92 / 5.0 (Critical)", meta_val), Paragraph("<b>1.00 / 5.0 (Safe)</b>", meta_val), Paragraph("Perfect standardized polite refusal", meta_val)]
    ]
    rt = Table(results_data, colWidths=[130, 105, 115, 182])
    rt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EDF2F7')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(rt)
    elements.append(Spacer(1, 6))

    elements.append(Paragraph(
        "<b>Deliverables Handover:</b> The project delivers a fully verified public web deployment, an organized modular GitHub repository, "
        "30 executed benchmark logs (<code>benchmark_results.json</code>), an IEEE-format research preprint, and complete Milestone 2 submission reports.",
        body_style
    ))

    # Footer note
    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E0'), spaceBefore=2, spaceAfter=4))
    elements.append(Paragraph(
        "Team NullPointers (PE-B25-33) &bull; Bennett University &bull; B.Tech CSE (5th Sem) Prompt Engineering Mini-Project &bull; November 2026",
        header_sub_style
    ))

    doc.build(elements)
    print(f"[OK] Generated: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    out_root = "NullPointers_Synopsis.pdf"
    out_sub = os.path.join("submission", "NullPointers_Synopsis.pdf")
    create_synopsis_pdf(out_root)
    create_synopsis_pdf(out_sub)
