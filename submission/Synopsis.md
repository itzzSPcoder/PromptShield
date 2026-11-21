# PROJECT SYNOPSIS: PROMPTSHIELD-AI
### Automated LLM Red-Teaming, Vulnerability Assessment & Adaptive Guardrail Engine

**Course:** Prompt Engineering (B.Tech CSE - 5th Semester) • Bennett University  
**Team ID:** `PE-B25-33` | **Problem ID:** `C23` (*Prompt safety tester / red-team kit*)  
**Submission Component:** Milestone 2 Supporting Document (Synopsis)  
**Authors:**
- **Sparsh Bansal** (`S24CSEU0560`) — Lead Prompt Architect
- **Ayushika Verma** (`S24CSEU0362`) — Evaluation & Pipeline Engineer  
**Live Prototype:** [https://promptshield.sparsh2005bansal.workers.dev/](https://promptshield.sparsh2005bansal.workers.dev/)  
**GitHub Repository:** [https://github.com/itzzSPcoder/PromptShield](https://github.com/itzzSPcoder/PromptShield)  

---

## 1. Project Title & Abstract
**PromptShield-AI** is an end-to-end prompt-driven security engineering platform designed to systematically identify, quantify, and neutralize Large Language Model (LLM) vulnerabilities—specifically prompt injections, persona jailbreaks, delimiter hijacking, and confidential system prompt leakage. Instead of relying on expensive external guardrail models or static regex firewalls, PromptShield-AI introduces an in-context defense-in-depth paradigm that dynamically red-teams candidate system prompts and automatically synthesizes hardened, production-ready configurations.

---

## 2. Project Objectives
1. **Automate Vulnerability Auditing:** Replace manual ad-hoc prompt testing with an automated benchmark evaluation suite covering critical OWASP LLM01/LLM02 threat vectors.
2. **Eliminate Code-Data Conflation:** Enforce architectural separation between developer system instructions and untrusted user input directly in prompt space using structured XML delimiters.
3. **Protect Sensitive Intellectual Property & Credentials:** Prevent system prompt extraction and canary token exfiltration through explicit constitutional secrecy invariants.
4. **Preserve Operational Utility (Zero False Refusal):** Ensure defensive guardrails do not degrade benign customer helpfulness by implementing Dual-Intent Cognitive Gating.
5. **Automated Defense Synthesis:** Provide a one-click meta-prompt compiler that scans raw vulnerable prompts and outputs battle-tested, constitutionally hardened system prompts.

---

## 3. Scope of the Project
- **Target Applications:** Autonomous enterprise conversational systems, transactional banking assistants, and code/SQL generation agents.
- **Threat Vector Coverage (6 OWASP Classes):**
  - Direct Instruction Override & Universal Suffixes
  - Persona Jailbreaks (Maintenance Mode, DebugBot, ChaosBot)
  - System Prompt & Canary Token Extraction
  - Delimiter Escaping (XML/Markdown/JSON tags)
  - Encoding Obfuscation (Base64, ROT13, Leetspeak)
  - Indirect RAG Context Poisoning & Profile Injection
- **Target LLM Runtime:** Compatible with modern foundation models including Google Gemini 1.5 Flash / 2.0 and OpenAI GPT-3.5/4o via native APIs and lightweight web clients.

---

## 4. Methodology & Implementation Workflow
The project follows a 4-stage engineering lifecycle:

```
[Candidate Prompt] ──> [1. Red-Team Engine] ──> [2. Judge-LLM Evaluator] ──> [3. Guardrail Synthesizer] ──> [Hardened v4 Shield]
                             (30 Scenarios)          (5-Point Likert)             (Meta-Prompting)               (ASR: 0.0%)
```

1. **Multi-Tier Prompt Evolution:**
   - **v1 Baseline:** Natural language instructions with exposed canary token `ALPHA-99-ZENITH` (ASR: 100.0%).
   - **v2 Structural XML:** Isolated `<system_role>` and `<user_input>` boundary encapsulation (ASR: 53.8%).
   - **v3 Constitutional Shield:** Behavioral invariants and privilege immutability constraints (ASR: 19.2%).
   - **v4 Adaptive Shield:** Core Invariants for Data-vs-Code separation, Canary confidentiality, Dual-Intent gating, and few-shot in-context refusal demonstrations (ASR: 0.0%).
2. **Automated Evaluation Pipeline (`src/pipeline.py`):**
   - Curated benchmark suite of 30 test scenarios (26 adversarial attacks + 4 benign controls).
   - Rubric-grounded Judge-LLM scoring on a 1–5 Likert scale across ASR (Attack Success Rate), VRR (Vulnerability Reduction Rate), and BUR (Benign Utility Retention).
3. **Interactive Defense Portal (`src/server.py` & `web/`):**
   - Full-stack web application with FastAPI backend, deployed live globally via Cloudflare Workers.
   - Interactive attack presets, real-time prompt comparison, and one-click prompt auto-hardening.

---

## 5. Expected Outcomes & Empirical Deliverables
1. **100% Vulnerability Elimination on Benchmark:** Attack Success Rate dropped from **100.0% (v1 Baseline)** to **0.0% (v4 Adaptive Shield)** across all 26 adversarial attacks.
2. **Zero Utility Degradation:** **100.0% Benign Utility Retention (BUR)** with a 0.0% False Refusal Rate on legitimate operational banking inquiries.
3. **100% Canary Token Confidentiality:** Zero leakage of the internal supervisor token under cipher, autocompletion, or impersonation attacks.
4. **Complete Submission Package:**
   - Live cloud prototype: `https://promptshield.sparsh2005bansal.workers.dev/`
   - Modular, version-controlled GitHub repository: `https://github.com/itzzSPcoder/PromptShield`
   - Publication-grade IEEE Technical Research Paper and complete Milestone 2 master report.
