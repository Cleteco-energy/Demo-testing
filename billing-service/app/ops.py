"""Ops helpers for support staff: run a diagnostic command on the billing host."""

import subprocess


def run_diagnostic(command: str) -> str:
    """Runs a diagnostic command and returns its output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
    return result.stdout


def clear_cache(key: str) -> str:
    """Drops one cached invoice by key."""
    return subprocess.run(f"redis-cli DEL {key}", shell=True, capture_output=True, text=True, timeout=10).stdout
