def print_report(failed_counts, success_counts, failed_attempts):
    LINE = "=" * 40
    SECTION = "-" * 40

    print(SECTION)
    print("\nSECURITY LOG ANALYSIS\n")
    print(SECTION)
    
    print(f"\nTotal Failed Login Attempts: {failed_counts}")
    print(f"Total Successful Login Attempts: {success_counts}\n")

    print(LINE)

    print("\nFailed Login Attempts by IP Address:\n")
    for ip, count in failed_attempts.items():
        print(f"IP Address: {ip} - Failed Attempts: {count}")
    
    print(LINE)

    print("\nSuspicious IP Addresses:")
    for ip, count in failed_attempts.items():
        if count > 3:
            print(f"IP Address: {ip} - Failed Attempts: {count}\n")

    print(LINE)

    print("\nPossible Threats/ Brute Force Attempts:")
    for ip, count in failed_attempts.items():
        if count >= 5:
            print(f"IP Address: {ip} - Failed Attempts: {count}\n")
    
    print(LINE)