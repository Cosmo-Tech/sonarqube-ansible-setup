# Cosmo-Tech SonarQube Setup

This project contains Ansible playbooks to set up and manage SonarQube with PostgreSQL for Cosmo-Tech.

## Prerequisites

- **For Production**: Ubuntu/Debian server with SSH access and sudo privileges
- **For Development**: VirtualBox, Vagrant, Ansible, Python 3.8+


## Usage

### Production Deployment

```sh
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

The project supports three environments defined in `inventory.yml`:

### Local Development (Vagrant)
```bash
ansible-playbook -i inventory.yml -l local playbooks/main.yml
```

### Pre-production
```bash
ansible-playbook -e "ansible_port=PORT_NUMBER" -i inventory.yml -l preprod playbooks/main.yml
```

### Production
```bash
ansible-playbook -i inventory.yml -l production playbooks/main.yml
```
