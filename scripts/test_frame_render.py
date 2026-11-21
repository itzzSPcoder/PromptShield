import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def draw_chrome_browser_frame(viewport_img, url="https://promptshield.sparsh2005bansal.workers.dev/"):
    vw, vh = viewport_img.size
    chrome_header_h = 76
    total_w = vw
    total_h = vh + chrome_header_h
    
    # Create canvas
    frame = Image.new("RGB", (total_w, total_h), (241, 243, 244)) # Chrome grey
    draw = ImageDraw.Draw(frame)
    
    # 1. Tab strip (height 36)
    tab_x, tab_y, tab_w, tab_h = 75, 6, 260, 30
    draw.rounded_rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h + 4], radius=8, fill=(255, 255, 255))
    
    # Shield icon in tab
    draw.ellipse([tab_x + 12, tab_y + 8, tab_x + 24, tab_y + 20], fill=(26, 115, 232))
    
    # Font
    try:
        font_tab = ImageFont.truetype("arial.ttf", 12)
        font_url = ImageFont.truetype("arial.ttf", 13)
        font_btn = ImageFont.truetype("arial.ttf", 14)
    except:
        font_tab = font_url = font_btn = ImageFont.load_default()
        
    draw.text((tab_x + 32, tab_y + 8), "PromptShield AI // Defense", fill=(60, 64, 67), font=font_tab)
    draw.text((tab_x + tab_w - 20, tab_y + 8), "×", fill=(128, 134, 139), font=font_tab)
    
    # Window controls (right)
    draw.text((total_w - 110, 10), "—", fill=(95, 99, 104), font=font_btn)
    draw.rectangle([total_w - 75, 12, total_w - 63, 22], outline=(95, 99, 104), width=1)
    draw.text((total_w - 35, 10), "✕", fill=(95, 99, 104), font=font_btn)
    
    # 2. Navigation / URL bar row (y: 36 to 76)
    draw.rectangle([0, 36, total_w, chrome_header_h], fill=(255, 255, 255))
    draw.line([0, chrome_header_h - 1, total_w, chrome_header_h - 1], fill=(218, 220, 224), width=1)
    
    # Nav buttons
    draw.text((16, 46), "←", fill=(128, 134, 139), font=font_btn)
    draw.text((44, 46), "→", fill=(180, 184, 189), font=font_btn)
    draw.text((72, 46), "⟳", fill=(95, 99, 104), font=font_btn)
    
    # URL pill
    url_box = [105, 41, total_w - 90, 69]
    draw.rounded_rectangle(url_box, radius=14, fill=(241, 243, 244))
    
    # Lock icon
    draw.text((120, 47), "🔒", fill=(24, 128, 56), font=font_tab)
    
    # URL text
    draw.text((142, 47), url, fill=(32, 33, 36), font=font_url)
    
    # Bookmark & profile icons
    draw.text((total_w - 120, 47), "★", fill=(128, 134, 139), font=font_tab)
    draw.ellipse([total_w - 65, 43, total_w - 41, 67], fill=(26, 115, 232))
    draw.text((total_w - 58, 48), "A", fill=(255, 255, 255), font=font_tab) # Ayushika profile
    
    # Paste viewport
    frame.paste(viewport_img, (0, chrome_header_h))
    return frame

# Test with test_local_chrome.png
im = Image.open("test_local_chrome.png")
result = draw_chrome_browser_frame(im)
result.save("test_chrome_wrapped.png")
print("Saved test_chrome_wrapped.png size:", result.size)
