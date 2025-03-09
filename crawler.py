import requests
from bs4 import BeautifulSoup
from rich.console import Console

console = Console()

def crawl_website(url):
    console.print(f"[bold yellow]🕵️‍♂️ البحث عن روابط داخل {url}...[/bold yellow]")

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        links = {a["href"] for a in soup.find_all("a", href=True)}
        
        for link in links:
            console.print(f"[bold green]🔗 رابط مكتشف: {link}[/bold green]")
    
    except requests.RequestException as e:
        console.print(f"[bold red]❌ خطأ: {e}[/bold red]")
