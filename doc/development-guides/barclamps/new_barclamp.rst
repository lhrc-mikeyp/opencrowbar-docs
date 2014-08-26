Creating a New OpenCrowbar Barclamp
-----------------------------------

    Note: These instructions only apply to OpenCrowbar
    barclamps/workloads.

Before you start, figure out the name that you want to use. It should be
short but descriptive. You will be able to add a more descriptive name,
the repo name must be unique. We also recommend using lower case and
only alpha + underbar (\_) in the name.

Starting from Template
~~~~~~~~~~~~~~~~~~~~~~

To create a new workload, start by forking or cloning the OpenCrowbar
template from [[https://github.com/opencrowbar/template\ ]]

Inside the template:
~~~~~~~~~~~~~~~~~~~~

#. replace "OCBTemplate" occurances with the name of your workload

   #. the replacements include the crowbar.yml, licenses, readme, and
      /doc files.
   #. update the /rails\_engine/db/migrate/[barclamp\_import] script
   #. change the name of the file to match the workload
   #. change the class and barclamp name to match the workload

#. correct file names that are workload specific

   #. rename the */doc/license/ocbtemplate.md* file with the name of
      your workload.md
   #. rename the */barclamps/ocbtemplate.yml* file with the name of your
      workload.yml
   #. rename the */BDD/features/ocbtemplate.feature* file with the name
      of your workload.feature
   #. rename the */roles/ocbtemplate-base/* directory with the name of
      your name of your workload-base


