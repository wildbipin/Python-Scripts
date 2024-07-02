import re
from collections import defaultdict

def parse_log(file_path):
    log_data = defaultdict(list)
    log_pattern = re.compile(
        r'(?P<ip>[\d.]+) - - \[(?P<date>[\w:/]+)\s[+\-]\d{4}\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\d+|-) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
    )
    
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                log_data['ip'].append(match.group('ip'))
                log_data['date'].append(match.group('date'))
                log_data['request'].append(match.group('request'))
                log_data['status'].append(match.group('status'))
                log_data['size'].append(match.group('size'))
                log_data['referrer'].append(match.group('referrer'))
                log_data['user_agent'].append(match.group('user_agent'))
    return log_data

def generate_report(log_data):
    print(f"Total requests: {len(log_data['ip'])}")
    status_counts = defaultdict(int)
    for status in log_data['status']:
        status_counts[status] += 1
    
    print("HTTP Status Codes:")
    for status, count in status_counts.items():
        print(f"  {status}: {count}")
    
    unique_ips = set(log_data['ip'])
    print(f"Unique IP addresses: {len(unique_ips)}")

    # More detailed analysis can be added here

if __name__ == "__main__":
    log_file_path = 'access.log'  # Replace with your log file path
    log_data = parse_log(log_file_path)
    generate_report(log_data)