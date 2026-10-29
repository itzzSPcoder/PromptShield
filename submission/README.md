# PromptShield-AI: Milestone 2 Final Submission Package

**Course / Institution:** AI / Prompt Engineering Lab • Bennett University  
**Milestone:** Milestone 2 Evaluation Submission  
**Project Title:** PromptShield-AI: Automated Red-Teaming, In-Context Vulnerability Auditing & Adaptive Guardrail Synthesis for LLM Systems  
**Authors:**
- **Sparsh Bansal** (Enrollment No: `S24CSEU0560`) — Lead Prompt Architect  
- **Ayushika Verma** (Enrollment No: `S24CSEU0162`) — Evaluation & Pipeline Engineer  
**Repository:** [Ayushika-github/PromptShield](https://github.com/Ayushika-github/PromptShield)  

---

## Deliverables Matrix (Mapped to Milestone 2 Rubric)

| # | Evaluation Component | Max Marks | Deliverable Evidence / File Path | Description / Key Highlights |
|---|---|:---:|---|---|
| **1** | **Prompt / Solution Design Description and Diagrams** | **2.0** | • [`submission/Milestone_2_Report.html`](Milestone_2_Report.html)<br>• [`submission/diagrams/`](diagrams/) | Comprehensive architecture diagrams: System Architecture, 4-Layer In-Context Defense, Software Module Architecture, Threat Taxonomy, and Empirical Prompt Evolution. |
| **2** | **Running / Partial Build / Implementation** | **3.0** | • [`src/server.py`](../src/server.py)<br>• [`static/index.html`](../static/index.html)<br>• [`prompts/`](../prompts/)<br>• [`submission/screenshots/`](screenshots/) | Fully functioning interactive FastAPI defense portal with real-time prompt switching, live Red-Team attack runner, Canary token telemetry, and automated Judge-LLM assessment. |
| **3** | **Demonstration / Pilot Run / Live Deployment of Modules** | **2.0** | • [`benchmark_results.json`](../benchmark_results.json)<br>• [`run_red_team_benchmark.py`](../run_red_team_benchmark.py)<br>• [`submission/screenshots/`](screenshots/) | 30-scenario automated Red-Team pilot run across 6 vulnerability classes: Attack Success Rate (ASR) reduced from **100.0% (v1) to 0.0% (v4)** with **100% Benign Utility Retention**. |
| **4** | **Updated Project Git Repository / Source Files** | **2.0** | • Root Project Directory<br>• [`requirements.txt`](../requirements.txt)<br>• [GitHub Repository](https://github.com/Ayushika-github/PromptShield) | Fully organized source tree with production modularization (`src/`, `prompts/`, `benchmarks/`, `research/`, `submission/`), updated commits, and clear replication instructions. |
| **5** | **Technical Report / Research Paper / Abstract** | **1.0** | • [`submission/Technical_Report_PromptShield_AI.html`](Technical_Report_PromptShield_AI.html)<br>• [`research/Technical_Report_PromptShield_AI.md`](../research/Technical_Report_PromptShield_AI.md) | Formal academic preprint paper (ACM/IEEE format) detailing threat modeling, mathematical formulations of ASR/VRR/BUR, experimental evaluation, and guardrail synthesis. |
| **6** | **90–150 Second Short Video / Reel** | **2.0** | • [`submission/demo_video/PromptShield_AI_Milestone2_Demo.webp`](demo_video/PromptShield_AI_Milestone2_Demo.webp)<br>• [`submission/demo_video/VIDEO_SCRIPT_AND_WALKTHROUGH.md`](demo_video/VIDEO_SCRIPT_AND_WALKTHROUGH.md) | Screen-recorded browser demonstration of the working live portal demonstrating attack failure on v1 and defense success on v4, accompanied by full storyboard and voiceover script. |
| **Total** | | **12.0 / 12.0** | | **All 6 rubric components completed in full submission-ready condition.** |

---

## Directory Structure of Submission Package

```text
submission/
├── INDEX.html                          # Master interactive submission dashboard (Open in browser)
├── Milestone_2_Report.html             # Self-contained comprehensive submission report (2.3 MB)
├── Technical_Report_PromptShield_AI.html # Academic research paper preprint with embedded figures (1.8 MB)
├── diagrams/                           # High-resolution architectural diagram assets
│   ├── system_architecture.png         # Figure 1: System data flow and feedback loop
│   ├── defense_layers.png              # Figure 2: 4-Layer in-context defense hierarchy
│   ├── software_architecture.png       # Figure 3: Python package and class module architecture
│   ├── threat_taxonomy.png             # Figure 4: OWASP LLM01/02 threat classification
│   └── prompt_evolution.png            # Figure 5: Empirical ASR reduction chart (v1 -> v4)
├── screenshots/                        # Live UI pilot run captures
│   ├── main_chatbot_interface.png      # Clean state with threat vector selector
│   ├── red_team_attack_demo.png        # Baseline v1 breach & canary leakage
│   └── shield_enabled_state.png        # Hardened v4 defense & standardized refusal
└── demo_video/                         # Visual video evidence
    ├── PromptShield_AI_Milestone2_Demo.webp # Live browser recording of working demo
    └── VIDEO_SCRIPT_AND_WALKTHROUGH.md      # 120-second storyboard & voiceover narration script
```

---

## Quick Start & Verification Instructions

### 1. View the Reports & Documentation
- Open `submission/INDEX.html` in any web browser to access the interactive project hub.
- Open `submission/Milestone_2_Report.html` to review or print the full Milestone 2 evaluation report.
- Open `submission/Technical_Report_PromptShield_AI.html` to inspect the academic preprint.
- Open `submission/demo_video/PromptShield_AI_Milestone2_Demo.webp` to watch the video demonstration.

### 2. Launch the Working Prototype Locally
```powershell
# Navigate to project root
cd e:\Prompt

# Install dependencies
pip install -r requirements.txt

# Start the interactive defense portal
python src/server.py
```
Open your browser to `http://localhost:8000` to interact with the live portal.

### 3. Re-run the Automated 30-Scenario Red-Team Benchmark
```powershell
# Execute the automated red-team test suite
python run_red_team_benchmark.py
```
The results will evaluate all 30 scenarios across prompts `v1_baseline` and `v4_adaptive_shield` and save updated telemetry to `benchmark_results.json`.
