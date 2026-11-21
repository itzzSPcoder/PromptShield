import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import math

def draw_chrome_browser_frame(viewport_img, url="https://promptshield.sparsh2005bansal.workers.dev/"):
    vw, vh = viewport_img.size
    chrome_header_h = 76
    total_w = vw
    total_h = vh + chrome_header_h
    
    # Chrome window background
    frame = Image.new("RGB", (total_w, total_h), (241, 243, 244))
    draw = ImageDraw.Draw(frame)
    
    # Fonts
    try:
        font_tab = ImageFont.truetype("arial.ttf", 12)
        font_url = ImageFont.truetype("arial.ttf", 13)
        font_btn = ImageFont.truetype("arial.ttf", 14)
    except:
        font_tab = font_url = font_btn = ImageFont.load_default()
        
    # 1. Tab bar
    tab_x, tab_y, tab_w, tab_h = 75, 6, 270, 30
    draw.rounded_rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h + 4], radius=8, fill=(255, 255, 255))
    draw.ellipse([tab_x + 12, tab_y + 8, tab_x + 24, tab_y + 20], fill=(26, 115, 232)) # Blue shield circle
    draw.text((tab_x + 32, tab_y + 8), "PromptShield AI // Chatbot Defense", fill=(60, 64, 67), font=font_tab)
    draw.text((tab_x + tab_w - 20, tab_y + 8), "×", fill=(128, 134, 139), font=font_tab)
    
    # Window controls
    draw.text((total_w - 110, 10), "—", fill=(95, 99, 104), font=font_btn)
    draw.rectangle([total_w - 75, 12, total_w - 63, 22], outline=(95, 99, 104), width=1)
    draw.text((total_w - 35, 10), "✕", fill=(95, 99, 104), font=font_btn)
    
    # 2. Navigation & Address bar
    draw.rectangle([0, 36, total_w, chrome_header_h], fill=(255, 255, 255))
    draw.line([0, chrome_header_h - 1, total_w, chrome_header_h - 1], fill=(218, 220, 224), width=1)
    
    draw.text((16, 46), "←", fill=(128, 134, 139), font=font_btn)
    draw.text((44, 46), "→", fill=(180, 184, 189), font=font_btn)
    draw.text((72, 46), "⟳", fill=(95, 99, 104), font=font_btn)
    
    # Address bar pill
    draw.rounded_rectangle([105, 41, total_w - 90, 69], radius=14, fill=(241, 243, 244))
    draw.text((120, 48), "🔒", fill=(24, 128, 56), font=font_tab)
    draw.text((142, 47), url, fill=(32, 33, 36), font=font_url)
    
    draw.text((total_w - 120, 47), "★", fill=(128, 134, 139), font=font_tab)
    draw.ellipse([total_w - 65, 43, total_w - 41, 67], fill=(26, 115, 232))
    draw.text((total_w - 58, 48), "A", fill=(255, 255, 255), font=font_tab) # Ayushika profile icon
    
    # Paste web viewport
    frame.paste(viewport_img, (0, chrome_header_h))
    return frame

def draw_cursor(draw, x, y, is_clicking=False, click_phase=0.0):
    # Shadow
    poly_shadow = [(x + 1, y + 1), (x + 1, y + 16), (x + 5, y + 12), (x + 8, y + 19), (x + 11, y + 18), (x + 7, y + 11), (x + 12, y + 11)]
    draw.polygon(poly_shadow, fill=(0, 0, 0))
    # Main white arrow with black stroke
    poly = [(x, y), (x, y + 15), (x + 4, y + 11), (x + 7, y + 18), (x + 10, y + 17), (x + 6, y + 10), (x + 11, y + 10)]
    draw.polygon(poly, fill=(255, 255, 255), outline=(30, 30, 30))
    
    if is_clicking and click_phase > 0:
        r = int(5 + 16 * click_phase)
        alpha_color = (26, 115, 232)
        draw.ellipse([x - r, y - r, x + r, y + r], outline=alpha_color, width=2)

