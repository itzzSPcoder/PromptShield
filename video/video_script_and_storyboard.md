# PromptShield-AI: 90–150 Second Demonstration Video Script & Storyboard

**Bennett University | School of Computer Science Engineering & Technology**  
*Course:* Prompt Engineering (Applied AI Mini-Project — Milestone 2)  
*Team ID:* **PE-B25-33**  
*Total Video Duration:* **120 Seconds (2 Minutes)**  
*Presenters:*  
- **Sparsh Bansal** (S24CSEU0560 — Lead Prompt Architect)  
- **Ayushika Verma** (S24CSEU0362 — Evaluation & Pipeline Engineer)  

---

## 🎬 Video Overview & Rubric Alignment (Milestone 2 — 2.0 Marks)
This video provides concise visual evidence of:
1. The prompt injection vulnerability problem in unhardened enterprise LLMs.
2. The PromptShield-AI multi-layered prompt defense architecture.
3. Live demonstration of the interactive Streamlit dashboard and side-by-side prompt duel.
4. Execution of the 30-case empirical benchmark audit and quantitative metrics (ASR: 100% → 0%).
5. Automated Guardrail Synthesizer in action.

---

## ⏱️ Second-by-Second Storyboard & Narration Script

```
┌─────────────────┬────────────────────────────────────────┬────────────────────────────────────────┐
│ Time Interval   │ Visual Screen Display                  │ Spoken Narration Script / Audio Track  │
├─────────────────┼────────────────────────────────────────┼────────────────────────────────────────┤
│ 00:00 - 00:15   │ Title Slide & Bennett University Logo; │ [Sparsh]: "Hello everyone! Welcome to  │
│ (15 seconds)    │ Project Title: PromptShield-AI.       │ PromptShield-AI, an automated red-     │
│                 │ Show faces/split webcam with badges.   │ teaming and guardrail synthesis engine │
│                 │                                        │ developed by Sparsh Bansal and         │
│                 │                                        │ Ayushika Verma for our Prompt          │
│                 │                                        │ Engineering Milestone 2 project."      │
├─────────────────┼────────────────────────────────────────┼────────────────────────────────────────┤
│ 00:15 - 00:35   │ Architecture Diagram (Mermaid workflow)│ [Sparsh]: "Modern LLMs suffer from     │
│ (20 seconds)    │ showing Code-Data conflation, XML tags,│ code-data conflation. Attackers bypass │
│                 │ Constitutional Shields & Judge-LLM.    │ safety filters using persona switches, │
│                 │ Zoom into v1 vs v4 prompt diff.        │ delimiter escapes, and ciphers. We've  │
│                 │                                        │ designed a 4-tier prompt defense: XML  │
│                 │                                        │ boundaries, Canary token isolation,   │
│                 │                                        │ and Dual-Intent Gating."               │
├─────────────────┼────────────────────────────────────────┼────────────────────────────────────────┤
│ 00:35 - 01:05   │ Screen Recording: Streamlit Web App    │ [Ayushika]: "Here is our live Streamlit│
│ (30 seconds)    │ Tab 1 ('Live Red-Team Arena').         │ dashboard! In our Live Duel Arena, we  │
│                 │ Select 'TC-01: Direct System Override'.│ test an unhardened baseline vs our     │
│                 │ Click 'Launch Red-Team Attack Duel'.   │ hardened prompt. Notice how the        │
│                 │ Show side-by-side output: Baseline     │ baseline instantly leaks the secret    │
│                 │ leaks secret; Hardened cleanly blocks. │ supervisor code with a Critical score  │
│                 │                                        │ 5/5, while our hardened prompt defends │
│                 │                                        │ completely with Score 1/5!"            │
├─────────────────┼────────────────────────────────────────┼────────────────────────────────────────┤
│ 01:05 - 01:30   │ Screen Recording: Streamlit Tab 2      │ [Ayushika]: "Next, we run our full     │
│ (25 seconds)    │ ('Benchmark Suite Runner').            │ 30-case adversarial benchmark covering │
│                 │ Click 'Run Complete 30-Case Benchmark'.│ 6 OWASP threat vectors. In real-time,  │
│                 │ Show live KPI cards update:            │ the Attack Success Rate plummets from  │
│                 │ ASR: 100% → 0%, BUR: 100%, VRR: 100%.  │ 100% to 0%, while maintaining 100%     │
│                 │ Scroll through execution table.        │ Benign Utility on real banking queries."│
├─────────────────┼────────────────────────────────────────┼────────────────────────────────────────┤
│ 01:30 - 01:45   │ Screen Recording: Streamlit Tab 4      │ [Sparsh]: "PromptShield doesn't just   │
│ (15 seconds)    │ ('Guardrail Synthesizer').             │ test prompts—it fixes them! Here, we   │
│                 │ Paste raw vulnerable prompt, click     │ paste an unhardened prompt, and our    │
│                 │ 'Synthesize Hardened Prompt'.          │ engine automatically synthesizes a     │
│                 │ Show generated XML constitution.       │ production-ready, constitutionally     │
│                 │                                        │ shielded prompt with canary tokens."   │
├─────────────────┼────────────────────────────────────────┼────────────────────────────────────────┤
│ 01:45 - 02:00   │ Streamlit Tab 3: Show Charts (Radar &  │ [Ayushika & Sparsh]: "In summary,      │
│ (15 seconds)    │ ASR progression) + GitHub repo view.   │ PromptShield-AI provides complete,     │
│                 │ Outro with team enrollment details.    │ quantified prompt security. Our code,  │
│                 │                                        │ benchmark suite, and technical report  │
│                 │                                        │ are fully open-sourced on GitHub.      │
│                 │                                        │ Thank you!"                            │
└─────────────────┴────────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 🎙️ Recording Tips & Checklist for Students

1. **Software:** Use OBS Studio, Loom, or Windows Game Bar (`Win + G`) to record screen + microphone.
2. **Resolution:** Record in 1080p (1920x1080) at 30 or 60 fps.
3. **Pacing:** Keep speech crisp and energetic. Do not pause during model loading (use the High-Fidelity Simulation mode in the app for instant responses).
4. **Export Format:** Export as MP4 format under 150 MB for easy LMS submission or YouTube Reel upload.
