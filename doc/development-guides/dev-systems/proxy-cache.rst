Configuration of Proxy Cache
============================

Because Dev Mode uses online access for packages, we *strongly*
recommend using a caching proxy such as Squid or Polipo.

If you are behind a firewall, you should have the cache access CNTLM or
similar.

Squid Proxy (on Ubuntu)
-----------------------

#. Configure your CNTLM proxy on :3128
#. Install: ``sudo apt-get install squid3``
#. Update your configuration: ``sudo vi /etc/squid3/squid.conf``
#. make sure that you allow containers to use the proxy
#. example https://gist.github.com/cloudedge/1b46280b7dfbffe2d763
#. it is important to add BOTH your local subnet & the docker subnet to
   allowed
#. include the ``always_direct allow to_localnet`` line
#. order is very important in the configuration file
#. Create your cache directory: ``sudo mkdir /var/cache/squid``
#. Allow Squid to write to the cache:
   ``sudo chown proxy:proxy /var/cache/squid``
#. Restart the service: ``sudo service squid3 restart``
#. Access the proxy
#. ``export http_proxy="http://127.0.0.1:8123"``
#. ``export https_proxy="http://127.0.0.1:8123"``
#. Test the proxy: ``wget google.com``

