import pytest
import requests
import time

def pytest_addoption(parser):
    parser.addoption("--host", default="localhost")
    parser.addoption("--port", default="9000")

@pytest.fixture
def sonarqube_url(pytestconfig):
    """Build SonarQube URL."""
    host = pytestconfig.getoption("host")
    port = pytestconfig.getoption("port")
    return f"http://{host}:{port}"

@pytest.fixture
def wait_for_sonarqube(sonarqube_url):
    """Wait for SonarQube to be ready."""
    def is_ready():
        max_retries = 30
        retry_interval = 10
        
        for _ in range(max_retries):
            try:
                response = requests.get(f"{sonarqube_url}/api/system/status")
                if response.status_code == 200 and response.json()["status"] == "UP":
                    return True
            except requests.RequestException:
                pass
            time.sleep(retry_interval)
        return False
    
    return is_ready
