# ansiblePlays
Repo for Ansible Playbooks

## satRegistration.yml
This playbook will take a managed host that has not been registered before and register it to Red Hat Satellite 6.5.

It requires some variables to be filled in and expects the **katello-ca-cert** and **puppet.conf** files to be put on a share somewhere that it can grab.  Playbook can be modified easily to deploy these files if they are local as well.

satRegistration.yml playbook also needs a ansible-vault encrypt_string value as a variable.

*ToDo: Add logic to unregister and clean in case managed host has been registered before and remove old katello-ca cert.