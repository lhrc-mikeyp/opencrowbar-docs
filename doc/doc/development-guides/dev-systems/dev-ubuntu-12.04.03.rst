Configuration Guide - Ubuntu 12.04.03
=====================================

-  Start the Ubuntu server install and answer the prompts
-  English & Ubuntu Server

   -  Choose eth0 as your primary interface

-  Name your machine and user accounts (we recommend "crowbar" as user)
   & time zone
-  Partitioning: guided to use entire disk and LVM

   -  defaults are OK
   -  you need to select YES to continue (NO = return to selection)

-  Proxy depends on your environment (we'll install Squid later)

   #. No automatic updates

-  Install OpenSSH & Samba (space toggles, enter continues)
-  Install GRUB boot loader
-  When Installation completes, make sure the ISO is not attached and
   allow reboot
-  you may want to snapshot the machine in this state

-  | Add Network for SSH from Host
   | ``sudo vi /etc/network/interfaces`` and add the following lines

::

    auto eth1
    iface eth1 inet static
      address 192.168.222.6
      netmask 255.255.255.0

| then restart networking:
| ``sudo service networking restart``

-  validate network access to this net network by using Putty (or other
   ssh client) to SSH into crowbar@192.168.222.6

#. Setup an .ssh keypair
#. use ``ssh-keygen -t rsa``

   #. if that fails, try ``rssh-keygen``

#. Passwordless sudo:
   ``sudo sed -ie "s/%sudo\tALL=(ALL:ALL) ALL/%sudo ALL=(ALL) NOPASSWD: ALL/g" /etc/sudoers``

   #. additional information, see
      http://serverfault.com/questions/160581/how-to-setup-passwordless-sudo-on-linux

#. Optional, `SAMBA and CNTLM <samba_cntlm.md>`__ if you are developing
   on Windows using VMs and/or behind corporate firewalls
#. Setup a `Squid Proxy <proxy-cache.md>`__ to ensure downloads are fast
   (needed by Crowbar too)
#. Make sure your environment does not use proxy for local addresses:

   #. ``export no_proxy="127.0.0.1,[::1],localhost,192.168.124.0/24,172.16.0.0/12"``
   #. tip: add this to your login init

#. you need git and tmux: ``sudo apt-get install git tmux``

Position Boot Assets
~~~~~~~~~~~~~~~~~~~~

    We'll need this for later but it takes a while so we do it now in
    different window....

Copy the ISOs that you want for nodes to
``$HOME/.cache/opencrowbar/tftpboot/isos``. It's OK to have more than 1
but make sure you have the space!

Examples:

#. ``mkdir -p $HOME/.cache/opencrowbar/tftpboot/isos``
#. ``cd $HOME/.cache/opencrowbar/tftpboot/isos``
#. Centos:
   ``wget http://centos.mirror.ndchost.com/6.5/isos/x86_64/CentOS-6.5-x86_64-bin-DVD1.iso``
#. Ubuntu:
   ``wget http://releases.ubuntu.com/12.04.4/ubuntu-12.04.4-server-amd64.iso``

Checkout Code
~~~~~~~~~~~~~

#. get git

   #. ubuntu: ``sudo apt-get install git``

#. get the code: ``git clone https://github.com/opencrowbar/core``
#. if you want to contribute

   #. review `Contribute Guidelines <../contributing-code.md>`__
   #. setup your `personal git fork <../contributing.md>`__

#. Advanced user optional `build Sledgehammer <build_sledgehammer.md>`__


