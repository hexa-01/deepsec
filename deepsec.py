import argparse
from rich.console import Console
from rich.panel import Panel
from scanner.crawler import crawl_website
from scanner.requests_handler import scan_website

console = Console()

def show_banner():
    banner = """
██████╗ ███████╗███████╗███████╗███████╗ ██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔═══██╗
██████╔╝█████╗  █████╗  █████╗  █████╗  ██║   ██║
██╔═══╝ ██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  ██║   ██║
██║     ██║     ██║     ██║     ███████╗╚██████╔╝
╚═╝     ╚═╝     ╚═╝     ╚═╝     ╚══════╝ ╚═════╝ 
"""
    console.print(Panel(banner, title="[bold cyan]DeepSec Web[/bold cyan]", style="bold magenta"))

def main():
    show_banner()

    parser = argparse.ArgumentParser(description="DeepSec Web - تحليل الثغرات الأمنية")
    parser.add_argument("--url", required=True, help="رابط الموقع المستهدف")
    parser.add_argument("--crawl", help="اكتشاف الروابط المخفية", action="store_true")
    parser.add_argument("--scan", help="فحص الثغرات الأمنية", action="store_true")

    args = parser.parse_args()

    console.print(f"[bold cyan]🔍 فحص {args.url} ...[/bold cyan]")

    if args.crawl:
        crawl_website(args.url)

    if args.scan:
        scan_website(args.url)

if __name__ == "__main__":
    main()
