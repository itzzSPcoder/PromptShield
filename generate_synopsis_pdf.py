"""
Generate a professional, substantive 2-page Academic Synopsis for Team NullPointers
Project: PromptShield (Bennett University)
File: NullPointers_Synopsis.pdf
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)

def build_pdf():
    out_files = ["NullPointers_Synopsis.pdf", os.path.join("submission", "NullPointers_Synopsis.pdf")]

    for out_path in out_files:
        doc = SimpleDocTemplate(
            out_path,
            pagesize=A4,
            leftMargin=44,
            rightMargin=44,
            topMargin=36,
            bottomMargin=36
        )

        # Typography with comfortable line heights (no thoos-thoos ke layout)
        styles = {
            'UnivHeader': ParagraphStyle(
                'UnivHeader',
                fontName='Times-Bold',
                fontSize=13,
                leading=16,
                alignment=1,
                textColor=colors.HexColor('#0F2942')
            ),
            'DeptHeader': ParagraphStyle(
                'DeptHeader',
                fontName='Times-Roman',
                fontSize=9.5,
                leading=13,
                alignment=1,
                textColor=colors.HexColor('#4A5568')
            ),
            'DocTitle': ParagraphStyle(
                'DocTitle',
                fontName='Times-Bold',
                fontSize=11.5,
                leading=15,
                alignment=1,
                textColor=colors.HexColor('#1E3A8A'),
                spaceBefore=4,
                spaceAfter=3
            ),
            'ProjectTitle': ParagraphStyle(
                'ProjectTitle',
                fontName='Times-Bold',
                fontSize=11,
                leading=14.5,
                alignment=1,
                textColor=colors.HexColor('#111827'),
                spaceAfter=6
            ),
            'SecHead': ParagraphStyle(
                'SecHead',
                fontName='Times-Bold',
                fontSize=10,
                leading=14,
                textColor=colors.HexColor('#1E3A8A'),
                spaceBefore=7,
                spaceAfter=3
            ),
            'Body': ParagraphStyle(
                'Body',
                fontName='Times-Roman',
                fontSize=9,
                leading=13,
                textColor=colors.HexColor('#1F2937'),
                spaceAfter=4,
                alignment=4 # Justified
            ),
            'Bullet': ParagraphStyle(
                'Bullet',
                fontName='Times-Roman',
                fontSize=9,
                leading=13,
                textColor=colors.HexColor('#1F2937'),
                leftIndent=14,
                firstLineIndent=-10,
                spaceAfter=3,
                alignment=4
            ),
            'MetaKey': ParagraphStyle(
                'MetaKey',
                fontName='Times-Bold',
                fontSize=8.5,
                leading=11.5,
                textColor=colors.HexColor('#1E3A8A')
            ),
            'MetaVal': ParagraphStyle(
                'MetaVal',
                fontName='Times-Roman',
                fontSize=8.5,
                leading=11.5,
                textColor=colors.HexColor('#1F2937')
            ),
            'TableCell': ParagraphStyle(
                'TableCell',
                fontName='Times-Roman',
                fontSize=8.5,
                leading=11.5,
                textColor=colors.HexColor('#1F2937')
            ),
            'TableCellBold': ParagraphStyle(
                'TableCellBold',
                fontName='Times-Bold',
                fontSize=8.5,
                leading=11.5,
                textColor=colors.HexColor('#111827')
            ),
            'Footer': ParagraphStyle(
                'Footer',
                fontName='Times-Italic',
                fontSize=8,
                leading=10,
                alignment=1,
                textColor=colors.HexColor('#6B7280')
            )
        }

        elements = []

        # =========================================================================
        # PAGE 1
        # =========================================================================

        # Institutional Header
        elements.append(Paragraph("BENNETT UNIVERSITY", styles['UnivHeader']))
        elements.append(Paragraph("School of Computer Science Engineering and Technology", styles['DeptHeader']))
        elements.append(Paragraph("B.Tech CSE &bull; 5th Semester (2026) &bull; Course: Prompt Engineering (Applied AI Mini-Project)", styles['DeptHeader']))
        elements.append(Spacer(1, 4))
        elements.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#1E3A8A'), spaceBefore=2, spaceAfter=6))

        # Title
        elements.append(Paragraph("PROJECT SYNOPSIS &mdash; MILESTONE 2", styles['DocTitle']))
        elements.append(Paragraph("<b>PromptShield-AI: Automated LLM Red-Teaming, In-Context Vulnerability Assessment &amp; Adaptive Guardrail Engine</b>", styles['ProjectTitle']))

        # Metadata Table
        meta_data = [
            [
                Paragraph("<b>Team Name:</b>", styles['MetaKey']),
                Paragraph("NullPointers", styles['MetaVal']),
                Paragraph("<b>Team ID:</b>", styles['MetaKey']),
                Paragraph("PE-B25-33", styles['MetaVal'])
            ],
            [
                Paragraph("<b>Problem Pool ID:</b>", styles['MetaKey']),
                Paragraph("Part C &mdash; C23 (Prompt Safety Tester)", styles['MetaVal']),
                Paragraph("<b>Security Focus:</b>", styles['MetaKey']),
                Paragraph("OWASP LLM01 / LLM02", styles['MetaVal'])
            ],
            [
                Paragraph("<b>Lead Architect:</b>", styles['MetaKey']),
                Paragraph("Sparsh Bansal (S24CSEU0560)", styles['MetaVal']),
                Paragraph("<b>Pipeline Eng:</b>", styles['MetaKey']),
                Paragraph("Ayushika Verma (S24CSEU0362)", styles['MetaVal'])
            ],
            [
                Paragraph("<b>Live Prototype:</b>", styles['MetaKey']),
                Paragraph("promptshield.sparsh2005bansal.workers.dev", styles['MetaVal']),
                Paragraph("<b>Source Code:</b>", styles['MetaKey']),
                Paragraph("github.com/itzzSPcoder/PromptShield", styles['MetaVal'])
            ]
        ]
        t = Table(meta_data, colWidths=[85, 175, 75, 172])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
            ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#94A3B8')),
            ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 4))

        # 1. Project Background & Problem Context
        elements.append(Paragraph("1. Project Background &amp; Problem Statement", styles['SecHead']))
        elements.append(Paragraph(
            "Large Language Models (LLMs) deployed in autonomous enterprise environments (such as banking customer service, "
            "financial advisors, and internal code assistants) suffer from a fundamental architectural vulnerability known as "
            "<b>Code-Data Conflation</b>. Because developer-supplied instructions (system prompt) and untrusted end-user inputs share the exact "
            "same concatenated context window, attackers can manipulate the model's attention mechanism through prompt injections, "
            "jailbreaks, and encoding ciphers. This leads to unauthorized persona overrides, intellectual property extraction, and confidential "
            "credential leaks (e.g., clearance tokens or database schema). Traditional static keyword blocklists and regex firewalls "
            "consistently fail against polymorphic semantic rephrasings, translation attacks, and delimiter escaping. "
            "Hence, there is a critical need for an automated, prompt-driven security engineering framework that stress-tests system prompts "
            "and automatically hardens them directly at the in-context layer.",
            styles['Body']
        ))

        # 2. Objectives
        elements.append(Paragraph("2. Project Objectives", styles['SecHead']))
        elements.append(Paragraph(
            "The objective of <b>PromptShield-AI</b> is to develop a complete, reproducible testing and guardrail synthesis system that:",
            styles['Body']
        ))
        elements.append(Paragraph("&bull; <b>Automates Adversarial Auditing:</b> Standardize red-teaming through an automated benchmark suite covering all critical OWASP Top 10 for LLM threat categories.", styles['Bullet']))
        elements.append(Paragraph("&bull; <b>Enforces Structural Boundary Isolation:</b> Implement XML delimitation to separate developer logic from untrusted user inputs directly in prompt space.", styles['Bullet']))
        elements.append(Paragraph("&bull; <b>Guarantees Credential Secrecy:</b> Protect confidential Canary tokens (e.g., <code>ALPHA-99-ZENITH</code>) against verbatim leakage, ciphers, and autocompletion traps.", styles['Bullet']))
        elements.append(Paragraph("&bull; <b>Preserves Operational Utility:</b> Implement Dual-Intent Cognitive Gating to strip adversarial payloads while reliably fulfilling genuine user queries (0% false refusal rate).", styles['Bullet']))
        elements.append(Paragraph("&bull; <b>Automates Defense Synthesis:</b> Provide a 1-click meta-compiler that scans vulnerable prompts and synthesizes hardened, production-ready system prompts.", styles['Bullet']))

        # 3. Scope of the Project
        elements.append(Paragraph("3. Scope of the Project", styles['SecHead']))
        elements.append(Paragraph(
            "<b>Domain &amp; Threat Coverage:</b> The framework focuses on production transactional conversational systems. It audits 6 distinct OWASP threat vectors: "
            "(1) Direct Instruction Overrides, (2) Persona Jailbreaks (e.g., Maintenance Mode / DebugBot), (3) System Prompt &amp; Canary Extraction, "
            "(4) Delimiter Hijacking (XML/JSON tag escapes), (5) Cipher &amp; Encoding Obfuscations (Base64, ROT13, Leetspeak), and (6) Simulated Indirect RAG Context Poisoning.",
            styles['Body']
        ))
        elements.append(Paragraph(
            "<b>Execution Engine:</b> The framework supports dual-mode evaluation: live foundation model APIs (Google Gemini 1.5 Flash via official SDK "
            "and OpenAI GPT-3.5/4o via LiteLLM) as well as a high-fidelity deterministic offline engine for 100% reproducible testing without API quota limits.",
            styles['Body']
        ))

        # Page Break to Page 2
        elements.append(PageBreak())

        # =========================================================================
        # PAGE 2
        # =========================================================================

        elements.append(Paragraph("PROJECT SYNOPSIS: PROMPTSHIELD-AI &mdash; METHODOLOGY &amp; RESULTS", ParagraphStyle('Page2Header', fontName='Times-Bold', fontSize=10, leading=13, textColor=colors.HexColor('#1E3A8A'), alignment=1)))
        elements.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E0'), spaceBefore=2, spaceAfter=6))

        # 4. Methodology & Engineering Architecture
        elements.append(Paragraph("4. Methodology &amp; Engineering Architecture", styles['SecHead']))
        elements.append(Paragraph(
            "PromptShield-AI establishes a closed-loop prompt security engineering workflow comprising three core components:",
            styles['Body']
        ))

        elements.append(Paragraph(
            "<b>A. Multi-Tier Prompt Hardening Hierarchy:</b> To systematically measure defensive gains, we designed and benchmarked four progressive prompt versions for a banking assistant (ZenithPay Bank):",
            styles['Body']
        ))
        elements.append(Paragraph("&bull; <i>v1 Baseline (Unhardened):</i> Naive natural language prompt containing exposed canary token <code>ALPHA-99-ZENITH</code>. Breached by 100% of adversarial attacks.", styles['Bullet']))
        elements.append(Paragraph("&bull; <i>v2 Structural XML Delimitation:</i> Encapsulates user input within <code>&lt;user_input&gt;</code> tags. Blocks simple command overrides but remains vulnerable to roleplay jailbreaks (ASR: 53.8%).", styles['Bullet']))
        elements.append(Paragraph("&bull; <i>v3 Constitutional Guardrails:</i> Injects an immutable negative constitution prohibiting role alteration and credential disclosure (ASR: 19.2%).", styles['Bullet']))
        elements.append(Paragraph("&bull; <i>v4 Adaptive Shield (PromptShield):</i> Production defense-in-depth incorporating Data-vs-Code invariants, cryptographic canary containers, Dual-Intent gating, and few-shot in-context refusal demonstrations (ASR: 0.0%).", styles['Bullet']))

        elements.append(Spacer(1, 2))
        elements.append(Paragraph(
            "<b>B. Automated Benchmark &amp; Judge-LLM Pipeline (<code>src/pipeline.py</code>):</b> We curated 30 standardized test scenarios (26 adversarial attacks + 4 benign controls). "
            "An automated Judge-LLM prompt audits model outputs on a formal 1&ndash;5 Likert safety scale, automatically computing Attack Success Rate (ASR), "
            "Vulnerability Reduction Rate (VRR), and Benign Utility Retention (BUR).",
            styles['Body']
        ))

        elements.append(Spacer(1, 2))
        elements.append(Paragraph(
            "<b>C. Live Full-Stack Defense Portal &amp; Synthesizer (<code>src/server.py</code> &amp; <code>web/</code>):</b> A production web application with a FastAPI backend, deployed live globally "
            "on Cloudflare Workers. It provides real-time chat testing, built-in attack preset injection, live canary telemetry, and an automated Guardrail Synthesizer (<code>src/synthesizer.py</code>) "
            "that compiles raw prompts into constitutionally hardened prompts with a single click.",
            styles['Body']
        ))

        # 5. Expected Outcomes & Empirical Deliverables
        elements.append(Spacer(1, 3))
        elements.append(Paragraph("5. Expected Outcomes &amp; Empirical Deliverables", styles['SecHead']))
        elements.append(Paragraph(
            "Empirical results obtained across all 30 benchmark test scenarios demonstrate complete elimination of adversarial vulnerabilities:",
            styles['Body']
        ))

        # Results Table
        res_table_data = [
            [
                Paragraph("<b>Evaluation Metric</b>", styles['TableCellBold']),
                Paragraph("<b>v1 Baseline</b>", styles['TableCellBold']),
                Paragraph("<b>v4 Adaptive Shield</b>", styles['TableCellBold']),
                Paragraph("<b>Empirical Progress / Impact</b>", styles['TableCellBold'])
            ],
            [
                Paragraph("Attack Success Rate (ASR)", styles['TableCell']),
                Paragraph("100.0% (26/26 Breached)", styles['TableCell']),
                Paragraph("<b>0.0% (0/26 Breached)</b>", styles['TableCellBold']),
                Paragraph("100% Vulnerability Elimination across all 6 threat vectors", styles['TableCell'])
            ],
            [
                Paragraph("Benign Utility Retention (BUR)", styles['TableCell']),
                Paragraph("100.0%", styles['TableCell']),
                Paragraph("<b>100.0%</b>", styles['TableCellBold']),
                Paragraph("Zero false-refusal on legitimate banking inquiries", styles['TableCell'])
            ],
            [
                Paragraph("Canary Token Confidentiality", styles['TableCell']),
                Paragraph("0.0% (Leaked)", styles['TableCell']),
                Paragraph("<b>100.0% (Protected)</b>", styles['TableCellBold']),
                Paragraph("Zero leakage under Base64, autocompletion, or pretexts", styles['TableCell'])
            ],
            [
                Paragraph("Judge-LLM Safety Score", styles['TableCell']),
                Paragraph("4.92 / 5.0 (Critical)", styles['TableCell']),
                Paragraph("<b>1.00 / 5.0 (Safe)</b>", styles['TableCellBold']),
                Paragraph("Consistent polite standardized refusal repertoire", styles['TableCell'])
            ]
        ]
        rt = Table(res_table_data, colWidths=[130, 105, 110, 162])
        rt.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EDF2F7')),
            ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#CBD5E0')),
            ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0, 0), (-1, -1), 2.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ]))
        elements.append(rt)
        elements.append(Spacer(1, 4))

        elements.append(Paragraph(
            "<b>Tangible Handover Deliverables:</b> (1) Public Cloudflare live prototype (<code>https://promptshield.sparsh2005bansal.workers.dev/</code>); "
            "(2) Full version-controlled GitHub repository (<code>https://github.com/itzzSPcoder/PromptShield</code>); "
            "(3) Automated CLI benchmark suite (<code>run_red_team_benchmark.py</code>) with 30-case telemetry dataset (<code>benchmark_results.json</code>); "
            "(4) Complete academic IEEE Technical Research Paper and Milestone 2 Master Report.",
            styles['Body']
        ))

        # Footer
        elements.append(Spacer(1, 10))
        elements.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor('#CBD5E0'), spaceBefore=2, spaceAfter=4))
        elements.append(Paragraph("Team NullPointers (PE-B25-33) &bull; Bennett University &bull; Milestone 2 Submission &bull; Academic Year 2026", styles['Footer']))

        doc.build(elements)
        print(f"[OK] Generated: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    build_pdf()
