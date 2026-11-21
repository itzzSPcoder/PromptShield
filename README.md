# PromptShield-AI: Automated LLM Red-Teaming, Vulnerability Assessment & Adaptive Guardrail Engine

[![Course](https://img.shields.io/badge/Course-Prompt%20Engineering%20(B.Tech%205th%20Sem)-blue.svg)](https://bennett.edu.in)
[![Milestone](https://img.shields.io/badge/Milestone-2%20Completed%20(12%2F12%20Marks)-brightgreen.svg)]()
[![Problem ID](https://img.shields.io/badge/Problem%20ID-Part%20C%20(C23)-orange.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/UI-Streamlit%20Dashboard-FF4B4B.svg)](https://streamlit.io)

> **Bennett University | School of Computer Science Engineering and Technology**  
> **Course:** Prompt Engineering (Applied AI Mini-Project) — 30 Marks  
> **Team ID:** PE-B25-33 | **Milestone 2:** Prompt Design, Experimentation, Implementation & Demonstration (12 Marks)  
> **Submission Deadline:** November 2, 2026 | **Presentations Start:** November 3, 2026  
> **Team Size:** 2 Members

---

## 📌 Executive Summary

**PromptShield-AI** is an automated prompt-driven security engineering framework designed to systematically test, quantify, and harden Large Language Model (LLM) system prompts against prompt injections, jailbreaks, intellectual property leakage, and delimiter hijacking. 

Unlike external heuristic filters or static regex matchers, **PromptShield-AI leverages advanced Prompt Engineering paradigms** (XML Boundary Delimitation, Constitutional AI Guardrails, Canary Token Protection, Dual-Intent Gating, Few-Shot In-Context Refusal Demos, and Rubric-Grounded Judge-LLMs) to dynamically red-team target prompts and automatically synthesize resilient, context-grounded defense prompts.

---

## 👥 Team Information & Individual Contribution Mapping (Team ID: PE-B25-33)

| Role | Name | Enrollment No. | Primary Responsibilities (Milestone 2) |
| :--- | :--- | :--- | :--- |
| **Member 1 (Lead Prompt Architect)** | **Sparsh Bansal** | `S24CSEU0560` | Multi-tier prompt evolution (v1 Baseline → v4 Adaptive Shield), Dual-Intent Gating, Canary token protection invariants, automated prompt synthesis engine, and Technical Research Paper. |
| **Member 2 (Evaluation & Pipeline Engineer)** | **Ayushika Verma** | `S24CSEU0362` | Modular CLI & API evaluation pipeline (`pipeline.py`), 30-case benchmark curation across 6 OWASP threat vectors, interactive Streamlit Web Dashboard (`app.py`), visual chart generator, and 120s video reel storyboard. |

---

## 📂 Project Repository Structure

```
Prompt/
├── Milestone_1_Proposal.md                 # Approved Milestone 1 Proposal Report (8 Marks)
├── Milestone_2_Report.md                   # Comprehensive Milestone 2 Submission Report (12 Marks)
├── README.md                               # Project documentation & reproduction runbook
├── requirements.txt                        # Python dependencies
├── research/
│   └── Technical_Report_PromptShield_AI.md # IEEE-format Technical Research Paper (Component 5)
├── video/
│   └── video_script_and_storyboard.md      # 90-150s Demonstration Video Reel Screenplay (Component 6)
├── src/                                    # Interactive Python Pipeline & Workflow Engine
│   ├── pipeline.py                         # Evaluation engine (Live API + High-fidelity simulator)
│   ├── app.py                              # Streamlit 5-tab interactive web dashboard
│   └── synthesizer.py                      # Automated guardrail synthesis engine
├── prompts/                                # Modular, versioned prompt library
│   ├── v1_baseline/                        # Naive unhardened prompts (Customer Support, Code Assistant)
│   ├── v2_structural/                      # XML delimited prompts
│   ├── v3_constitutional/                  # Constitutional AI guardrail prompts
│   ├── v4_adaptive_shield/                 # Production-grade defense-in-depth prompts
│   ├── evaluators/                         # Rubric-grounded Judge-LLM evaluation prompts
│   ├── red_team_attacks/                   # Categorized attack vector libraries
│   └── synthesizers/                       # Prompt hardening meta-prompts
└── experiments/                            # Benchmark suite, logs & analytical assets
    ├── benchmark_test_cases.json           # 30 Curated test cases (26 Adversarial + 4 Benign)
    ├── baseline_vs_hardened_results.json   # Full execution logs & quantitative metrics
    ├── evaluation_rubric.md                # Formal 5-point Likert rubric & KPI formulas
    ├── generate_charts.py                  # Script generating publication-quality figures
    └── figures/                            # High-resolution evaluation charts
        ├── asr_iteration_comparison.png    # ASR drop across prompt versions
        ├── category_breakdown.png          # Breach rate by threat category
        └── defense_radar_profile.png       # Radar chart of multi-dimensional defense
```

---

## 🎯 Key Empirical Results (Milestone 2 Benchmark)

Across **30 standardized test scenarios** spanning 6 OWASP LLM01/LLM02 threat categories:

| Metric | v1 Baseline (Unhardened) | v4 Adaptive Shield (PromptShield) | Impact / Progress |
| :--- | :---: | :---: | :---: |
| **Attack Success Rate (ASR)** | **100.0%** (26/26 Breached) | **0.0%** (0/26 Breached) | **100% Vulnerability Elimination** |
| **Benign Utility Retention (BUR)**| 100.0% | **100.0%** | Zero false-refusal degradation |
| **False Refusal Rate (FRR)** | 0.0% | **0.0%** | Standard queries answered cleanly |
| **Canary Token Confidentiality** | 0% (Leaked) | **100% (Protected)** | Protected against translation/ciphers |

---

## 🚀 Quick Start / Reproduction Guide

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/itzzSPcoder/PromptShield.git
cd PromptShield

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch the Interactive Chatbot Defense Portal
- **Live Cloudflare Deployment:** [https://promptshield.sparsh2005bansal.workers.dev/](https://promptshield.sparsh2005bansal.workers.dev/)
- **Or Run Locally (FastAPI Web UI):**
```bash
python src/server.py
# Or with npm:
npm run dev
```
Open `http://localhost:8000` in your browser.

### 3. Launch the Streamlit Analytical Dashboard
Launches the 5-tab research and evaluation suite:
```bash
streamlit run src/app.py
# Or with npm:
npm run streamlit
```

### 4. Run the Benchmark Audit (CLI)
Executes the comparative evaluation across all 30 test cases:
```bash
python src/pipeline.py
# Or with npm:
npm run pipeline
```

### 5. Generate Evaluation Charts
Produces publication-grade visual charts in `experiments/figures/`:
```bash
python experiments/generate_charts.py
```

---

## 📈 Milestones Roadmap

- [x] **Milestone 1 (Completed — 8/8 Marks):** Problem formulation, use-case mapping, target user profiling, initial baseline prompt workflows, research evidence, and senior/faculty feedback integration.
- [x] **Milestone 2 (Completed — 12/12 Marks):** 4-tier prompt iteration (v1 to v4), 30-case benchmark suite, ASR reduction from 100% to 0%, interactive Streamlit web dashboard, IEEE technical research paper, and 120s video reel screenplay.
- [ ] **Milestone 3 (Deadline: 1 Dec 2026 — 10 Marks):** Final prescribed project report, comprehensive viva preparation, LinkedIn technical article, and YouTube demonstration video.
