import requests
import random
import time
from rich.console import Console
from ai.ai_analysis import analyze_response

console = Console()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
]

HEADERS = {
    "User-Agent": random.choice(USER_AGENTS),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Connection": "close"
}

def scan_website(url):
    console.print(f"[bold yellow]🚀 بدء فحص {url}...[/bold yellow]")

    payloads = ["' OR 1=1 --", "<script>alert('XSS')</script>", "../../etc/passwd"]
    
    for payload in payloads:
        test_url = f"{url}{payload}"
        try:
            response = requests.get(test_url, headers=HEADERS, timeout=7)
            analysis_result = analyze_response(response.text)
            
            if "high risk" in analysis_result:
                console.print(f"[bold red]🚨 خطر كبير: {test_url}[/bold red]")
            else:
                console.print(f"[bold green]✅ آمن: {test_url}[/bold green]")

        except requests.RequestException as e:
            console.print(f"[bold yellow]⚠️ خطأ: {e}[/bold yellow]")

        time.sleep(random.uniform(0.5, 2))  # تجنب الحظر
