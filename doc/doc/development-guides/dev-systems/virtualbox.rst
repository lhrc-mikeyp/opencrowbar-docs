VirtualBox Development System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set up a VirtualBox environment for Crowbar Development, follow these
given instructions.

VirtualBox

#. File...Preferences...Network
#. you want at least two Host-Only Ethernet Adapters

-  1 should be IP 192.168.222.1 & DHCP should be off
   =================================================

-  2 should be IP 192.168.124.1 & DHCP should be off
   =================================================

-  Create new Linux Ubuntu 64 bit Virtual Machine

#. RAM: 4096

-  Disk: VDI, Dynamically Allocated, at least 40 GB (80 recommended)
-  Before Booting, go into settings

#. System...Processor: give your self at least 2 cores

-  Storage IDE Controller; choose CD Ubuntu-12.04.4-server-amd64.iso

   -  you have to download the ISO but you'll need it later

-  Network:

   -  Adapter 1 (default OK) - NAT
   -  Adapter 2 - Host Only #1 (has no number)
   -  Adapter 3 - Host Only #2

Now, go `back <README.md>`__ and find specifics for the O/S you're
using.
