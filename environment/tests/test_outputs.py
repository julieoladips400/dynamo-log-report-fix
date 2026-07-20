import json
import os
import pytest

def test_report_json_exists():
    """Verifies that /app/report.json was created."""
    assert os.path.exists("/app/report.json"), "report.json does not exist"

def test_total_requests_key():
    """Verifies that report.json contains the 'total_requests' key with expected value."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)
    assert "total_requests" in data, "Missing total_requests key"
    assert data["total_requests"] == 6

def test_unique_ips_key():
    """Verifies that report.json contains the 'unique_ips' key with expected value."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)
    assert "unique_ips" in data, "Missing unique_ips key"
    assert data["unique_ips"] == 3

def test_top_path_key():
    """Verifies that report.json contains the 'top_path' key with expected value."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)
    assert "top_path" in data, "Missing top_path key"
    assert data["top_path"] == "/index.html"
