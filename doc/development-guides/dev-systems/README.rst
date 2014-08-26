Dev System Configuration
========================

Installation and Configuration Overview - What you'll be doing:
---------------------------------------------------------------

#. Install the base OS
#. Configure base OS for running Crowbar
#. git clone https://github.com/opencrowbar/core
#. Start crowbar in a Docker container
#. Deploy slave nodes and Hack away!

Prereqs
-------

You'll need (or end up with after following these docs):

-  A Linux development environment (running on bare metal or VirtualBox)
-  Internet Access
-  Your own user (NOT ROOT)
-  Several Networks:
-  Crowbar relies on a few private networks - they can all be on the
   same NIC, bridges, or whatever.
-  Recommended: a local caching proxy server - we download a lot.

OK, let's get started setting up the development environemnt:
=============================================================

What's your platform?
---------------------

Virtual Machine Setup
~~~~~~~~~~~~~~~~~~~~~

-  `VirtualBox <virtualbox.md>`__ based installations - network configs
   and basic install info
-  `KVM on Ubuntu <kvm-ubuntu.md>`__
-  `KVM on Fedora Core 19 <kvm-fedora.md>`__

O/S configs
-----------

Makes sure you have development O/S on the Virtual Machine or bare
metal. Also, get the docker stuff all configured properly:

-  `Ubuntu 12.04.03 <dev-ubuntu-12.04.03.md>`__
-  `CentOS 6.5 <dev-centos-6.5.md>`__
-  `Fedora Core 19 <dev-Fedora.md>`__
-  `SUSE <dev-vm-SUSE.md>`__
-  `OpenSUSE Images <openSUSE-images.md>`__

Setup Docker Admin Node
-----------------------

#. follow steps in `docker-admin.md <docker-admin.md>`__

Deploy Nodes!
~~~~~~~~~~~~~

Now that you've got Crowbar installed, it's time to look in the
`Deployment Guide <../../deployment-guide/README.md>`__ for instructions
about provisioning nodes.

Change to Crowbar user
~~~~~~~~~~~~~~~~~~~~~~

#. ``su - crowbar`` to gain ruby-2.0 and control Crowbar via the CLI!
#. we've provided a handle ``tools/rails-console`` command if you want
   to reach deep into the bowels of the bunny.

