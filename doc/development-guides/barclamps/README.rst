Crowbar Barclamps
-----------------

    **NOTE: This is from the wiki and needs to be reviewed, RAH
    11/9/2012**

| The Crowbar barclamp provides the roles and recipes to set up the
barclamp framework.
| It initializes the system, creates initial instances of other
barclamps defined in its configuration, and creates the users to access
the crowbar API and UI. Any number of barclamp instances can be started.
By default, the system starts a network, ganglia, nagios, ntp, dns,
provisioner, deployer, ipmi, raid, and BIOS barclamp based upon their
default configurations. The initialization function of the crowbar
barclamp works exactly like the other barclamps. A proposal is created
and can be committed during installation.

The main post-installation function is to provide the main transition
entry point for the system. All barclamps' transition functions can be
called directly, but the crowbar barclamp calls these in an order
specified each barclamps' crowbar.yml file. The default unspecified
priority is 1000.

Roles
~~~~~

The following node roles are defined:

-  Crowbar

   -  Configures the system to run the barclamp framework (web app and
      other services).
   -  Depends upon the apache2, rails, passenger, and utils cookbooks.

Scripts
~~~~~~~

The shared barclamp command line library is all the is provided to
interact with the barclamp.

The following scripts are also provided.

+--------------------------+------------------------------------------------------------------+
| Script                   | Description                                                      |
+==========================+==================================================================+
| crowbar                  | Master control script for the command line interface             |
+--------------------------+------------------------------------------------------------------+
| crowbar\_crowbar         | The actual control script for the crowbar barclamp               |
+--------------------------+------------------------------------------------------------------+
| crowbar\_watch\_status   | Wrapper for script that watches the node state and node status   |
+--------------------------+------------------------------------------------------------------+
| crowbar\_node\_state     | Displays the current provisioner state of the nodes              |
+--------------------------+------------------------------------------------------------------+
| crowbar\_node\_status    | Displays the current nagios state of the nodes                   |
+--------------------------+------------------------------------------------------------------+
| transition.sh            | A helper script that can be used to transition nodes             |
+--------------------------+------------------------------------------------------------------+

Parameters
~~~~~~~~~~

The Crowbar Barclamp has a couple of list parameters.

+-------------+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name        | Default                                                     | Description                                                                                                                                                          |
+=============+=============================================================+======================================================================================================================================================================+
| instances   | The starting barclamps using their default configurations   | A map of barclamp names that reference a list of json files (default is special to mean to take the defaults) that represent starting barclamp instances to create   |
+-------------+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| users       | A map of users - containing crowbar                         | This map defines the users allowed access to the OpenCrowbar UI and its REST API                                                                                     |
+-------------+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The users map contains a map.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The key is the user name and the rest of the required fields are:

+---------------+-----------------------------------+
| Name          | Description                       |
+===============+===================================+
| password      | Clear text password of the user   |
+---------------+-----------------------------------+
| description   | A description of the user.        |
+---------------+-----------------------------------+

**Operations**

When the barclamp is committed, it uses a custom apply\_roles function
to ensure that the barclamps listed in the instances variable are
created and committed.

Once running, the barclamp provides the global transition function that
calls other barclamps as nodes transition. The barclamp is also
responsible for creating new nodes, assigning them a temporary name. The
deployer will change these things if needed later in the node life
cycle. The transition function will also add the crowbar config to the
admin node as it transitions through the **discovered** state.

When starting a barclamp, use the following steps.

Example (using Swift):

**Proposals:**

#. crowbar swift proposal list

   -  Output: Nothing or the name of the current proposals ie...
      default, Default, etc...

#. crowbar swift proposal show Default > swift\_default.txt

   -  Output: creates the file swift\_default.txt with the settings that
      are currently ready for deployment
   -  Other things you can do with the file:

      -  Edit the file and change parameters. Once done you will need to
         import or edit the proposal.

#. crowbar swift proposal --file=swift\_default.txt edit Default

   -  Output: "Edited Default"

#. Command: crowbar swift commit Default

   -  Output: "Committed Default"

**Working with the Running Config**

#. crowbar swift list

   -  List Current running configs

#. crowbar swift show "Name"

   -  Shows the config in question in stdout, you can use standard unix
      commands to send it to a file

#. crowbar swift --file=file.txt edit "Name"

   -  Edit and commits the current running config

#. crowbar swift create default2

   -  creates and commits a config using defaults

**Usage: crowbar swift [options] **

-  --help or -h - help
-  --hostname or -n - specifies the destination server
-  --port or -p - specifies the destination server port
-  --debug or -d - turns on debugging information
-  --data - used by create or edit as data (must be in json format)
-  --file - used by create or edit as data when read from a file (must
   be in json format)
-  --timeout - timeout in seconds for read http reads
-  transition - Transition a mac to state
-  edit - edit a new config
-  list - show a list of current configs
-  help - this page
-  delete - delete a config
-  element\_node - List nodes that could be that element
-  elements - List elements of a deploy
-  show - show a specific config
-  create - create a specific config
-  proposal - Proposal sub-commands
-  commit - Commit a proposal to active
-  edit - edit a new proposal
-  list - show a list of current proposals
-  delete - delete a proposal
-  show - show a specific proposal
-  create - create a proposal

