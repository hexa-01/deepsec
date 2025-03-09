import os
import subprocess
import signal
from rich.console import Console
from bandit.core import config, manager

console = Console()

def analyze_code(file_path):
    if not os.path.exists(file_path):
        console.print(f"[bold red]🚨 الملف {file_path} غير موجود![/bold red]")
        return

    console.print(f"[bold cyan]🔍 فحص الثغرات في: {file_path}[/bold cyan]")

    if file_path.endswith(".py"):
        conf = config.BanditConfig()
        b_mgr = manager.BanditManager(conf, "file")
        b_mgr.discover_files([file_path])
        b_mgr.run_tests()

        for issue in b_mgr.get_issue_list():
            console.print(f"[bold red]🚨 {issue.text} (في السطر {issue.lineno})[/bold red]")

    elif file_path.endswith((".php", ".js", ".c", ".cpp", ".rs")):
        result = subprocess.run(["semgrep", "--config=auto", file_path], capture_output=True, text=True)
        console.print(result.stdout)
    else:
        console.print("[bold red]🚨 نوع الملف غير مدعوم![/bold red]")

def analyze_project(directory):
    if not os.path.exists(directory):
        console.print(f"[bold red]🚨 المجلد {directory} غير موجود![/bold red]")
        return

    console.print(f"[bold cyan]📂 جاري تحليل المشروع: {directory}[/bold cyan]")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".py", ".php", ".js", ".c", ".cpp", ".rs")):
                analyze_code(os.path.join(root, file))

def dynamic_analysis(file_path):
    console.print(f"[bold cyan]🕵️ تشغيل الكود في بيئة معزولة: {file_path}[/bold cyan]")

    try:
        process = subprocess.Popen(
            ["python3", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid
        )
        
        stdout, stderr = process.communicate(timeout=5)

        console.print(f"[bold green]📤 خرج البرنامج:[/bold green] {stdout.decode()}")
        if stderr:
            console.print(f"[bold red]🚨 أخطاء محتملة:[/bold red] {stderr.decode()}")

    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        console.print("[bold red]⏳ التحليل توقف بسبب تجاوز المهلة! قد يكون هناك حلقة لا نهائية.[/bold red]")

    except Exception as e:
        console.print(f"[bold red]⚠️ خطأ أثناء التحليل: {e}[/bold red]")

def check_dependencies():
    console.print("[bold cyan]🔎 فحص مكتبات المشروع بحثًا عن ثغرات...[/bold cyan]")
    
    safety_result = subprocess.run(["safety", "check"], capture_output=True, text=True)
    console.print(safety_result.stdout)

    snyk_result = subprocess.run(["snyk", "test"], capture_output=True, text=True)
    console.print(snyk_result.stdout)
