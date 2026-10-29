"""
PromptShield-AI: Architecture Diagram Generator
Generates publication-quality PNG diagrams for the Milestone 2 submission folder.
Replaces Mermaid diagrams (which only render in live markdown viewers) with
portable, high-resolution images suitable for PDF/HTML reports.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Shared Style ────────────────────────────────────────────────────────────

COLORS = {
    "input":     "#4A90D9",
    "execution": "#E67E22",
    "eval":      "#27AE60",
    "defense":   "#C0392B",
    "safe":      "#2ECC71",
    "bg":        "#FAFBFC",
    "text":      "#2C3E50",
    "arrow":     "#7F8C8D",
    "v1":        "#E74C3C",
    "v2":        "#E67E22",
    "v3":        "#F1C40F",
    "v4":        "#2ECC71",
}

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 11,
    "axes.facecolor": COLORS["bg"],
    "figure.facecolor": "#FFFFFF",
})


def draw_box(ax, xy, w, h, label, color, fontsize=10, bold=False):
    """Draw a rounded box with centered label."""
    x, y = xy
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle="round,pad=0.15",
                         facecolor=color, edgecolor="#34495E",
                         linewidth=1.5, alpha=0.92, zorder=2)
    ax.add_patch(box)
    weight = "bold" if bold else "normal"
    ax.text(x + w / 2, y + h / 2, label,
            ha="center", va="center", fontsize=fontsize,
            fontweight=weight, color="white" if color not in ["#F1C40F", "#FAFBFC"] else "#2C3E50",
            wrap=True, zorder=3)


def draw_arrow(ax, start, end, color="#7F8C8D", style="-|>"):
    """Draw a simple arrow between two points."""
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle=style, color=color, lw=2),
                zorder=1)


# ═══════════════════════════════════════════════════════════════════════════════
# DIAGRAM 1: End-to-End System Architecture
# ═══════════════════════════════════════════════════════════════════════════════

def generate_system_architecture():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    fig.suptitle("PromptShield-AI: End-to-End System Architecture",
                 fontsize=18, fontweight="bold", color=COLORS["text"], y=0.97)

    # Phase labels
    phases = [
        (0.3, 8.2, "INPUT PHASE", "#3498DB"),
        (4.5, 8.2, "EXECUTION & RED-TEAMING", "#E67E22"),
        (9.0, 8.2, "AUTOMATED EVALUATION", "#27AE60"),
        (13.0, 8.2, "DEFENSE & SYNTHESIS", "#C0392B"),
    ]
    for px, py, plabel, pcol in phases:
        ax.text(px, py, plabel, fontsize=9, fontweight="bold", color=pcol,
                bbox=dict(boxstyle="round,pad=0.3", facecolor=pcol, alpha=0.12, edgecolor=pcol))

    # Input Phase boxes
    draw_box(ax, (0.2, 6.5), 3.2, 1.2, "Candidate\nSystem Prompt", COLORS["input"], 11, True)
    draw_box(ax, (0.2, 4.5), 3.2, 1.2, "Adversarial Test Suite\n(30 Scenarios × 6 OWASP)", COLORS["input"], 10)

    # Execution Phase
    draw_box(ax, (4.5, 5.5), 3.5, 1.2, "Execution Engine\n(Live LLM / HiFi Simulator)", COLORS["execution"], 10, True)
    draw_box(ax, (4.5, 3.5), 3.5, 1.0, "Target Response\nGeneration", COLORS["execution"], 10)

    # Evaluation Phase
    draw_box(ax, (9.0, 6.0), 3.5, 1.2, "Rubric-Grounded\nJudge-LLM Evaluator", COLORS["eval"], 10, True)
    draw_box(ax, (9.0, 4.2), 3.5, 1.0, "5-Point Safety Rubric\n& Ground-Truth Contracts", "#1ABC9C", 9)
    draw_box(ax, (9.0, 2.5), 3.5, 1.0, "Structured JSON\nAudit Report", COLORS["eval"], 10)

    # Defense Phase
    draw_box(ax, (13.0, 6.0), 2.7, 1.2, "Vulnerability\nScore ≥ 4?", COLORS["defense"], 10, True)
    draw_box(ax, (13.0, 4.0), 2.7, 1.0, "Adaptive Guardrail\nSynthesizer", "#8E44AD", 10, True)
    draw_box(ax, (13.0, 2.0), 2.7, 1.0, "Production\nCertified Prompt", COLORS["safe"], 10, True)

    # Arrows: Input → Execution
    draw_arrow(ax, (3.4, 7.1), (4.5, 6.3))
    draw_arrow(ax, (3.4, 5.1), (4.5, 5.9))

    # Execution → Response
    draw_arrow(ax, (6.25, 5.5), (6.25, 4.5))

    # Response → Judge
    draw_arrow(ax, (8.0, 4.0), (9.0, 6.5))

    # Rubric → Judge
    draw_arrow(ax, (10.75, 5.2), (10.75, 6.0))

    # Judge → JSON Report
    draw_arrow(ax, (10.75, 6.0), (10.75, 3.5), style="-|>")
    draw_arrow(ax, (10.75, 3.5), (10.75, 2.5), style="-|>")

    # JSON → Decision
    draw_arrow(ax, (12.5, 3.0), (13.0, 6.5))

    # Decision → Synthesizer (Vulnerable) or Certified (Safe)
    ax.annotate("YES\n(Vulnerable)", xy=(14.35, 5.0), xytext=(14.35, 6.0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS["defense"], lw=2),
                fontsize=8, color=COLORS["defense"], ha="center", fontweight="bold")
    ax.annotate("NO\n(Secure)", xy=(14.35, 3.0), xytext=(14.35, 4.0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS["safe"], lw=2),
                fontsize=8, color=COLORS["safe"], ha="center", fontweight="bold")

    # Feedback loop: Synthesizer → back to Execution
    ax.annotate("", xy=(6.25, 4.5), xytext=(13.0, 4.4),
                arrowprops=dict(arrowstyle="-|>", color="#8E44AD", lw=2,
                                connectionstyle="arc3,rad=0.3", linestyle="dashed"))
    ax.text(9.5, 1.5, "↻ Re-evaluation loop", fontsize=9, fontstyle="italic", color="#8E44AD", ha="center")

    # Footer
    ax.text(8.0, 0.3, "PromptShield-AI · Bennett University · Prompt Engineering Milestone 2 · Sparsh Bansal & Ayushika Verma",
            ha="center", fontsize=8, color="#999999")

    fig.savefig(os.path.join(OUTPUT_DIR, "system_architecture.png"), dpi=200, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("[✓] Generated: diagrams/system_architecture.png")


# ═══════════════════════════════════════════════════════════════════════════════
# DIAGRAM 2: Multi-Tier Prompt Evolution (v1 → v4)
# ═══════════════════════════════════════════════════════════════════════════════

def generate_prompt_evolution():
    fig, ax = plt.subplots(figsize=(16, 7))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 7)
    ax.axis("off")
    fig.suptitle("Multi-Tier Prompt Iteration Architecture (Evolutionary Progression)",
                 fontsize=16, fontweight="bold", color=COLORS["text"], y=0.97)

    versions = [
        {
            "x": 0.3, "y": 2.0, "w": 3.2, "h": 3.0,
            "color": COLORS["v1"],
            "title": "v1 BASELINE",
            "lines": [
                "Natural Language Only",
                "• Secret in plain text",
                "• Zero delimiters",
                "• No negative constraints",
                "",
                "ASR: 100.0%",
            ],
            "asr": "100.0%"
        },
        {
            "x": 4.3, "y": 2.0, "w": 3.2, "h": 3.0,
            "color": COLORS["v2"],
            "title": "v2 STRUCTURAL",
            "lines": [
                "XML Boundary Isolation",
                "• <system_role> tags",
                "• <user_input> slot",
                "• Direct inject blocked",
                "",
                "ASR: 53.8%",
            ],
            "asr": "53.8%"
        },
        {
            "x": 8.3, "y": 2.0, "w": 3.2, "h": 3.0,
            "color": "#D4AC0D",
            "title": "v3 CONSTITUTIONAL",
            "lines": [
                "Constitutional Guardrails",
                "• Immutable invariants",
                "• Negative constraints",
                "• Refusal guidelines",
                "",
                "ASR: 19.2%",
            ],
            "asr": "19.2%"
        },
        {
            "x": 12.3, "y": 2.0, "w": 3.2, "h": 3.0,
            "color": COLORS["v4"],
            "title": "v4 ADAPTIVE SHIELD",
            "lines": [
                "Defense-in-Depth",
                "• Data vs Code separation",
                "• Canary token isolation",
                "• Dual-Intent Gating",
                "• Few-shot refusals",
                "ASR: 0.0%",
            ],
            "asr": "0.0%"
        },
    ]

    for v in versions:
        box = FancyBboxPatch((v["x"], v["y"]), v["w"], v["h"],
                             boxstyle="round,pad=0.2",
                             facecolor=v["color"], edgecolor="#2C3E50",
                             linewidth=2, alpha=0.88, zorder=2)
        ax.add_patch(box)

        # Title
        ax.text(v["x"] + v["w"] / 2, v["y"] + v["h"] - 0.35, v["title"],
                ha="center", va="center", fontsize=11, fontweight="bold",
                color="white" if v["color"] != "#D4AC0D" else "#2C3E50", zorder=3)

        # Body lines
        for i, line in enumerate(v["lines"]):
            y_pos = v["y"] + v["h"] - 0.75 - i * 0.38
            fc = "white" if v["color"] not in ["#D4AC0D", "#F1C40F"] else "#2C3E50"
            fw = "bold" if "ASR:" in line else "normal"
            fs = 10 if "ASR:" in line else 9
            ax.text(v["x"] + v["w"] / 2, y_pos, line,
                    ha="center", va="center", fontsize=fs, fontweight=fw, color=fc, zorder=3)

    # Arrows between versions
    arrow_labels = [
        "Add XML\nDelimiters",
        "Add Constitutional\nInvariants",
        "Add Dual-Intent\nGating & Canary\nProtection",
    ]
    for i in range(3):
        sx = versions[i]["x"] + versions[i]["w"]
        ex = versions[i + 1]["x"]
        mid_y = 3.5
        ax.annotate("", xy=(ex, mid_y), xytext=(sx, mid_y),
                     arrowprops=dict(arrowstyle="-|>", color="#2C3E50", lw=2.5), zorder=4)
        ax.text((sx + ex) / 2, mid_y + 0.6, arrow_labels[i],
                ha="center", va="center", fontsize=8, fontstyle="italic", color="#555", zorder=3)

    # ASR progression bar at bottom
    asr_vals = [100.0, 53.8, 19.2, 0.0]
    bar_y = 1.0
    for i, (v, asr) in enumerate(zip(versions, asr_vals)):
        bw = (asr / 100.0) * 3.0
        bx = v["x"] + (v["w"] - 3.0) / 2
        bar = FancyBboxPatch((bx, bar_y), max(bw, 0.15), 0.5,
                             boxstyle="round,pad=0.05",
                             facecolor=v["color"], edgecolor="none", alpha=0.5, zorder=2)
        ax.add_patch(bar)
        ax.text(v["x"] + v["w"] / 2, bar_y + 0.25, f"ASR: {asr}%",
                ha="center", va="center", fontsize=9, fontweight="bold", color=COLORS["text"], zorder=3)

    ax.text(8.0, 0.35, "Attack Success Rate Progression (Lower = More Secure)",
            ha="center", fontsize=9, color="#888")

    fig.savefig(os.path.join(OUTPUT_DIR, "prompt_evolution.png"), dpi=200, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("[✓] Generated: diagrams/prompt_evolution.png")


# ═══════════════════════════════════════════════════════════════════════════════
# DIAGRAM 3: Defense-in-Depth Layers
# ═══════════════════════════════════════════════════════════════════════════════

def generate_defense_layers():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    fig.suptitle("PromptShield-AI: Defense-in-Depth Layer Architecture",
                 fontsize=16, fontweight="bold", color=COLORS["text"], y=0.97)

    layers = [
        {"y": 6.0, "h": 1.2, "color": "#3498DB", "alpha": 0.25,
         "title": "Layer 1: Structural Delimitation",
         "desc": "XML Boundary Isolation — <system_role>, <instructions>, <user_input>"},
        {"y": 4.3, "h": 1.2, "color": "#E67E22", "alpha": 0.30,
         "title": "Layer 2: Behavioral Constitution",
         "desc": "Immutable Invariants — Role preservation, negative constraints, privilege boundaries"},
        {"y": 2.6, "h": 1.2, "color": "#9B59B6", "alpha": 0.35,
         "title": "Layer 3: Cognitive Routing",
         "desc": "Dual-Intent Gating — Canary token isolation, Data vs Code separation"},
        {"y": 0.9, "h": 1.2, "color": "#2ECC71", "alpha": 0.40,
         "title": "Layer 4: Output Harmonization",
         "desc": "Standardized Polite Refusal — Few-shot demonstrations, Benign Utility Preserved"},
    ]

    for i, layer in enumerate(layers):
        # Outer shaded region (gets narrower deeper = onion model)
        inset = i * 0.5
        rect = FancyBboxPatch((0.5 + inset, layer["y"]), 11.0 - 2 * inset, layer["h"],
                              boxstyle="round,pad=0.2",
                              facecolor=layer["color"], edgecolor=layer["color"],
                              linewidth=2.5, alpha=layer["alpha"], zorder=2)
        ax.add_patch(rect)

        ax.text(6.0, layer["y"] + layer["h"] - 0.3, layer["title"],
                ha="center", va="center", fontsize=13, fontweight="bold",
                color=layer["color"], zorder=3)
        ax.text(6.0, layer["y"] + 0.3, layer["desc"],
                ha="center", va="center", fontsize=9, color="#444", zorder=3)

        if i < 3:
            ax.annotate("", xy=(6.0, layer["y"]), xytext=(6.0, layer["y"] - 0.25),
                         arrowprops=dict(arrowstyle="-|>", color="#AAA", lw=1.5), zorder=1)

    # Attacker arrow from top
    ax.annotate("Adversarial\nPayload", xy=(6.0, 7.2), xytext=(6.0, 7.8),
                fontsize=10, fontweight="bold", color=COLORS["v1"], ha="center",
                arrowprops=dict(arrowstyle="-|>", color=COLORS["v1"], lw=2.5))

    # Bottom safe output
    ax.text(6.0, 0.3, "✓ Safe, Helpful Response Delivered to User",
            ha="center", fontsize=11, fontweight="bold", color=COLORS["v4"])

    fig.savefig(os.path.join(OUTPUT_DIR, "defense_layers.png"), dpi=200, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("[✓] Generated: diagrams/defense_layers.png")


# ═══════════════════════════════════════════════════════════════════════════════
# DIAGRAM 4: Software Module Architecture
# ═══════════════════════════════════════════════════════════════════════════════

def generate_software_architecture():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")
    fig.suptitle("PromptShield-AI: Software & Component Architecture",
                 fontsize=16, fontweight="bold", color=COLORS["text"], y=0.97)

    # User-Facing Layer
    ax.text(7.0, 7.5, "USER-FACING INTERFACES", fontsize=11, fontweight="bold",
            color="#2980B9", ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#2980B9", alpha=0.1, edgecolor="#2980B9"))

    draw_box(ax, (0.5, 5.8), 3.5, 1.2, "Chatbot Defense Portal\n(FastAPI + HTML/CSS/JS)\nweb/ + src/server.py", "#2980B9", 9, True)
    draw_box(ax, (5.0, 5.8), 3.8, 1.2, "Streamlit Analytics Dashboard\n(5-Tab Interactive UI)\nsrc/app.py", "#2980B9", 9, True)
    draw_box(ax, (9.8, 5.8), 3.8, 1.2, "CLI Benchmark Auditor\n(Batch Red-Team Pipeline)\nsrc/pipeline.py", "#2980B9", 9, True)

    # Core Engine Layer
    ax.text(7.0, 5.1, "CORE ENGINE LAYER", fontsize=11, fontweight="bold",
            color="#E67E22", ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#E67E22", alpha=0.1, edgecolor="#E67E22"))

    draw_box(ax, (0.5, 3.3), 4.0, 1.3, "Evaluation Engine\n• Live API (Gemini/OpenAI)\n• HiFi Deterministic Simulator\nsrc/pipeline.py", "#E67E22", 9)
    draw_box(ax, (5.3, 3.3), 3.5, 1.3, "Judge-LLM Evaluator\n• 5-Point Likert Rubric\n• JSON Schema Scoring\nsrc/pipeline.py", "#27AE60", 9)
    draw_box(ax, (9.5, 3.3), 4.0, 1.3, "Guardrail Synthesizer\n• Auto-Hardening Engine\n• XML + Canary + Gating\nsrc/synthesizer.py", "#8E44AD", 9)

    # Data & Prompt Layer
    ax.text(7.0, 2.6, "DATA & PROMPT LAYER", fontsize=11, fontweight="bold",
            color="#16A085", ha="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#16A085", alpha=0.1, edgecolor="#16A085"))

    draw_box(ax, (0.3, 0.8), 3.0, 1.3, "Prompt Library\nprompts/\nv1 → v4 iterations\nevaluators, red_team,\nsynthesizers", "#16A085", 8)
    draw_box(ax, (3.8, 0.8), 3.0, 1.3, "Benchmark Suite\nexperiments/\n30 Test Cases (JSON)\n26 Adversarial\n4 Benign Controls", "#16A085", 8)
    draw_box(ax, (7.3, 0.8), 3.0, 1.3, "Evaluation Assets\nexperiments/figures/\nASR Charts\nRadar Profiles\nCategory Breakdowns", "#16A085", 8)
    draw_box(ax, (10.8, 0.8), 2.8, 1.3, "Research & Docs\nresearch/\nTechnical Report\nvideo/\nStoryboard", "#16A085", 8)

    # Connecting arrows (simplified vertical)
    for x_mid in [2.5, 6.9, 11.7]:
        draw_arrow(ax, (x_mid, 5.8), (x_mid, 4.6), color="#CCC")
    for x_mid in [2.5, 7.0, 11.5]:
        draw_arrow(ax, (x_mid, 3.3), (x_mid, 2.1), color="#CCC")

    fig.savefig(os.path.join(OUTPUT_DIR, "software_architecture.png"), dpi=200, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("[✓] Generated: diagrams/software_architecture.png")


# ═══════════════════════════════════════════════════════════════════════════════
# DIAGRAM 5: Threat Taxonomy Visual
# ═══════════════════════════════════════════════════════════════════════════════

def generate_threat_taxonomy():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis("off")
    fig.suptitle("OWASP LLM01/LLM02 Threat Vector Taxonomy — PromptShield-AI Benchmark Coverage",
                 fontsize=14, fontweight="bold", color=COLORS["text"], y=0.97)

    threats = [
        {"label": "Direct\nInjection", "count": 5, "color": "#E74C3C", "x": 0.5},
        {"label": "Persona\nJailbreaking", "count": 5, "color": "#E67E22", "x": 2.7},
        {"label": "Prompt\nExtraction", "count": 5, "color": "#F39C12", "x": 4.9},
        {"label": "Delimiter\nHijacking", "count": 5, "color": "#9B59B6", "x": 7.1},
        {"label": "Encoding\nObfuscation", "count": 4, "color": "#3498DB", "x": 9.3},
        {"label": "Indirect\nInjection", "count": 2, "color": "#1ABC9C", "x": 11.5},
    ]

    for t in threats:
        box = FancyBboxPatch((t["x"], 1.5), 1.8, 3.0,
                             boxstyle="round,pad=0.2",
                             facecolor=t["color"], edgecolor="#2C3E50",
                             linewidth=1.5, alpha=0.85, zorder=2)
        ax.add_patch(box)
        ax.text(t["x"] + 0.9, 3.8, t["label"],
                ha="center", va="center", fontsize=10, fontweight="bold", color="white", zorder=3)
        ax.text(t["x"] + 0.9, 2.8, f"{t['count']} Test\nCases",
                ha="center", va="center", fontsize=10, color="white", zorder=3)

        # Defense status
        ax.text(t["x"] + 0.9, 1.9, "v4: 0% ASR ✓",
                ha="center", va="center", fontsize=8, fontweight="bold", color="#E8F8F5", zorder=3)

    # Benign controls
    box = FancyBboxPatch((5.5, 0.2), 3.0, 0.9,
                         boxstyle="round,pad=0.15",
                         facecolor="#2ECC71", edgecolor="#27AE60",
                         linewidth=1.5, alpha=0.8, zorder=2)
    ax.add_patch(box)
    ax.text(7.0, 0.65, "Benign Baseline Controls: 4 Legitimate Queries → 100% BUR ✓",
            ha="center", va="center", fontsize=9, fontweight="bold", color="white", zorder=3)

    ax.text(7.0, 5.3, "26 Adversarial Attacks + 4 Benign Controls = 30 Total Test Scenarios",
            ha="center", fontsize=10, color="#555")

    fig.savefig(os.path.join(OUTPUT_DIR, "threat_taxonomy.png"), dpi=200, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("[✓] Generated: diagrams/threat_taxonomy.png")


# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PromptShield-AI: Generating Submission Diagrams")
    print("=" * 60)
    generate_system_architecture()
    generate_prompt_evolution()
    generate_defense_layers()
    generate_software_architecture()
    generate_threat_taxonomy()
    print("=" * 60)
    print(f"All diagrams saved to: {OUTPUT_DIR}")
