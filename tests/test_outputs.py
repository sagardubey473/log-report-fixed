import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Expected values are derived from the access.log shipped in environment/:
# 6 non-empty request lines, 3 distinct client IPs
# (192.168.0.1, 192.168.0.2, 10.0.0.5), and /index.html requested 3 times.
EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def _load():
    return json.loads(REPORT.read_text())


def test_report_is_json_object_with_exact_keys():
    """Criterion 1: /app/report.json exists and parses as a JSON object with
    exactly the keys total_requests, unique_ips, and top_path."""
    assert REPORT.exists(), "no report.json found"
    report = _load()
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report.keys()) == set(EXPECTED.keys()), (
        f"report.json keys {sorted(report.keys())} != "
        f"expected {sorted(EXPECTED.keys())}"
    )


def test_total_requests():
    """Criterion 2: total_requests equals the number of non-empty lines in
    /app/access.log (6)."""
    assert _load()["total_requests"] == EXPECTED["total_requests"]


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs in
    /app/access.log (3)."""
    assert _load()["unique_ips"] == EXPECTED["unique_ips"]


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path in
    /app/access.log (/index.html)."""
    assert _load()["top_path"] == EXPECTED["top_path"]