def draw_subtitle_bar(draw, text, act_tag, width, height):
    # Professional broadcast lower-third subtitle bar
    bar_h = 44
    bar_y = height - bar_h - 10
    margin = 30
    
    # Translucent pill background
    draw.rounded_rectangle([margin, bar_y, width - margin, bar_y + bar_h], radius=8, fill=(20, 24, 33))
    
    try:
        font_tag = ImageFont.truetype("arialbd.ttf", 12)
        font_sub = ImageFont.truetype("arial.ttf", 13)
    except:
        font_tag = font_sub = ImageFont.load_default()
        
    # Tag pill
    draw.rounded_rectangle([margin + 8, bar_y + 8, margin + 170, bar_y + 36], radius=4, fill=(37, 99, 235))
    draw.text((margin + 16, bar_y + 14), act_tag, fill=(255, 255, 255), font=font_tag)
    
    # Subtitle text
    draw.text((margin + 185, bar_y + 14), text, fill=(240, 243, 246), font=font_sub)

def ease_in_out(t):
    return t * t * (3.0 - 2.0 * t)

def interpolate_pos(p1, p2, t):
    t_e = ease_in_out(max(0.0, min(1.0, t)))
    return (
        int(p1[0] + (p2[0] - p1[0]) * t_e),
        int(p1[1] + (p2[1] - p1[1]) * t_e)
    )

