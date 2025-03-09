import argparse
from rich.console import Console
from analyzer import analyze_code, analyze_project, dynamic_analysis, check_dependencies
from network_scanner import scan_protocols, scan_with_ml

console = Console()

def main():
    parser = argparse.ArgumentParser(description="DeepSec - أقوى أداة تحليل أمني")
    parser.add_argument("--analyze", help="تحليل ملف كود واكتشاف الثغرات")
    parser.add_argument("--check-project", help="تحليل مشروع كامل")
    parser.add_argument("--scan-protocol", help="تحليل الشبكة وكشف الهجمات")
    parser.add_argument("--scan-ml", help="تحليل الشبكة باستخدام الذكاء الاصطناعي")
    parser.add_argument("--dynamic", help="تحليل سلوك الكود أثناء تشغيله")
    parser.add_argument("--check-deps", help="فحص ثغرات المكتبات الخارجية")

    args = parser.parse_args()

    if args.analyze:
        analyze_code(args.analyze)
    elif args.check_project:
        analyze_project(args.check_project)
    elif args.scan_protocol:
        scan_protocols(args.scan_protocol)
    elif args.scan_ml:
        scan_with_ml(args.scan_ml)
    elif args.dynamic:
        dynamic_analysis(args.dynamic)
    elif args.check_deps:
        check_dependencies()
    else:
        console.print("[bold red]🚨 لم يتم إدخال أمر صحيح! استخدم --help لعرض الخيارات.[/bold red]")

if __name__ == "__main__":
    main()
