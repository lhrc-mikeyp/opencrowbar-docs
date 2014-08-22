.. OpenCrowbar documentation master file for sphinx

OpenCrowbar Documentation
=========================

Welcome to the OpenCrowbar Project - the gateway to a new hardware
provisioning experience that delivers the best of software deployment
automation and orchestration. OpenCrowbar is a successor of the 3 year-old
& still active Crowbar project. It derives much of its functionality
from its predecessor, but offers a lot more.

OpenCrowbar documentation is divided into the following sections:

* :ref:`deploy-guide`
* :ref:`development-guide`
* :ref:`faq`
* :ref:`license`
* :ref:`principles`
* :ref:`user-guide`


.. filelist::

.. _`deploy-guide`:

Deploy Guide
------------

.. toctree::
   :maxdepth: 2

   ./doc/deployment-guide/Install-CentOS-RHEL-6.5-AdminNode
   ./doc/deployment-guide/README
   ./doc/deployment-guide/accessing_bmcs
   ./doc/deployment-guide/adding-operating-systems
   ./doc/deployment-guide/admin_port_maps
   ./doc/deployment-guide/attaching-to-bmc
   ./doc/deployment-guide/directory-layout
   ./doc/deployment-guide/node_registration
   ./doc/deployment-guide/troubleshooting/README


.. _`development-guide`:

Development Guide
-----------------

.. toctree::
   :maxdepth: 2

   ./doc/development-guides/README
   ./doc/development-guides/api/README
   ./doc/development-guides/api/attrib
   ./doc/development-guides/api/barclamp
   ./doc/development-guides/api/deployment
   ./doc/development-guides/api/deployment_role
   ./doc/development-guides/api/dhcp_database
   ./doc/development-guides/api/group
   ./doc/development-guides/api/ignore_me
   ./doc/development-guides/api/interfaces
   ./doc/development-guides/api/jig
   ./doc/development-guides/api/network
   ./doc/development-guides/api/node
   ./doc/development-guides/api/node_role
   ./doc/development-guides/api/range
   ./doc/development-guides/api/role
   ./doc/development-guides/api/run
   ./doc/development-guides/api/status
   ./doc/development-guides/api/test
   ./doc/development-guides/api/user
   ./doc/development-guides/barclamps/README
   ./doc/development-guides/barclamps/new_barclamp
   ./doc/development-guides/contributing-code
   ./doc/development-guides/contributing
   ./doc/development-guides/database
   ./doc/development-guides/dev-systems/README
   ./doc/development-guides/dev-systems/build_sledgehammer
   ./doc/development-guides/dev-systems/dev-openSUSE-images
   ./doc/development-guides/dev-systems/dev-ubuntu-12.04.03
   ./doc/development-guides/dev-systems/dev-vm-SUSE
   ./doc/development-guides/dev-systems/dev-vm-Ubuntu
   ./doc/development-guides/dev-systems/dev-vm
   ./doc/development-guides/dev-systems/docker-TLDR
   ./doc/development-guides/dev-systems/docker-admin
   ./doc/development-guides/dev-systems/docker-slaves
   ./doc/development-guides/dev-systems/kvm-fedora
   ./doc/development-guides/dev-systems/kvm-ubuntu
   ./doc/development-guides/dev-systems/proxy-cache
   ./doc/development-guides/dev-systems/samba_cntlm
   ./doc/development-guides/dev-systems/virtualbox
   ./doc/development-guides/doc-format-guides/README
   ./doc/development-guides/doc-format-guides/formatting
   ./doc/development-guides/doc-format-guides/topic
   ./doc/development-guides/jigs/README
   ./doc/development-guides/jigs/chef
   ./doc/development-guides/jigs/noop
   ./doc/development-guides/jigs/script
   ./doc/development-guides/model/00100_CB2_Design_Topics
   ./doc/development-guides/model/README
   ./doc/development-guides/model/attrib
   ./doc/development-guides/model/barclamp
   ./doc/development-guides/model/crowbar_model
   ./doc/development-guides/model/deployment
   ./doc/development-guides/model/deployment_role
   ./doc/development-guides/model/group
   ./doc/development-guides/model/model
   ./doc/development-guides/model/network
   ./doc/development-guides/model/node
   ./doc/development-guides/model/node_role
   ./doc/development-guides/model/role
   ./doc/development-guides/model/run
   ./doc/development-guides/model/user
   ./doc/development-guides/network-details
   ./doc/development-guides/provisioning
   ./doc/development-guides/testing/README
   ./doc/development-guides/testing/bdd/README
   ./doc/development-guides/testing/bdd/dsl
   ./doc/development-guides/testing/bdd/internals/README
   ./doc/development-guides/testing/bdd/internals/config
   ./doc/development-guides/testing/bdd/internals/json
   ./doc/development-guides/testing/bdd/internals/rest
   ./doc/development-guides/testing/bdd/rats/README
   ./doc/development-guides/testing/bdd/rats/clirat
   ./doc/development-guides/testing/bdd/steps
   ./doc/development-guides/testing/bdd/steps_rest
   ./doc/development-guides/testing/bdd/tips
   ./doc/development-guides/testing/simulator
   ./doc/development-guides/ui/README
   ./doc/development-guides/ui/localization
   ./doc/development-guides/ui/navigation
   ./doc/development-guides/ui/role
   ./doc/development-guides/ui/tips_and_tricks
   ./doc/development-guides/workflow/README
   ./doc/development-guides/workflow/dev-build-sledgehammer
   ./doc/development-guides/workflow/knife-config
   ./doc/development-guides/workflow/online-install
   ./doc/development-guides/workflow/package-updates
   ./doc/development-guides/workflow/sledgehammer-hooks
   ./doc/development-guides/workflow/smoketesting


.. _`faq`:

Frequently Asked Questions (FAQ)
--------------------------------

.. toctree::
   :maxdepth: 2

   ./doc/faq/README
   ./doc/faq/UEFI
   ./doc/faq/do_you_have_a_question


.. _`license`:

OpenCrowbar License
-------------------

.. toctree::
   :maxdepth: 2

   ./doc/licenses/README
   ./doc/licenses/crowbar/README
   ./doc/licenses/crowbar/berkshelf-2
   ./doc/licenses/crowbar/deployer
   ./doc/licenses/crowbar/dns
   ./doc/licenses/crowbar/licenses
   ./doc/licenses/crowbar/logging
   ./doc/licenses/crowbar/network
   ./doc/licenses/crowbar/ntp
   ./doc/licenses/crowbar/provisioner
   ./doc/licenses/crowbar/test


.. _`principles`:

Operational Principles
----------------------

.. toctree::
   :maxdepth: 2

   ./doc/principles/README
   ./doc/principles/attribute_injection
   ./doc/principles/concepts
   ./doc/principles/emergent_services
   ./doc/principles/heterogenous-os-support
   ./doc/principles/late_binding
   ./doc/principles/ready_state
   ./doc/principles/simulated_annealing


.. _`user-guide`:

User Guide
----------

.. toctree::
   :maxdepth: 2

   ./doc/user-guide/README


.. TODO the following need some love and attention before enabling them

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`


