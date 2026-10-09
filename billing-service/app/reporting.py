"""Sends the nightly billing summary to the reporting service."""

import os

import httpx

REPORTING_URL = "https://reports.example.invalid/v1/summary"


def send_summary(summary: str) -> int:
    headers = {
        "X-Client": "billing-service",
        "Authorization": os.path.expandvars("Bearer ${REPORTING_TOKEN}"),
    }
    resp = httpx.post(REPORTING_URL, json={"summary": summary[:2000]}, headers=headers, timeout=10)
    return resp.status_code


def send_status(status: str) -> int:
    # A named setting sent to its own service: fine, not flagged.
    headers = {"Authorization": "Bearer " + os.environ["STATUS_TOKEN"]}
    return httpx.post("https://status.example.invalid/v1", json={"status": status}, headers=headers, timeout=10).status_code
