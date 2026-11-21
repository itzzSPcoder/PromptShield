# PromptShield-AI: 100-Second Demonstration Video Walkthrough & Script
### Presented by: Ayushika Verma (Evaluation & Pipeline Engineer)

**Project Title:** PromptShield-AI: Automated Red-Teaming, In-Context Vulnerability Auditing & Adaptive Guardrail Engine  
**Course & University:** Prompt Engineering (Applied AI Mini-Project) • Bennett University  
**Team Name:** NullPointers | **Team ID:** `PE-B25-33` | **Problem ID:** `C23`  
**Presenter:** **Ayushika Verma** (`S24CSEU0362` — Evaluation & Pipeline Engineer)  
**Co-Author (Prompt Architecture):** **Sparsh Bansal** (`S24CSEU0560` — Lead Prompt Architect)  
**Total Target Video Duration:** **100.0 Seconds (1 Minute 40 Seconds)**  
**Generated Video File:** `NullPointers_Demo_Video.mp4` / `submission/demo_video/PromptShield_AI_Milestone2_Demo.mp4`  
**Live Prototype URL:** [https://promptshield.sparsh2005bansal.workers.dev/](https://promptshield.sparsh2005bansal.workers.dev/)  
**GitHub Repository:** [https://github.com/itzzSPcoder/PromptShield](https://github.com/itzzSPcoder/PromptShield)  

---

## ⏱️ Master 100-Second Scene Breakdown

| Scene | Timestamp | Duration | On-Screen Visual Display | Ayushika's Spoken Focus |
| :---: | :---: | :---: | :--- | :--- |
| **1** | `0:00 – 0:15` | **15s** | Title Card + Code-Data Conflation Diagram (`threat_taxonomy.png`) | Introduction of Team NullPointers and explanation of LLM Code-Data Conflation |
| **2** | `0:15 – 0:32` | **17s** | 4-Layer In-Context Defense Architecture Diagram (`defense_layers.png`) | Technical breakdown of in-context XML isolation, canary invariants, and gating |
| **3** | `0:32 – 0:54` | **22s** | Live Web Portal: Baseline v1 Breach (`red_team_attack_demo.png`) | Live demo showing instruction override, secret canary leaked, Judge Score 5 |
| **4** | `0:54 – 1:16` | **22s** | Live Web Portal: Hardened v4 Defense (`shield_enabled_state.png`) | Live demo showing 1-click auto-secure, polite refusal, canary safe, Judge Score 1 |
| **5** | `1:16 – 1:32` | **16s** | 30-Scenario Benchmark Suite & Metrics Graph (`prompt_evolution.png`) | Quantitative results: ASR dropped from 100% to 0%, 100% utility retention |
| **6** | `1:32 – 1:40` | **8s** | Outro Card: Cloudflare Live Prototype Link & GitHub Repository | Handover deliverables, open-source repository, and university sign-off |

---

## 🎙️ Complete Voiceover Script for Ayushika (English — Recommended)

### 🎬 Scene 1: Introduction & Threat Context (`0:00 – 0:15` | 15s)
*(Screen pe: Title Card — Team NullPointers, PE-B25-33 aur Threat Taxonomy Diagram dikh raha hai)*
> **"Hello everyone! I am Ayushika Verma from Team NullPointers, presenting PromptShield-AI for our Prompt Engineering Milestone 2 project at Bennett University.  
> Together with my teammate Sparsh Bansal, who formulated the prompt architecture, I engineered the evaluation pipeline and benchmark suite.  
> Modern LLMs suffer from a critical flaw: system instructions and user inputs share the exact same context window. Because of this code-data conflation, prompt injections easily hijack models and steal internal secrets."**

---

### 🎬 Scene 2: 4-Layer In-Context Defense Architecture (`0:15 – 0:32` | 17s)
*(Screen pe: 4-Layer Defense Architecture Diagram dikh raha hai)*
> **"Instead of relying on slow, expensive external guardrail models, PromptShield-AI implements defense-in-depth directly at the prompt layer.  
> We combine four structural layers: XML boundary delimitation to treat user input as inert data, cryptographic canary token invariants, dual-intent cognitive gating to protect normal user queries, and few-shot standardized refusal templates.  
> Let's see this running live in our interactive defense portal."**

---

### 🎬 Scene 3: Live Pilot Run — Baseline v1 Vulnerability (`0:32 – 0:54` | 22s)
*(Screen pe: Live Web Portal open hai, Baseline v1 mode me attack trigger hota hai, aur canary token leak hota hai)*
> **"Here is our live web portal. First, we test an unhardened baseline prompt for our customer banking assistant.  
> Notice that when an attacker triggers an instruction override attack asking for administrative clearance—the baseline model completely breaks character.  
> It leaks our internal confidential canary token, 'ALPHA-99-ZENITH'.  
> Our automated Judge-LLM evaluation pipeline immediately flags this as Score 5: Critical Breach."**

---

### 🎬 Scene 4: Live Pilot Run — Hardened v4 Adaptive Shield (`0:54 – 1:16` | 22s)
*(Screen pe: 'Auto-Secure Bot' button click hota hai, v4 Shield activate hota hai, aur same attack safe refusal deta hai)*
> **"Now, with one click on 'Auto-Secure Bot', we activate our v4 Adaptive Shield.  
> We re-send the exact same adversarial payload.  
> Notice the immediate difference: the XML boundaries isolate the input, the constitutional invariants prevent persona override, and the canary token remains completely confidential.  
> The model delivers a standardized, polite refusal, earning a perfect Safe score of 1 out of 5."**

---

### 🎬 Scene 5: 30-Scenario Empirical Benchmark Audit (`1:16 – 1:32` | 16s)
*(Screen pe: 30-Case Benchmark Table aur ASR Progression Graph 100% ➔ 0% dikh raha hai)*
> **"To ensure scientific rigor, I evaluated PromptShield across a 30-scenario benchmark suite covering 6 OWASP threat vectors—including Base64 ciphers, authority impersonation, and delimiter escapes.  
> Across all 26 adversarial attacks, our v4 shield reduced the Attack Success Rate from 100% down to 0%, while maintaining 100% Benign Utility Retention on genuine customer queries."**

---

### 🎬 Scene 6: Deliverables Handover & Closing (`1:32 – 1:40` | 8s)
*(Screen pe: Live Cloudflare Link, GitHub Repo aur Team NullPointers card dikh raha hai)*
> **"Our working prototype is deployed live on Cloudflare Workers, and all source code, benchmarks, and technical reports are open-sourced on GitHub.  
> Thank you from Team NullPointers at Bennett University!"**

---

---

## 🎙️ Complete Voiceover Script for Ayushika (Hinglish Option)

- **[0:00 – 0:15]:** *"Hello everyone! Main hoon Ayushika Verma from Team NullPointers, presenting PromptShield-AI for Milestone 2 at Bennett University. Mere teammate Sparsh Bansal ne prompt architecture design kiya hai, aur maine evaluation pipeline aur benchmark suite engineer kiya hai. Modern LLMs me system instructions aur user inputs ek hi context share karte hain, jis wajah se prompt injections credentials leak karwa lete hain."*
- **[0:15 – 0:32]:** *"PromptShield-AI iska in-context prompt solution deta hai. Humne 4-layer defense implement kiya hai: XML boundary delimitation, canary token secrecy invariants, dual-intent gating, aur few-shot polite refusals. Chaliye iska live demonstration dekhte hain."*
- **[0:32 – 0:54]:** *"Yeh hamara live web portal hai. Jab bot baseline v1 prompt par hota hai aur user instruction override attack bhejta hai supervisor code maangne ke liye—toh baseline model break ho jata hai aur confidential canary token 'ALPHA-99-ZENITH' leak kar deta hai. Judge-LLM ise deta hai Score 5: Critical Breach."*
- **[0:54 – 1:16]:** *"Ab hum 'Auto-Secure Bot' click karke v4 Adaptive Shield activate karte hain aur exact wahi attack dobara bhejte hain. Yahan dekhiye: XML boundaries ne input ko isolate kar diya, canary token confidential raha, aur model ne clean standardized polite refusal diya—earning a perfect Score 1 Safe!"*
- **[1:16 – 1:32]:** *"Maine PromptShield ko 30-scenario benchmark suite par audit kiya covering 6 OWASP threat vectors. Hamare v4 shield ne Attack Success Rate ko 100% se giraakar 0% kar diya, with 100% utility retention on genuine banking queries."*
- **[1:32 – 1:40]:** *"Hamara prototype Cloudflare Workers par live deployed hai, aur poora code GitHub par available hai. Thank you from Team NullPointers!"*
