from parser import parse_logs
from detector import analyze_logs
from report import print_report
LINE = "=" * 40
SECTION = "-" * 40



logs = parse_logs("logs/auth.log")

failed_counts, success_counts, failed_attempts = analyze_logs(logs)

print_report(failed_counts, success_counts, failed_attempts)
