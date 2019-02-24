# Software Installation

This script is used to upgrade or downgrade devices in the Americas POC lab with the desired software packages. It prompts the user for the version and retrieves the specified version from the FTP server. If the jtac recommended version is specified, the script gets the version name from Juniper website before retrieveing the software package from the FTP server.

## Requirements

Ansible: `pip install ansible`  Version: 2.4.0.0 or higher

Jxmlease: `pip install jxmlease`

Ansible Galaxy: `sudo apt install ansible`

Juniper junos module: `ansible-galaxy install Juniper.junos`

Junos-eznc: `pip install junos-eznc`

Beautifulsoup: `apt-get install python-bs4`  (for Python 2)

Requests: `pip install requests`

## Usage

To clone the repository

`git clone https://git.juniper.net/americas-poc/junos-upgrade.git`

To run the software installation script

```
cd junos_upgrade
ansible-playbook  software_upgrade.yml -i inventory --limit=host1,host2,...
```
For example:

ansible-playbook  software_upgrade.yml -i inventory --limit=poc-qfx5110-17,poc-ex4300-13

NB: If the models are different, the script retrieves the JTAC version of the individual models and performs the upgrade. If you specify the version, the version name must exist for both models on the FTP server for the code to work properly.  


To perform a storage cleanup

```
cd junos_upgrade
ansible-playbook  storage_cleanup.yml -i inventory --limit=host1,host2,...
```

For example:

ansible-playbook  storage_cleanup.yml  -i inventory --limit=poc-qfx5110-17,poc-ex4300-13


## Assumptions

 1. The software package is available on the FTP server.
 2. The device has minimum configuration including the management IP, default route and name-server. For best results, the **default_config.py** script should be run on the device before performing the upgrade.
 3. The device has the correct hostname and IP information on the DNS **inf-poc-infoblox.amerpoc.jnpr.net**.
 4. The devices belong to the domain `amerpoc.jnpr.net` which is defined as default in the script.
 5. The script uses the hostnames on the DNS. If no hostname is available, insert the IP address into the **inventory** file under the right model and remove the **.amerpoc.jnpr.net** in the **software_upgrade** file.
