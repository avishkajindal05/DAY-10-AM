from collections import Counter, defaultdict

logs = [
"2026-03-08 10:10:01 - INFO - server - Server started",
"2026-03-08 10:10:05 - INFO - auth - User login successful",
"2026-03-08 10:10:15 - ERROR - database - Connection timeout",
"2026-03-08 10:10:20 - WARNING - server - High memory usage",
"2026-03-08 10:10:30 - ERROR - auth - Invalid login attempt",
"2026-03-08 10:11:00 - INFO - payments - Payment processed",
"2026-03-08 10:11:10 - ERROR - database - Connection timeout",
"2026-03-08 10:11:15 - CRITICAL - server - Server crash detected",
"2026-03-08 10:11:30 - WARNING - auth - Multiple login attempts",
"2026-03-08 10:12:00 - INFO - server - Health check OK",
"2026-03-08 10:12:10 - ERROR - payments - Payment gateway failure",
"2026-03-08 10:12:30 - INFO - database - Query executed"
]

def parse_log(line):

    parts = line.split(" - ")

    return {
        "timestamp": parts[0],
        "level": parts[1],
        "module": parts[2],
        "message": parts[3]
    }
    
def analyze_logs(parsed_logs):

    level_counter = Counter()
    module_counter = Counter()
    error_counter = Counter()

    errors_by_module = defaultdict(list)

    total_logs = len(parsed_logs)
    error_count = 0

    for log in parsed_logs:

        level = log.get("level")
        module = log.get("module")
        message = log.get("message")

        level_counter[level] += 1
        module_counter[module] += 1

        if level in ("ERROR", "CRITICAL"):
            error_count += 1
            error_counter[message] += 1
            errors_by_module[module].append(message)

    summary = {
        "total_entries": total_logs,
        "error_rate": round((error_count / total_logs) * 100, 2),
        "top_errors": error_counter.most_common(3),
        "busiest_module": module_counter.most_common(1)[0][0]
    }

    return {
        "level_distribution": dict(level_counter),
        "module_activity": dict(module_counter),
        "top_errors": error_counter.most_common(5),
        "errors_by_module": dict(errors_by_module),
        "summary": summary
    }
    


parsed_logs = [parse_log(log) for log in logs]

result = analyze_logs(parsed_logs)

for k, v in result.items():
    print(k, ":", v)