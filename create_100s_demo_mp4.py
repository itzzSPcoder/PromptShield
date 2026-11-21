"""
Generate exact 100-second 720p MP4 demonstration video for Team NullPointers.
File: NullPointers_Demo_Video.mp4
Duration: 100.0 Seconds (2400 frames @ 24 fps)
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(ROOT, "submission")
DIAG = os.path.join(SUB, "diagrams")
SCREENS = os.path.join(SUB, "screenshots")
DEMO_DIR = os.path.join(SUB, "demo_video")

WIDTH, HEIGHT = 1280, 720
FPS = 24
TOTAL_SECONDS = 100
TOTAL_FRAMES = FPS * TOTAL_SECONDS

def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\calibri.ttf"
    ]
    for fn in font_names:
        if os.path.exists(fn):
            try:
                return ImageFont.truetype(fn, size)
            except:
                pass
    return ImageFont.load_default()

font_title = get_font(28, bold=True)
font_sec = get_font(18, bold=True)
font_sub = get_font(15, bold=False)
font_cue = get_font(14, bold=True)
font_meta = get_font(13, bold=False)

def create_scene_frame(header_text, timestamp_text, main_img_path, cue_text):
    # Base canvas with modern dark academic styling
    canvas = Image.new("RGB", (WIDTH, HEIGHT), color=(14, 20, 32))
    draw = ImageDraw.Draw(canvas)

    # Top banner bar
    draw.rectangle([(0, 0), (WIDTH, 64)], fill=(22, 30, 48))
    draw.line([(0, 64), (WIDTH, 64)], fill=(56, 189, 248), width=2)

    # University & Project Branding on Left
    draw.text((24, 12), "PROMPTSHIELD-AI  //  BENNETT UNIVERSITY", font=font_sec, fill=(56, 189, 248))
    draw.text((24, 38), "Team NullPointers (PE-B25-33) • Presenter: Ayushika Verma", font=font_meta, fill=(148, 163, 184))

    # Scene Title & Timestamp on Right
    draw.text((WIDTH - 420, 12), header_text, font=font_sec, fill=(255, 255, 255))
    draw.text((WIDTH - 420, 38), f"Timer: {timestamp_text} (Target: 100s)", font=font_meta, fill=(16, 185, 129))

    # Bottom Audio Cue Bar
    draw.rectangle([(0, HEIGHT - 54), (WIDTH, HEIGHT)], fill=(18, 26, 42))
    draw.line([(0, HEIGHT - 54), (WIDTH, HEIGHT - 54)], fill=(31, 45, 66), width=1)
    draw.text((24, HEIGHT - 38), f"AUDIO CUE: {cue_text}", font=font_cue, fill=(245, 158, 11))

    # Center Content Image
    if main_img_path and os.path.exists(main_img_path):
        try:
            content_img = Image.open(main_img_path).convert("RGBA")
            # Calculate max box for content: (WIDTH - 80, HEIGHT - 140)
            max_w = WIDTH - 80
            max_h = HEIGHT - 144
            scale = min(max_w / content_img.width, max_h / content_img.height, 1.0)
            new_w = int(content_img.width * scale)
            new_h = int(content_img.height * scale)
            content_resized = content_img.resize((new_w, new_h), Image.Resampling.LANCZOS)

            pos_x = (WIDTH - new_w) // 2
            pos_y = 64 + (max_h - new_h) // 2 + 10

            # Card background behind content
            card_box = [(pos_x - 4, pos_y - 4), (pos_x + new_w + 4, pos_y + new_h + 4)]
            draw.rectangle(card_box, fill=(255, 255, 255))
            canvas.paste(content_resized, (pos_x, pos_y), content_resized)
        except Exception as e:
            print(f"Error loading {main_img_path}: {e}")

    # Convert to OpenCV BGR
    return cv2.cvtColor(np.array(canvas), cv2.COLOR_RGB2BGR)

def generate_video():
    scenes = [
        {
            "header": "Scene 1: Threat Model & Conflation",
            "time_range": "0:00 - 0:15",
            "duration": 15,
            "image": os.path.join(DIAG, "threat_taxonomy.png"),
            "cue": "Ayushika: 'Welcome to PromptShield-AI... LLMs conflate system instructions with untrusted user data.'"
        },
        {
            "header": "Scene 2: 4-Layer Defense Architecture",
            "time_range": "0:15 - 0:32",
            "duration": 17,
            "image": os.path.join(DIAG, "defense_layers.png"),
            "cue": "Ayushika: 'We engineer 4 in-context layers: XML tags, canary token invariants, dual-intent gating.'"
        },
        {
            "header": "Scene 3: Live Pilot Run - Baseline Breach",
            "time_range": "0:32 - 0:54",
            "duration": 22,
            "image": os.path.join(SCREENS, "red_team_attack_demo.png"),
            "cue": "Ayushika: 'On baseline prompt, attacker overrides instructions; canary ALPHA-99-ZENITH leaks (Score 5).'"
        },
        {
            "header": "Scene 4: Live Pilot Run - Hardened v4 Defense",
            "time_range": "0:54 - 1:16",
            "duration": 22,
            "image": os.path.join(SCREENS, "shield_enabled_state.png"),
            "cue": "Ayushika: 'With v4 shield active, same attack is isolated; canary safe, standardized polite refusal (Score 1).'"
        },
        {
            "header": "Scene 5: 30-Case Benchmark Suite & Metrics",
            "time_range": "1:16 - 1:32",
            "duration": 16,
            "image": os.path.join(DIAG, "prompt_evolution.png"),
            "cue": "Ayushika: 'Across 30 OWASP test cases, Attack Success Rate drops from 100% to 0%, BUR is 100%.'"
        },
        {
            "header": "Scene 6: Live Deployment & Deliverables",
            "time_range": "1:32 - 1:40",
            "duration": 8,
            "image": os.path.join(SCREENS, "main_chatbot_interface.png"),
            "cue": "Ayushika: 'Live prototype deployed on Cloudflare Workers, code on GitHub. Thank you from Team NullPointers!'"
        }
    ]

    out_root = os.path.join(ROOT, "NullPointers_Demo_Video.mp4")
    out_sub = os.path.join(DEMO_DIR, "PromptShield_AI_Milestone2_Demo.mp4")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(out_root, fourcc, FPS, (WIDTH, HEIGHT))

    print(f"[INFO] Rendering 100-second MP4 ({TOTAL_FRAMES} frames @ {FPS} fps)...")

    frame_counter = 0
    for idx, sc in enumerate(scenes):
        sc_frames = sc["duration"] * FPS
        frame_bgr = create_scene_frame(sc["header"], sc["time_range"], sc["image"], sc["cue"])
        
        for f in range(sc_frames):
            writer.write(frame_bgr)
            frame_counter += 1

    writer.release()
    print(f"[SUCCESS] Wrote {frame_counter} frames ({frame_counter/FPS:.1f}s) to: {out_root}")

    # Copy to submission directory as well
    import shutil
    shutil.copyfile(out_root, out_sub)
    print(f"[SUCCESS] Copied to submission: {out_sub}")

if __name__ == "__main__":
    generate_video()
