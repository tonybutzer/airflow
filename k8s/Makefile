
cat:
	cat Makefile

# (cd /etc/yum.repos.d && wget https://people.canonical.com/~mvo/snapd/amazon-linux2/snapd-amzn2.repo)
ik8s:
	sudo yum install snapd
	sudo systemctl enable --now snapd.socket
	sudo ln -s /var/lib/snapd/snap /snap
	sleep 5
	sudo snap install microk8s --classic


list:
	yum list snapd\*


enable:
	microk8s enable dns dashboard storage
	
stat:
	microk8s.status 


token:
	microk8s kubectl create token default
