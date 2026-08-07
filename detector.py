def analyze_logs(logs):
    failed_counts = 0
    success_counts = 0
    failed_attempts = {}

    for log in logs:
        status = log["status"]
        ip = log["ip"]
        
        if status == 'FAILED':
            failed_counts += 1
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1
        
        if status == 'SUCCESS':
            success_counts += 1
    
    return failed_counts, success_counts, failed_attempts
            