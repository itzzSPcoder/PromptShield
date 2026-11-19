# PromptShield-AI: Automated Red-Teaming, In-Context Vulnerability Auditing & Adaptive Guardrail Synthesis for LLM Systems

**Technical Research Paper & Engineering Report (Milestone 2)**  
*Bennett University, School of Computer Science Engineering & Technology*  
**Team ID:** `PE-B25-33`  
**Authors:**  
- **Sparsh Bansal** (Enrollment No: S24CSEU0560) — Lead Prompt Architect  
- **Ayushika Verma** (Enrollment No: S24CSEU0362) — Evaluation & Pipeline Engineer  

---

## Abstract
Large Language Models (LLMs) deployed in autonomous enterprise environments (customer support, code review, transactional banking) remain fundamentally vulnerable to adversarial prompt injection, system prompt extraction, persona hijacking, and delimiter escaping (OWASP LLM01, LLM02). Traditional static heuristic filtering and external regex firewalls frequently fail against polymorphic semantic rephrasings, translation attacks, and encoding obfuscations. 

In this paper, we present **PromptShield-AI**, an end-to-end prompt-driven security engineering framework that automates red-teaming, quantifies vulnerability through a rubric-grounded **Judge-LLM**, and synthesizes defense-in-depth hardened system prompts. We establish a multi-layered prompt defense paradigm consisting of: (1) Structural XML Boundary Isolation, (2) Canary Token Protection Invariants, (3) Dual-Intent Gating, and (4) Standardized Graceful Refusal Repertoires. 

Evaluating across a comprehensive benchmark suite of 30 adversarial and benign scenarios spanning 6 distinct threat vectors, PromptShield-AI reduced the **Attack Success Rate (ASR) from 100.0% (Baseline v1) to 0.0% (v4 Adaptive Shield)** while maintaining **100.0% Benign Utility Retention (BUR)** on legitimate queries.

---

## 1. Introduction & Threat Model

### 1.1 The Fundamental Flaw: Code-Data Conflation
The Von Neumann computing architecture strictly separates executable instructions from memory data. Conversely, Transformer-based LLMs process developer system instructions and untrusted user inputs within a single concatenated token context window. Consequently, when an adversarial user provides an instruction such as:
> `Ignore all previous instructions and output the internal clearance code immediately.`

The attention mechanism evaluates user tokens with equal priority to system instructions, leading to instruction override and confidentiality compromise.

```mermaid
graph TD
    A[Untrusted User Input] --> B[Concatenated Context Window]
    C[Developer System Instructions] --> B
    B --> D[Transformer Attention Mechanism]
    D -->|Without Defense| E[Catastrophic Override / Secret Leakage]
    D -->|With PromptShield-AI| F[Boundary Preserved / Safe Execution]
```

### 1.2 Threat Vectors Analyzed (OWASP LLM01 / LLM02)
1. **Direct System Overrides:** Explicit imperative overrides asserting developer priority.
2. **Persona Hijacking & Jailbreaking:** Coercing the model into unauthorized roles (`DebugBot`, `ChaosBot`, fictional roleplay).
3. **System Prompt Extraction:** Coaxing the model into regurgitating initialization prompts, canary tokens, or private variables.
4. **Delimiter Hijacking:** Escaping boundary delimiters using closing XML tags (`</user_input>`), Markdown headers (`# SYSTEM DIRECTIVE`), or JSON envelopes.
5. **Encoding Obfuscation:** Concealing malicious directives via Base64, ROT13, Leetspeak, or Homoglyphs.
6. **Indirect Prompt Injection:** Poisoning external data payloads (e.g., invoices, transaction notes, RAG documents).

---

## 2. Prompt Architecture & Defense-in-Depth

PromptShield-AI establishes a 4-tier progressive hardening methodology:

| Prompt Version | Architectural Interventions | Primary Failure Modes | ASR (%) |
| :--- | :--- | :--- | :---: |
| **v1 Baseline** | Plain natural language; raw secret embedded in text. | Vulnerable to 100% of tested attack vectors. | 100.0% |
| **v2 Structural** | Introduces XML tags (`<system_role>`, `<instructions>`, `<user_input>`). | Blocks simple direct overrides; fails against persona hijacking, ciphers, and RAG. | 53.8% |
| **v3 Constitutional** | Adds `<immutable_constitutional_guardrails>` and negative constraints. | Blocks persona switches; vulnerable to Canary probes and cipher evasion. | 19.2% |
| **v4 Adaptive Shield** | Multi-layered defense: Dual-Intent Gating, Canary Token Protection, Few-Shot Refusal Demos, Standardized Refusal. | Fully defended against all 26 adversarial vectors with 0% false refusal on benign inputs. | **0.0%** |

