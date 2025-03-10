# Testing Documentation

This directory contains the test suite for the SonarQube deployment project. The testing approach focuses on essential functionality to ensure core features are working correctly.

## Test Structure

- `conftest.py`: Common test fixtures and configurations
- `integration/`: Integration tests for SonarQube deployment
- `run_tests.py`: Main test runner script
- `syntax_check.yml`: Ansible syntax checking playbook

## Core Test Cases

1. **Basic Installation Tests**
   - SonarQube is running and accessible
   - Health check returns GREEN status
   - Database connection is working
   - Default authentication is functional

## Running Tests

### Using the Test Runner

The `run_tests.py` script provides a simple way to execute all tests:

```bash
# For Vagrant development environment
./tests/run_tests.py --vagrant

# For production environment
./tests/run_tests.py --host <server-ip>
```

### Manual Test Execution

You can also run individual test components:

```bash
# Lint checks
ansible-lint

# Syntax check
ansible-playbook tests/syntax_check.yml

# Integration tests only
pytest -v tests/integration/
```

## Test Dependencies

Required Python packages:
- pytest>=7.0.0
- requests>=2.28.0

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Test Configuration

The test suite can be configured through command-line options:

- `--host`: Target host for testing (default: localhost)
- `--port`: SonarQube port (default: 9000)
- `--vagrant`: Run against Vagrant development environment

## Interpreting Results

The test runner will provide clear pass/fail indicators:
- ✓ (Pass): Test completed successfully
- ✗ (Fail): Test failed with errors

Full test output will be displayed for any failures to aid in troubleshooting.
