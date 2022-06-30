# Lidar USGS South Dakota Data in the Cloud

## Current Action

1. Establish via terraform a butzer-eccoe-admin-box t2.small
	- mkdir tfinfra
	- cp joshua.picotte tf stuff here
	- install docker for tf
	- miniconda ?


## Actions

- get at least two small ec2 instances created and launched/started up in eccoe account
- create a bucket named eccoe-lidar
- move some of sodak into the bucket
- get conda python working as simple as possible
- load docker and test hello world
- demonstrate infracstucture as code with simple terrform scripts
- train Ajit and the Mann Brothers on the 10% of the cloud that get used
- set them free



## ssh


### Keys

- find any *.pem files those are ssh key pair files
- *.ppk files also are key pair files
- if you use putty as your agent - know how to use puttygen and pageant to manage keys
	- this will be used for winscp and fileZilla

- just learned today that puttygen will read id_rsa keys made with ssh-keygen - and you can import those in pageant as well


### Linux like clients

- cygwin
- git bash
- cmder
- cmd
- powershell

> all the above can launch an ssh session to another computer

- tallgrass and the cloud can talk to each other via ssh and rclone - but you have to set up key pairs between them

- git can use ssh keys as well
	- git can also use tokens - bothe methods have their respective adavantages/disadvantages

- authentication is almost always painful and can consume brain attention units

### VDI

- you can use the shared h drive to store your key pair and consolidate keys between your laptop and your vdi
	- this would prevent key sprawl - you just have to have a plan for your keypairs - or you will get to ssh key hell

