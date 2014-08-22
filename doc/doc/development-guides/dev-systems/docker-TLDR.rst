Short Term notes for running the OpenCrowbar in Docker
------------------------------------------------------

This is the TL;DR version; the full version is
`here <docker-admin.md>`__.

#. Place the OS install ISOs for OSes you want to deploy on to slaves in
    ``$HOME/.cache/opencrowbar/tftpboot/isos``. We currently support:
#. ``CentOS-6.5-x86_64-bin-DVD1.iso``
#. ``RHEL6.4-20130130.0-Server-x86_64-DVD1.iso``
#. ``ubuntu-12.04.4-server-amd64.iso``
#. Prep Environment
#. Install Docker (do once)
#. ``sudo chmod 666 /var/run/docker.sock`` (to run docker without sudo)
#. ``sudo usermod -a -G docker <your-user>`` (to permanently run Docker
    without sudo)
#. To build Sledgehammer:
#. ``tools/build_sledgehammer.sh``
   `Details <../../workflow/dev-build-sledgehammer.md>`__
#. To run in development mode:
#. ``tools/docker-admin centos ./development.sh``
#. To run in production mode:
#. ``tools/docker-admin centos ./production.sh admin.cluster.fqdn``
    The first time you run this, it will take awhile as caches a few
    critical files and extracts the ISOs.
#. ``tools/kvm-slave`` (to launch a KVM-based compute node)

Once Crowbar is bootstrapped (or if anything goes wrong), you will get a
shell running inside a 'tmux' session, the first of which is in the
container. Exiting the shell will kill Docker.

More about tmux:

http://tmuxp.readthedocs.org/en/latest/about_tmux.html
