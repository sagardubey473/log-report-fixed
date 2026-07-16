An Apache-style access log is located at `/app/access.log`. Each line follows the
common log format, for example:

```
192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
```

Analyze the log and write a JSON report to `/app/report.json`. The report must be
a single JSON object with exactly these three keys:

- `total_requests` (integer): the total number of request lines in the log
  (ignore empty lines).
- `unique_ips` (integer): the number of distinct client IP addresses (the first
  field of each line).
- `top_path` (string): the request path that appears most often in the log
  (e.g. `/index.html`).

Success criteria:

1. `/app/report.json` exists and parses as a JSON object with exactly the keys
   `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` equals the number of non-empty lines in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IPs in `/app/access.log`.
4. `top_path` is the most frequently requested path in `/app/access.log`.
