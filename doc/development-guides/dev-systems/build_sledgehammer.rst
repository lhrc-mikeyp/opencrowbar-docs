Build Sledgehammer (Advanced Dev Only)
======================================

WARNING: Option step! Usually requires multiple retries.

By default, setup will now download golden sledgehammers and this step
is not needed.

    Only do this step if you want to make changes to Sledgehammer! We
    recommend using the golden sledgehammer.

#. prep for sledgehammer requirements:

   #. ubuntu: ``sudo apt-get install curl rpm rpm2cpio``

#. from core, ``tools/build_sledgehammer.sh``

   #. warning: this may take multiple attempts to complete to downloads.
      Keep trying.
   #. warning: might need a better literal mirror in
      sledgehammer/sledgehammer.ks - see
      `Details <(../../workflow/dev-build-sledgehammer.md)>`__


