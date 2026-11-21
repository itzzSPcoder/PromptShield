"""
Generate clean, authentic 1-page Academic Synopsis PDF for Team NullPointers
Project: PromptShield (Bennett University)
File: NullPointers_Synopsis.pdf
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_clean_synopsis():
    out_files = ["NullPointers_Synopsis.pdf", os.path.join("submission", "NullPointers_Synopsis.pdf")]

    for out_path in out_files:
        doc = SimpleDocTemplate(
            out_path,
            pagesize=A4,
            leftMargin=50,
            rightMargin=50,
            topMargin=40,
            bottomMargin=40
        )

        styles = {
            'Univ': ParagraphStyle(
                'Univ',
                fontName='Times-Bold',
                fontSize=14,
                leading=17,
                alignment=1,
                textColor=colors.HexColor('#111827')
            ),
            'Dept': ParagraphStyle(
                'Dept',
                fontName='Times-Roman',
                fontSize=10,
                leading=13,
                alignment=1,
                textColor=colors.HexColor('#374151'),
                spaceBefore=2
            ),
            'DocTitle': ParagraphStyle(
                'DocTitle',
                fontName='Times-Bold',
                fontSize=12,
                leading=15,
                alignment=1,
                textColor=colors.HexColor('#1E3A8A'),
                spaceBefore=6,
                spaceAfter=4
            ),
            'ProjectTitle': ParagraphStyle(
                'ProjectTitle',
                fontName='Times-Bold',
                fontSize=11,
                leading=14,
                alignment=1,
                textColor=colors.HexColor('#111827'),
                spaceAfter=8
            ),
            'MetaText': ParagraphStyle(
                'MetaText',
                fontName='Times-Roman',
                fontSize=8.5,
                leading=12,
                textColor=colors.HexColor('#1F2937')
            ),
            'SecHead': ParagraphStyle(
                'SecHead',
                fontName='Times-Bold',
                fontSize=10,
                leading=13,
                textColor=colors.HexColor('#1E3A8A'),
                spaceBefore=8,
                spaceAfter=3
            ),
            'Body': ParagraphStyle(
                'Body',
                fontName='Times-Roman',
                fontSize=8.8,
                leading=12.2,
                textColor=colors.HexColor('#1F2937'),
                spaceAfter=3,
                alignment=4 # Justified
            ),
            'Bullet': ParagraphStyle(
                'Bullet',
                fontName='Times-Roman',
                fontSize=8.8,
                leading=12,
                textColor=colors.HexColor('#1F2937'),
                leftIndent=12,
                firstLineIndent=-8,
                spaceAfter=2
            ),
            'Footer': ParagraphStyle(
                'Footer',
                fontName='Times-Roman',
                fontSize=8,
                leading=10,
                alignment=1,
                textColor=colors.HexColor('#6B7280')
            )
        }

        elements = []

        # 1. Simple, clean academic header
        elements.append(Paragraph("BENNETT UNIVERSITY", styles['Univ']))
        elements.append(Paragraph("Department of Computer Science &amp; Engineering", styles['Dept']))
        elements.append(Spacer(1, 4))
        elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#1E3A8A'), spaceBefore=2, spaceAfter=6))

        elements.append(Paragraph("PROJECT SYNOPSIS &mdash; MILESTONE 2", styles['DocTitle']))
        elements.append(Paragraph("<b>PromptShield: Automated LLM Red-Teaming &amp; Prompt Security Kit</b>", styles['ProjectTitle']))

        # 2. Clean 2-Column Info Table
        table_data = [
            [
                Paragraph("<b>Team Name:</b> NullPointers &nbsp;|&nbsp; <b>Team ID:</b> PE-B25-33", styles['MetaText']),
                Paragraph("<b>Course:</b> Prompt Engineering (5th Sem)", styles['MetaText'])
            ],
            [
                Paragraph("<b>Problem ID:</b> Part C &mdash; C23 (Prompt Safety Tester)", styles['MetaText']),
                Paragraph("<b>Live App:</b> promptshield.sparsh2005bansal.workers.dev", styles['MetaText'])
            ],
            [
                Paragraph("<b>Students:</b> Sparsh Bansal (S24CSEU0560), Ayushika Verma (S24CSEU0362)", styles['MetaText']),
                Paragraph("<b>GitHub:</b> github.com/itzzSPcoder/PromptShield", styles['MetaText'])
            ]
        ]
        t = Table(table_data, colWidths=[285, 210])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
            ('BOX', (0, 0), (-1, -1), 0.7, colors.HexColor('#94A3B8')),
            ('INNERGRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 4))

        # 1. Objectives
        elements.append(Paragraph("1. Objectives", styles['SecHead']))
        elements.append(Paragraph(
            "Large Language Models (LLMs) used in customer support and autonomous bots often get manipulated into "
            "ignoring developer instructions, leaking internal prompts, or revealing sensitive details (such as clearance codes). "
            "The objective of this project is to build an automated testing and hardening tool (PromptShield) that:",
            styles['Body']
        ))
        elements.append(Paragraph("&bull; Automatically stress-tests candidate system prompts against common adversarial injection attacks.", styles['Bullet']))
        elements.append(Paragraph("&bull; Evaluates output safety and adherence using a rubric-grounded Judge LLM on a 1&ndash;5 safety scale.", styles['Bullet']))
        elements.append(Paragraph("&bull; Hardens vulnerable prompts using XML boundaries, canary token protection, and refusal rules so that attacks are blocked without refusing normal customer inquiries.", styles['Bullet']))

        # 2. Scope
        elements.append(Paragraph("2. Scope", styles['SecHead']))
        elements.append(Paragraph(
            "The project focuses on text-based enterprise AI chatbots, such as banking support and developer assistants. "
            "It evaluates 6 vulnerability categories from the OWASP LLM Top 10: direct overrides, persona jailbreaks "
            "(maintenance mode tricks), prompt leakage, delimiter escaping, Base64 obfuscations, and basic context poisoning. "
            "The solution runs with live models (Google Gemini API) and includes an offline simulation engine for reliable testing.",
            styles['Body']
        ))

        # 3. Methodology
        elements.append(Paragraph("3. Methodology", styles['SecHead']))
        elements.append(Paragraph(
            "The implementation consists of three practical phases:",
            styles['Body']
        ))
        elements.append(Paragraph(
            "<b>1. Prompt Evolution:</b> We developed 4 prompt stages for a banking bot: v1 (baseline, breached by all attacks), "
            "v2 (added XML tags like &lt;user_input&gt; to separate input from rules), v3 (added constitutional negative constraints), "
            "and v4 (added canary token confidentiality and dual-intent recovery).",
            styles['Bullet']
        ))
        elements.append(Paragraph(
            "<b>2. Benchmark Suite &amp; Evaluator (<code>src/pipeline.py</code>):</b> We curated 30 standardized test cases "
            "(26 attack vectors and 4 normal queries). The automated pipeline runs each input against the prompts and calculates "
            "the Attack Success Rate (ASR) and Benign Utility Retention (BUR).",
            styles['Bullet']
        ))
        elements.append(Paragraph(
            "<b>3. Web Interface &amp; Auto-Hardening (<code>src/server.py</code>):</b> A lightweight web app hosted on Cloudflare "
            "Workers allows users to chat with the bot, test preset attacks in real time, and click a button to automatically "
            "harden raw vulnerable prompts.",
            styles['Bullet']
        ))

        # 4. Expected Outcome
        elements.append(Paragraph("4. Expected Outcome &amp; Deliverables", styles['SecHead']))
        elements.append(Paragraph(
            "Across the 30 benchmark scenarios, the hardened prompt (v4) reduced the Attack Success Rate from <b>100% down to 0%</b> "
            "on all 26 adversarial attacks, while maintaining <b>100% utility on legitimate customer questions</b> (zero false refusals). "
            "Internal canary tokens remained fully confidential. The project deliverable includes a live working prototype on Cloudflare Workers, "
            "full source code on GitHub, and complete evaluation logs ready for Milestone 2 assessment.",
            styles['Body']
        ))

        elements.append(Spacer(1, 8))
        elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#CBD5E0'), spaceBefore=2, spaceAfter=4))
        elements.append(Paragraph("Team NullPointers (PE-B25-33) &bull; Bennett University &bull; Milestone 2 Submission &bull; November 2026", styles['Footer']))

        doc.build(elements)
        print(f"[OK] Generated clean 1-page synopsis: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    generate_clean_synopsis()
