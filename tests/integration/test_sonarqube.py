"""Integration tests for SonarQube deployment."""
import pytest
import requests
from urllib.parse import urljoin

def test_sonarqube_running(wait_for_sonarqube):
    """Verify SonarQube is operational."""
    assert wait_for_sonarqube(), "SonarQube failed to start and become ready"

def test_basic_health(sonarqube_url):
    """Verify basic health check."""
    url = urljoin(sonarqube_url, "api/system/health")
    response = requests.get(url)
    assert response.status_code == 200, "Health check endpoint not accessible"
    data = response.json()
    assert data["health"] == "GREEN", f"SonarQube health is not GREEN: {data['health']}"

def test_database_connection(sonarqube_url):
    """Verify database connection is working."""
    url = urljoin(sonarqube_url, "api/system/info")
    response = requests.get(url)
    assert response.status_code == 200, "System info endpoint not accessible"
    info = response.json()
    assert "Database" in info, "Database information not found in system info"
    assert info["Database"]["Status"] == "UP", "Database not connected"

def test_authentication(sonarqube_url):
    """Verify authentication with default credentials."""
    url = urljoin(sonarqube_url, "api/authentication/validate")
    response = requests.get(url, auth=("admin", "admin"))
    assert response.status_code == 200, "Authentication endpoint not accessible"
    assert response.json()["valid"], "Default admin credentials not working"
