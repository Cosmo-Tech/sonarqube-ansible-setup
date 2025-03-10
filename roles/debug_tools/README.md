# Debug Tools Role

This Ansible role installs common debugging tools to help with system troubleshooting and development.

## Installed Tools

- **htop**: Interactive process viewer
- **vim**: Improved vi editor
- **ripgrep**: Fast grep alternative
- **bat**: Cat clone with syntax highlighting

## Requirements

- Ansible 2.9 or higher
- Debian 12 (Bookworm) or Ubuntu 20.04+ (Focal/Jammy)

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
# Alternative package names for Debian-based systems
debug_tools_ripgrep_alt_package: "ripgrep"
debug_tools_bat_alt_package: "batcat"

# Create a symlink from batcat to bat for consistency
debug_tools_create_bat_symlink: true

# Additional debugging tools to install
# Example: ["strace", "lsof", "tcpdump"]
debug_tools_additional_packages: []
```

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: debug_tools
      debug_tools_additional_packages:
        - strace
        - lsof
        - tcpdump
```

## License

MIT

## Author Information

Created by Cosmo-Tech
