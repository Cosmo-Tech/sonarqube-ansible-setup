# Cosmo-Tech SonarQube Setup

This project contains Ansible playbooks to set up and manage SonarQube with PostgreSQL for Cosmo-Tech.

## Prerequisites

- **For Production**: Ubuntu/Debian server with SSH access and sudo privileges
- **For Development**: VirtualBox, Vagrant, Ansible, Python 3.8+

## Quick Setup

```sh
# 1. Set up Python environment
uv venv && source .venv/bin/activate
uv pip install .
```

## Usage

### Production Deployment

```sh
# Run the playbook
ansible-playbook playbooks/main.yml

# With specific password (optional) otherwise we generate one
SONARQUBE_DB_PASSWORD="your_secure_password" ansible-playbook playbooks/main.yml
```

### Development with Vagrant

```sh
# Start VM and run playbook
vagrant up
ansible-playbook -i inventories/dev/hosts playbooks/main.yml

# Or provision during VM creation
ANSIBLE_PROVISION=true vagrant up

# Access SonarQube at http://localhost:9000
# Default credentials: admin/admin

# Stop or remove VM
vagrant halt
vagrant destroy
```


## Testing

```sh
ansible-lint
```

For more details on testing, see the test scripts in the `tests/` directory.
