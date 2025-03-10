# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"  # Debian 12
  config.vm.hostname = "sonarqube-dev"
  
  # Forward SonarQube port
  config.vm.network "forwarded_port", guest: 9000, host: 9000
  
  # Forward PostgreSQL port for external access if needed
  config.vm.network "forwarded_port", guest: 5432, host: 5432
  
  # Private network for Ansible
  config.vm.network "private_network", ip: "192.168.56.10"
  
  # VM Resources
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"  # SonarQube needs at least 4GB
    vb.cpus = 2
    vb.name = "sonarqube-dev"
  end
  
  # Bootstrap script to prepare the VM for Ansible
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3 python3-pip psycopg2
    echo "VM is ready for Ansible provisioning"
  SHELL

end
