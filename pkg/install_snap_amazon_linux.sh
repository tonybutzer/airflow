#! /bin/bash

sudo yum install git

sudo bash -c 'cd /etc/yum.repos.d && wget https://people.canonical.com/~mvo/snapd/amazon-linux2/snapd-amzn2.repo'

sudo yum install snapd

