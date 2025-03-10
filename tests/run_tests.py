#!/usr/bin/env python3
"""
Simplified test runner for SonarQube deployment.
"""

import subprocess
import sys
import os
import argparse
import importlib.util

def run_test(cmd, name):
    """Run a test command and print its status."""
    print(f"\n=== Running {name} ===")
    result = subprocess.run(cmd, shell=True, env=os.environ)
    success = result.returncode == 0
    status = "✓ Passed" if success else "✗ Failed"
    print(f"{status}: {name}")
    return success

def main():
    parser = argparse.ArgumentParser(description="Run SonarQube deployment tests")
    parser.add_argument("--vagrant", action="store_true", help="Run tests against Vagrant VM")
    parser.add_argument("--host", default=None, help="Host to run tests against")
    parser.add_argument("--skip-integration", action="store_true", help="Skip integration tests")
    args = parser.parse_args()

    # Set up environment
    if args.vagrant:
        host = "localhost"
        os.environ["ANSIBLE_CONFIG"] = "inventories/dev/ansible.cfg"
    elif args.host:
        host = args.host
    else:
        print("Error: Either --vagrant or --host must be specified")
        sys.exit(1)

    # Define test sequence
    tests = [
        ("ansible-playbook tests/syntax_check.yml", "Syntax and Linting Check"),
    ]
    
    # Add integration tests if not skipped
    if not args.skip_integration:
        tests.append((f"python -m pytest -v tests/integration/ --host={host}", "Integration Tests"))
    
    # Run tests
    failed = False
    for cmd, name in tests:
        if not run_test(cmd, name):
            failed = True
            break

    # Print summary
    print("\n=== Test Summary ===")
    if failed:
        print("❌ Some tests failed")
        sys.exit(1)
    else:
        print("✅ All tests passed")
        sys.exit(0)

if __name__ == "__main__":
    main()