def main():
    print("Loading captured browser states...")
    states = {}
    state_names = [
        "state0_initial.png",
        "state1_typed_prompt.png",
        "state2_thinking.png",
        "state3_breach_response.png",
        "state4_audit_20.png",
        "state5_audit_60.png",
        "state6_audit_100.png",
        "state7_hardened_active.png",
        "state8_defended_response.png",
        "state9_prompt_modal.png",
        "state10_prompt_scrolled.png",
        "state11_conclusion.png"
    ]
    for name in state_names:
        path = os.path.join("demo_frames", name)
        states[name] = Image.open(path).convert("RGB")
        
    # Video specs: 25 fps, 100.0 seconds -> 2500 frames exactly
    fps = 25
    total_frames = 2500
    
    # Dimensions
    vw, vh = states["state0_initial.png"].size
    chrome_h = 76
    out_w = vw
    out_h = vh + chrome_h
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    temp_video = "temp_recording.mp4"
    out = cv2.VideoWriter(temp_video, fourcc, fps, (out_w, out_h))
    
    print(f"Generating {total_frames} frames ({out_w}x{out_h}) at {fps} fps (Duration: 100.0 seconds)...")
    
    # Scripted timeline schedule:
    # Frame ranges:
    # 0 - 300 (0s - 12s): Intro (state0)
    # 300 - 625 (12s - 25s): Attack Selection & Submit (state0 -> state1 -> state2)
    # 625 - 1050 (25s - 42s): Breach Leak Analysis (state3)
    # 1050 - 1550 (42s - 62s): 1-Click Auto-Audit & Hardening (state4 -> state5 -> state6 -> state7)
    # 1550 - 2000 (62s - 80s): Neutralized Injection & Verification (state7 -> state8)
    # 2000 - 2300 (80s - 92s): Inspect System Prompt Architecture (state9 -> state10)
    # 2300 - 2500 (92s - 100s): Conclusion, Team PE-B25-33 & Live Links (state11)

    for f in range(total_frames):
        t_sec = f / fps
        is_click = False
        click_phase = 0.0
        
        # Determine base viewport, cursor position, and subtitle
        if f < 300: # 0.0s - 12.0s: Intro
            base_img = states["state0_initial.png"]
            tag = "AYUSHIKA VERMA · INTRO"
            sub = "Welcome. I am Ayushika Verma representing Team NullPointers. Today, we demonstrate PromptShield AI live."
            
            # Cursor glides: center -> brand (162, 40) -> botCard (162, 158) -> sidebar
            if f < 100:
                pos = interpolate_pos((640, 360 + chrome_h), (162, 40 + chrome_h), f / 100.0)
            elif f < 200:
                pos = interpolate_pos((162, 40 + chrome_h), (162, 158 + chrome_h), (f - 100) / 100.0)
            else:
                pos = interpolate_pos((162, 158 + chrome_h), (162, 350 + chrome_h), (f - 200) / 100.0)

        elif f < 625: # 12.0s - 25.0s: Attack Selection & Submit
            tag = "ACT 1 · ATTACK EXECUTION"
            sub = "Under baseline v1, we launch a direct jailbreak attack requesting confidential clearance keys."
            
            # Cursor moves to preset chip 2 (162, 518) -> clicks at 400 -> moves to sendBtn (1192, 500) -> clicks at 550
            if f < 400:
                base_img = states["state0_initial.png"]
                pos = interpolate_pos((162, 350 + chrome_h), (162, 518 + chrome_h), (f - 300) / 100.0)
            elif f < 430:
                base_img = states["state1_typed_prompt.png"]
                pos = (162, 518 + chrome_h)
                is_click = True
                click_phase = (f - 400) / 30.0
            elif f < 550:
                base_img = states["state1_typed_prompt.png"]
                pos = interpolate_pos((162, 518 + chrome_h), (1192, 500 + chrome_h), (f - 430) / 120.0)
            elif f < 580:
                base_img = states["state2_thinking.png"]
                pos = (1192, 500 + chrome_h)
                is_click = True
                click_phase = (f - 550) / 30.0
            else:
                base_img = states["state2_thinking.png"]
                pos = (1192, 500 + chrome_h)

        elif f < 1050: # 25.0s - 42.0s: Breach & Canary Exfiltration
            base_img = states["state3_breach_response.png"]
            tag = "ACT 2 · BREACH CONFIRMED"
            sub = "Critical breach confirmed! The unhardened model leaks the canary token ALPHA-99-ZENITH (Likert: 5/5)."
            
            # Cursor moves over leaked token in chat bubble, then over red verdict badge
            if f < 750:
                pos = interpolate_pos((1192, 500 + chrome_h), (750, 280 + chrome_h), (f - 625) / 125.0)
            elif f < 900:
                pos = interpolate_pos((750, 280 + chrome_h), (750, 360 + chrome_h), (f - 750) / 150.0)
            else:
                pos = interpolate_pos((750, 360 + chrome_h), (162, 390 + chrome_h), (f - 900) / 150.0)

        elif f < 1550: # 42.0s - 62.0s: 1-Click Auto-Audit & Hardening
            tag = "ACT 3 · AUTO-AUDIT & HARDENING"
            sub = "With one click, PromptShield's automated engine audits the bot against OWASP vectors and hardens the prompt."
            
            # Click autoSecureBtn at 1100 -> audit modal opens
            if f < 1100:
                base_img = states["state3_breach_response.png"]
                pos = (162, 390 + chrome_h)
            elif f < 1130:
                base_img = states["state4_audit_20.png"]
                pos = (162, 390 + chrome_h)
                is_click = True
                click_phase = (f - 1100) / 30.0
            elif f < 1250:
                base_img = states["state4_audit_20.png"] # 20%
                pos = interpolate_pos((162, 390 + chrome_h), (640, 360 + chrome_h), (f - 1130) / 120.0)
            elif f < 1370:
                base_img = states["state5_audit_60.png"] # 60%
                pos = (640, 360 + chrome_h)
            elif f < 1470:
                base_img = states["state6_audit_100.png"] # 100% complete
                pos = interpolate_pos((640, 360 + chrome_h), (640, 505 + chrome_h), (f - 1370) / 100.0) # over finish btn
            elif f < 1500:
                base_img = states["state6_audit_100.png"]
                pos = (640, 505 + chrome_h)
                is_click = True
                click_phase = (f - 1470) / 30.0
            else:
                base_img = states["state7_hardened_active.png"]
                pos = interpolate_pos((640, 505 + chrome_h), (162, 518 + chrome_h), (f - 1500) / 50.0)

        elif f < 2000: # 62.0s - 80.0s: Re-testing Attack on Hardened Bot
            tag = "ACT 4 · ATTACK DEFLECTED"
            sub = "Re-submitting the identical attack. The synthesized XML boundaries and guardrails neutralize the injection."
            
            # Click preset at 1600 -> click send at 1700 -> state8 (defended)
            if f < 1600:
                base_img = states["state7_hardened_active.png"]
                pos = (162, 518 + chrome_h)
            elif f < 1630:
                base_img = states["state7_hardened_active.png"]
                pos = (162, 518 + chrome_h)
                is_click = True
                click_phase = (f - 1600) / 30.0
            elif f < 1700:
                base_img = states["state7_hardened_active.png"]
                pos = interpolate_pos((162, 518 + chrome_h), (1192, 500 + chrome_h), (f - 1630) / 70.0)
            elif f < 1730:
                base_img = states["state8_defended_response.png"]
                pos = (1192, 500 + chrome_h)
                is_click = True
                click_phase = (f - 1700) / 30.0
            else:
                base_img = states["state8_defended_response.png"]
                pos = interpolate_pos((1192, 500 + chrome_h), (750, 420 + chrome_h), (f - 1730) / 270.0)

        elif f < 2300: # 80.0s - 92.0s: Inspect System Prompt Architecture
            tag = "ACT 5 · DEFENSE ARCHITECTURE"
            sub = "Inspecting prompt guardrails: XML delimiter isolation, canary token integrity trap, and constitutional rules."
            
            # Click viewPromptBtn (1071, 33) at 2060 -> scroll prompt modal -> click close
            if f < 2060:
                base_img = states["state8_defended_response.png"]
                pos = interpolate_pos((750, 420 + chrome_h), (1071, 33 + chrome_h), (f - 2000) / 60.0)
            elif f < 2090:
                base_img = states["state9_prompt_modal.png"]
                pos = (1071, 33 + chrome_h)
                is_click = True
                click_phase = (f - 2060) / 30.0
            elif f < 2180:
                base_img = states["state9_prompt_modal.png"]
                pos = interpolate_pos((1071, 33 + chrome_h), (640, 350 + chrome_h), (f - 2090) / 90.0)
            elif f < 2250:
                base_img = states["state10_prompt_scrolled.png"]
                pos = interpolate_pos((640, 350 + chrome_h), (920, 160 + chrome_h), (f - 2180) / 70.0) # over modal close X
            elif f < 2280:
                base_img = states["state10_prompt_scrolled.png"]
                pos = (920, 160 + chrome_h)
                is_click = True
                click_phase = (f - 2250) / 30.0
            else:
                base_img = states["state11_conclusion.png"]
                pos = interpolate_pos((920, 160 + chrome_h), (162, 848 + chrome_h), (f - 2280) / 20.0)

        else: # 92.0s - 100.0s: Conclusion, Team PE-B25-33 & Live Links
            base_img = states["state11_conclusion.png"]
            tag = "TEAM PE-B25-33 · CONCLUSION"
            sub = "PromptShield AI: 0% ASR, 100% Benign Utility Rate. Live deployment & GitHub verified."
            
            # Hover over Team credentials in sidebar footer
            if f < 2420:
                pos = interpolate_pos((162, 848 + chrome_h), (162, 848 + chrome_h), 1.0)
            else:
                pos = interpolate_pos((162, 848 + chrome_h), (640, 58 + chrome_h), (f - 2420) / 80.0) # glide to URL bar
                
        # 1. Wrap in Chrome browser frame
        frame_img = draw_chrome_browser_frame(base_img)
        draw = ImageDraw.Draw(frame_img)
        
        # 2. Draw mouse cursor
        draw_cursor(draw, pos[0], pos[1], is_clicking=is_click, click_phase=click_phase)
        
        # 3. Draw subtitle banner
        draw_subtitle_bar(draw, sub, tag, out_w, out_h)
        
        # Convert to BGR for OpenCV
        frame_cv = cv2.cvtColor(np.array(frame_img), cv2.COLOR_RGB2BGR)
        out.write(frame_cv)
        
        if f % 250 == 0:
            print(f"Rendered {f}/{total_frames} frames ({int(t_sec)}s / 100s)...")
            
    out.release()
    print("Video generation finished!")
    
    # Save to both target locations
    target1 = "NullPointers_Demo_Video.mp4"
    target2 = os.path.join("submission", "demo_video", "PromptShield_AI_Milestone2_Demo.mp4")
    
    import shutil
    shutil.copyfile(temp_video, target1)
    shutil.copyfile(temp_video, target2)
    print(f"Saved: {target1} ({os.path.getsize(target1)} bytes)")
    print(f"Saved: {target2} ({os.path.getsize(target2)} bytes)")

if __name__ == "__main__":
    main()
