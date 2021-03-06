Setting Up the Virtual Machine (VM) on a Fedora host O/S
--------------------------------------------------------

#. | Create a new virtual network 192.168.124.0/24 (using virt-manager
   or virsh).
   |  Do not use DHCP for this network.

#. Start with a fresh Fedora 19 VM (this can be a minimal install).

#. | Assign the previously created virtual network to the VM and
   configure the
   |  VM's networking like this:

| IP address: 192.168.124.10
|  Netmask: 255.255.255.0
|  Gateway: 192.168.124.1
|  DNS: 192.168.124.1

| (You will need to edit ``/etc/sysconfig/network-scripts/ifcfg-eth0``
and
|  ``/etc/resolv.conf`` to achieve this on a VM that was configured
differently
|  during installation.)

#. Connect to the machine via SSH and try to ping some address to verify
   that
    traffic gets routed correctly and DNS works.

kvm-host> ssh root@192.168.124.10\ 

#. [Optional] If you have problems with outbound connections from VM
   even after
    editing network-scripts and resolv.conf, it might be that iptables
    forwarding rules for the virtual network didn't get created on your
   host
    machine. Check that with iptables:

kvm-host> sudo iptables -L

| Chain FORWARD
|  target prot opt source destination
|  ACCEPT all -- anywhere 192.168.124.0/24 state RELATED,ESTABLISHED
|  ACCEPT all -- 192.168.124.0/24 anywhere

(The output is shortened to show the important part only.)

| If you don't see the above forwarding rules, shut down your VMs and
restart
|  libvirtd:

kvm-host> systemctl restart libvirtd.service

Then check the iptables output again and the forwarding rules should be
there.

#. Create a user on the VM for Crowbar development.

| root@crowbar-dev> useradd -m crowbar
|  root@crowbar-dev> passwd crowbar
