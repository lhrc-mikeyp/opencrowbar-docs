OpenCrowbar Troubleshooting Tips
--------------------------------

Chef-Client Fails: cannot download Chef RPM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the very first role applied to a new node fails, there are several
possible causes.

#. outbound network access is not working. Likely cause is that your
   squid proxy is not configured
#. set the http\_proxy (\`export http\_proxy="http://127.0.0.1:8123\ ")
   and attempt to access google.com from the admin server
#. if that worked, try the same thing after ssh'ing to the node
#. you are missing the /tftboot/files path
#. this can be caused when you do not have the ISOs staged

No OS? Installing an OS, the TFTP Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TFTP provides the boot images for the operating system install.

You can inspect the TFTP information the admin node provides by looking
in the ``/tftpboot`` directories.

These directories contain the sledgehammer discovery, base OS install
images and specific instructions for each node in the
``/tftpboot/nodes`` directory.

If Crowbar is not providing the right boot image, this is a good place
to start.
