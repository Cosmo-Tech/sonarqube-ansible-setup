# Cosmo-Tech SonarQube Setup

This project contains Ansible playbooks to set up and manage SonarQube with PostgreSQL for Cosmo-Tech.

## Prerequisites

- **For Production**: Ubuntu/Debian server with SSH access and sudo privileges
- **For Development**: VirtualBox, Vagrant, Ansible, Python 3.8+


## Usage

### Production Deployment

```sh
# Run the playbook for production
ansible-playbook -i inventory.yml -l production playbooks/main.yml

# With specific password
read -s SONARQUBE_DB_PASSWORD
export SONARQUBE_DB_PASSWORD
ansible-playbook -i inventory.yml -l production playbooks/main.yml
```

### Development with Vagrant

```sh
# Start VM and run playbook
vagrant up
ansible-playbook -i inventory.yml -l local playbooks/main.yml

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

## Environment Usage

The project supports three environments defined in a single `inventory.yml` file:

### Local Development (Vagrant)
```bash
ansible-playbook -i inventory.yml -l local playbooks/main.yml
```

### Pre-production
```bash
ansible-playbook -i inventory.yml -l preprod playbooks/main.yml
```

### Production
```bash
ansible-playbook -i inventory.yml -l production playbooks/main.yml
```

### Inventory Structure

The inventory is organized using Ansible groups:
- `local`: Development environment using Vagrant VM
- `preprod`: Pre-production environment
- `production`: Production environment
- `sonarqube`: Parent group containing all environments

Common SSH and Python settings are defined at the root level, making configuration maintenance simpler and reducing duplication.