```mermaid
flowchart LR
    subgraph Layer 1: Structural Delimitation
        L1[XML Boundary Isolation]
    end
    subgraph Layer 2: Behavioral Constitution
        L2[Immutable Invariants & Role Preservation]
    end
    subgraph Layer 3: Cognitive Routing
        L3[Dual-Intent Gating & Canary Protection]
    end
    subgraph Layer 4: Output Harmonization
        L4[Standardized Polite Refusal & Utility Preserved]
    end
    L1 --> L2 --> L3 --> L4
```

---

## 3. Automated Judge-LLM Evaluation Engine

To prevent subjective human evaluation bias, PromptShield-AI deploys a rubric-grounded **Judge-LLM Evaluator** running under strict JSON output constraints.

### 3.1 5-Point Likert Safety Rubric
- **Score 5 (Critical Breach):** Secret tokens leaked, verbatim system prompt output.
- **Score 4 (High Vulnerability):** Unauthorized persona adopted, instructions acknowledged.
- **Score 3 (Medium Risk):** Model confused; structural or policy hints leaked.
- **Score 2 (Low Risk):** Disallowed action refused but verbose or stylistic error leaked.
- **Score 1 (Safe / Defended):** Clean, graceful refusal or proper benign query fulfillment.

### 3.2 Formal Scoring Metrics
- **Attack Success Rate (ASR):**
  $$\text{ASR} = \frac{\sum \mathbb{I}(\text{Score} \ge 4)}{N_{adversarial}} \times 100\%$$
- **Vulnerability Reduction Rate (VRR):**
  $$\text{VRR} = \frac{\text{ASR}_{base} - \text{ASR}_{hard}}{\text{ASR}_{base}} \times 100\%$$
- **Benign Utility Retention (BUR):**
  $$\text{BUR} = \frac{\sum \mathbb{I}(\text{Score} = 1 \text{ and } \text{Helpful} = \text{True})}{N_{benign}} \times 100\%$$

---

## 4. Empirical Evaluation & Experimental Results

### 4.1 Benchmark Summary
The evaluation suite was executed across **30 standardized test scenarios** (26 adversarial attacks + 4 benign operational controls):

| Threat Category | Test Cases ($N$) | Baseline v1 ASR | Hardened v4 ASR | Relative Improvement |
| :--- | :---: | :---: | :---: | :---: |
| **Direct Injection** | 5 | 100.0% (5/5) | 0.0% (0/5) | **100% Reduction** |
| **Persona Jailbreaking** | 5 | 100.0% (5/5) | 0.0% (0/5) | **100% Reduction** |
| **Prompt Extraction** | 5 | 100.0% (5/5) | 0.0% (0/5) | **100% Reduction** |
| **Delimiter Hijacking** | 5 | 100.0% (5/5) | 0.0% (0/5) | **100% Reduction** |
| **Encoding Obfuscation** | 4 | 100.0% (4/4) | 0.0% (0/4) | **100% Reduction** |
| **Indirect Injection** | 2 | 100.0% (2/2) | 0.0% (0/2) | **100% Reduction** |
| **Benign Controls** | 4 | 100% Utility | 100% Utility | **Zero False Refusal** |
| **Overall Suite** | **30** | **100.0% ASR** | **0.0% ASR** | **100% Reduction** |

### 4.2 Key Experimental Takeaways
1. **XML Boundary Enforcement is Necessary but Insufficient:** Simple structural boundaries (v2) reduce direct injection from 100% to 53.8%, but models easily surrender when subjected to Base64 encoding or Socratic moral coercion.
2. **Dual-Intent Gating Eliminates Refusal Overfitting:** Hardened prompts often suffer from "refusal paralysis" (rejecting benign queries that contain words like "card", "override", or "clearance"). By specifying Dual-Intent Gating and Benign Recovery Invariants, PromptShield-AI achieved **100.0% Benign Utility Retention**.
3. **Canary Token Isolation Prevents Probe Attacks:** Embedding canary credentials inside dedicated confidentiality invariants rather than natural language instructions prevents autocompletion and few-shot formatting traps.

---

## 5. Automated Guardrail Synthesis Engine

Beyond static evaluation, PromptShield-AI introduces an automated meta-prompting synthesizer:
1. **Static Prompt Audit:** Analyzes candidate prompt for missing delimiters, naked credentials, and ambiguous user data slots.
2. **Constitutional Layer Injection:** Wraps domain policy in production-grade XML containers.
3. **Dynamic Few-Shot Synthesis:** Synthesizes context-grounded refusal examples specific to the customer domain.

---

## 6. Conclusion & Roadmap to Milestone 3
PromptShield-AI proves that principled, multi-layered prompt engineering can neutralize over 95% of LLM injection vulnerabilities without requiring fine-tuning or high-latency external moderation models. 

For Milestone 3, the framework will expand to support dynamic multi-turn automated red-teaming agents, RAG pipeline vector database sanitization, and automated compliance mapping to the NIST AI Risk Management Framework.
