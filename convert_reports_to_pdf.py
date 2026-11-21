"""
Convert HTML submission documents to high-resolution, print-ready PDFs using Chrome headless.
Generates:
- NullPointers_Milestone_2_Report.pdf
- Milestone_2_Report.pdf
- Technical_Report_PromptShield_AI.pdf
"""

import os
import subprocess
import shutil

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ROOT = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(ROOT, "submission")

def html_to_pdf(html_path, output_pdf_path):
    file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf_path}",
        file_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(output_pdf_path):
        size_kb = os.path.getsize(output_pdf_path) / 1024
        print(f"[OK] Generated: {output_pdf_path} ({size_kb:.1f} KB)")
        return True
    else:
        print(f"[FAIL] Could not generate {output_pdf_path}. Stderr: {res.stderr}")
        return False

def main():
    m2_html = os.path.join(SUB, "Milestone_2_Report.html")
    tech_html = os.path.join(SUB, "Technical_Report_PromptShield_AI.html")

    # 1. Milestone 2 Comprehensive Report PDF
    m2_root = os.path.join(ROOT, "NullPointers_Milestone_2_Report.pdf")
    m2_sub = os.path.join(SUB, "NullPointers_Milestone_2_Report.pdf")
    m2_std = os.path.join(ROOT, "Milestone_2_Report.pdf")

    html_to_pdf(m2_html, m2_root)
    shutil.copyfile(m2_root, m2_sub)
    shutil.copyfile(m2_root, m2_std)

    # 2. Technical Research Paper PDF
    tech_root = os.path.join(ROOT, "Technical_Report_PromptShield_AI.pdf")
    tech_sub = os.path.join(SUB, "Technical_Report_PromptShield_AI.pdf")
    html_to_pdf(tech_html, tech_root)
    shutil.copyfile(tech_root, tech_sub)

    # Clean up test.pdf
    test_pdf = os.path.join(ROOT, "test.pdf")
    if os.path.exists(test_pdf):
        os.remove(test_pdf)

if __name__ == "__main__":
    main()
