# Cosmo-Tech SonarQube Setup

This project contains Ansible playbooks and configuration files to set up and manage the SonarQube server with PostgreSQL for Cosmo-Tech.

## Project Structure

```
.
├── ansible.cfg           # Ansible configuration
├── group_vars/           # Variables shared across playbooks
│   └── all.yml           # Common variables for all hosts
├── hosts.ini             # Inventory file for production
├── inventories/          # Environment-specific inventories
│   └── dev/              # Development environment
│       ├── hosts         # Development hosts file
│       └── group_vars/   # Development variables
│           └── all.yml   # Development-specific variables
├── playbooks/            # Playbook directory
│   └── main.yml          # Main playbook that includes roles
├── roles/                # Roles directory
│   ├── postgresql/       # PostgreSQL role
│   │   ├── defaults/     # Default variables for PostgreSQL
│   │   │   └── main.yml
│   │   └── tasks/        # Tasks for PostgreSQL installation
│   │       └── main.yml
│   └── sonarqube/        # SonarQube role
│       ├── defaults/     # Default variables for SonarQube
│       │   └── main.yml
│       ├── tasks/        # Tasks for SonarQube installation
│       │   └── main.yml
│       └── templates/    # Templates for SonarQube
│           └── docker-compose.yml.j2  # Docker Compose template
└── Vagrantfile           # Vagrant configuration for local development
```

## Prerequisites

### For Production Deployment
- Target server with Ubuntu/Debian
- SSH access to the target server
- Sudo privileges on the target server

### For Local Development
- VirtualBox
- Vagrant
- Ansible
- Docker (for testing)
- Python 3.8 or later

## Setup

1. Create and activate a Python virtual environment:
```sh
uv venv
source .venv/bin/activate
```

2. Install project dependencies:
```sh
# Core dependencies
uv pip install .

# Testing dependencies
pip install -r requirements.txt
```

3. Install system dependencies (for local development):
```sh
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y virtualbox vagrant docker.io

# Enable Docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER  # Log out and back in after this
```

2. For production, set the required environment variable for the PostgreSQL password:
```sh
export SONARQUBE_DB_PASSWORD="your_secure_password"
```

## Usage

### Production Deployment

Run the Ansible playbook to install PostgreSQL and SonarQube on the production server:
```sh
ansible-playbook playbooks/main.yml
```

### Local Development with Vagrant

1. Start the Vagrant VM:
```sh
vagrant up
```

2. Run the Ansible playbook against the Vagrant VM:
```sh
ansible-playbook -i inventories/dev/hosts playbooks/main.yml
```

Alternatively, you can provision during VM creation:
```sh
ANSIBLE_PROVISION=true vagrant up
```

3. Access SonarQube in your browser at:
```
http://localhost:9000
```

4. To stop the VM:
```sh
vagrant halt
```

5. To remove the VM:
```sh
vagrant destroy
```

## Accessing SonarQube

After successful installation, SonarQube will be available at:
- Production: `http://<server-ip>:9000`
- Local development: `http://localhost:9000`

Default credentials:
- Username: admin
- Password: admin

## Customization

You can customize the installation by modifying the variables in:
- `group_vars/all.yml` - For global production variables
- `inventories/dev/group_vars/all.yml` - For development environment variables
- `roles/postgresql/defaults/main.yml` - For PostgreSQL-specific settings
- `roles/sonarqube/defaults/main.yml` - For SonarQube-specific settings

## Vagrant VM Specifications

The local development VM is configured with:
- Debian 12 (Bookworm)
- 4GB RAM
- 2 CPU cores
- Port forwarding: 9000 (SonarQube) and 5432 (PostgreSQL)
- Private IP: 192.168.56.10

## Testing

This project includes comprehensive testing mechanisms to ensure proper functionality. You can run all tests using the provided helper script or execute specific tests individually.

### Running All Tests

Use the helper script to run all tests in sequence:

```sh
# For Vagrant environment
VAGRANT_TEST=true ./tests/run_tests.sh

# For production environment
SONARQUBE_HOST=<your-server-ip> ./tests/run_tests.sh
```

This will run:
1. Syntax and linting checks
2. Molecule tests for PostgreSQL role
3. Molecule tests for SonarQube role
4. Integration tests

### Running Individual Tests

#### Syntax and Linting Tests

```sh
# Run syntax checks and linting
ansible-playbook tests/syntax_check.yml

# Run only ansible-lint
ansible-lint
```

#### Integration Tests

After deployment, verify the SonarQube installation:
```sh
# For production
./tests/integration_test.sh <server-ip> 9000

# For local Vagrant VM
./tests/integration_test.sh localhost 9000
```

#### Molecule Tests

Test individual roles in isolation:
```sh
# Test PostgreSQL role
cd roles/postgresql
molecule test

# Test SonarQube role
cd roles/sonarqube
molecule test
```

#### Idempotency Testing

Verify that running the playbook multiple times doesn't cause changes:
```sh
# First run
ansible-playbook -i inventories/dev/hosts playbooks/main.yml

# Second run (should report no changes)
ansible-playbook -i inventories/dev/hosts playbooks/main.yml
```

### Test Configuration

- `.ansible-lint` - Ansible linting rules and exclusions
- `molecule/*/molecule.yml` - Molecule test environment configuration
- `tests/syntax_check.yml` - Syntax and linting test definitions
- `tests/integration_test.sh` - Integration test script

### Prerequisites for Testing

1. Install test dependencies:
```sh
pip install molecule molecule-plugins[vagrant] yamllint ansible-lint
```

2. Ensure VirtualBox and Vagrant are installed for Molecule tests:
```sh
# Ubuntu/Debian
sudo apt-get install virtualbox vagrant
```
