Analyze the Nginx access log file located at `/app/access.log`.

Calculate the following metrics from the log file:
1. `total_requests`: The total number of HTTP request lines in the log.
2. `unique_ips`: The total count of distinct client IP addresses.
3. `top_path`: The most frequently requested endpoint path.

Write the summary result as a JSON object to `/app/report.json` using exact key names:

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```
