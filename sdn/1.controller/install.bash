#!/bin/bash

sudo apt-get update

sudo apt-get --yes install python-software-properties

sudo apt-get --yes install ubuntu-cloud-keyring

echo | sudo add-apt-repository cloud-archive:juno

sudo apt-get update

sudo apt-get --yes install keystone

touch /tmp/override.txt

sudo dpkg --unpack hp-sdn-ctl_2.7.18.0503_amd64.deb

sudo apt-get --yes install -f

sudo dpkg -l hp-sdn-ctl

OUTPUT="$(sudo service sdnc status)"

sudo /opt/sdn/admin/config_local_keystone

echo "${OUTPUT}" | grep "running"

if [[ "${OUTPUT}" =~ .*"running".* ]];then
        echo "Installation success"
else
        echo "Installation failed"
fi
