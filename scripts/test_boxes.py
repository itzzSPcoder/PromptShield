import subprocess
import time
import json
import urllib.request
import asyncio
import websockets

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
proc = subprocess.Popen([
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--remote-debugging-port=9222',
    '--user-data-dir=d:\\oldCoding\\Class\\Prompt\\temp_chrome',
    '--window-size=1280,720',
    'http://127.0.0.1:8000'
])
time.sleep(2)

async def check_boxes():
    with urllib.request.urlopen('http://127.0.0.1:9222/json') as resp:
        tabs = json.loads(resp.read().decode())
    page_tab = [t for t in tabs if t.get('type') == 'page'][0]
    async with websockets.connect(page_tab['webSocketDebuggerUrl'], max_size=20_000_000) as ws:
        js = """
        (function() {
            function box(sel) {
                const el = document.querySelector(sel);
                if (!el) return null;
                const r = el.getBoundingClientRect();
                return {x: Math.round(r.left + r.width/2), y: Math.round(r.top + r.height/2)};
            }
            return {
                brand: box('.brand'),
                botCard: box('#botStatusCard'),
                autoSecureBtn: box('#autoSecureBtn'),
                preset1: box('.preset-chip'),
                chatInput: box('#chatInput'),
                sendBtn: box('#chatForm button[type="submit"]'),
                viewPromptBtn: box('#viewPromptBtn'),
                teamCred: box('.team-cred')
            };
        })()
        """
        await ws.send(json.dumps({'id': 1, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))
        while True:
            resp = json.loads(await ws.recv())
            if resp.get('id') == 1:
                print('Boxes:', json.dumps(resp['result']['result']['value'], indent=2))
                break

try:
    asyncio.run(check_boxes())
finally:
    proc.terminate()
