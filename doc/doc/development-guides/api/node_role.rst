Node Role APIs
~~~~~~~~~~~~~~

Node Roles are the core of OpenCrowbar deployment and orchestration
engine

| There are four types of data that OpenCrowbar tracks, three of them
| are maintained on related NodeRoleDatum mode.

#. user data (node\_role.data) is set by users during the proposed
   state (also known as "out bound data")
#. system data (node\_role.sysdata) is set by crowbar before annealing
   (also known as "out bound data")
#. wall data (node\_role.wall) is set by the jig after transistion
   (also known as "in bound data")
#. discovery data (node.wall) is stored on the node instead of node
    role because it reflects node information aggregated from all the
    jigs. This information is available using the node.attrib\_[name]
    and Attrib model. Please see the node API docs for more about this
    type of data

| NodeRole does not have a natural key, so you must reference them them
| by ID or under the relevant Nodes, Roles, or Deployment.

API Actions
^^^^^^^^^^^

+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| Verb     | URL                                                   | Comments        |
+==========+=======================================================+=================+===========================================================+=====+
| GET      | api/v2/node\_roles                                    | List            |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| GET      | api/v2/node\_roles/:id                                | Specific Item   |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| PUT      | api/v2/node\_roles/:id                                | Update Item     |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| POST     | api/v2/node\_roles                                    | Create Item     |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| GET      | /api/v2/node\_roles/[:node\_role\_id]/attribs         | none            | List Attribs for a specific node\_role                    | -   |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| GET      | /api/v2/node\_roles/[:node\_role\_id]/attribs/[:id]   | none            | Show Attrib (including value) for a specific Node\_Role   | -   |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| PUT      | /api/v2/node\_roles/[:node\_role\_id]/attribs/[:id]   | none            | Update Attrib                                             |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+
| DELETE   | -                                                     | NOT SUPPORTED   |
+----------+-------------------------------------------------------+-----------------+-----------------------------------------------------------+-----+

| Helpers have been added to NodeRole create so that you do not need to
| provide IDs when creating a new NodeRole. You can pass:

-  Deployment Name instead of Deployment ID
-  Node Name instead of Node ID
-  Role Name instead of Role ID

JSON fields
-----------

+------------------+----------------+------------+-------------------------+
| Attribute        | Type           | Settable   | Note                    |
+==================+================+============+=========================+
| Available        | Boolean        | Yes        |                         |
+------------------+----------------+------------+-------------------------+
| Cohort           | Integer        | ??         |                         |
+------------------+----------------+------------+-------------------------+
| Created\_at      | String         | No         | Unicode - date format   |
+------------------+----------------+------------+-------------------------+
| Updated\_at      | String         | No         | Unicode - date format   |
+------------------+----------------+------------+-------------------------+
| Runlog           | String         | ??         |                         |
+------------------+----------------+------------+-------------------------+
| Order            | Integer        | ??         |                         |
+------------------+----------------+------------+-------------------------+
| State            | Integer        | ??         |                         |
+------------------+----------------+------------+-------------------------+
| Node\_Id         | Integer        | Yes        |                         |
+------------------+----------------+------------+-------------------------+
| Status           | ??             | ??         |                         |
+------------------+----------------+------------+-------------------------+
| Run\_count       | Integer        | No         |                         |
+------------------+----------------+------------+-------------------------+
| Deployment\_Id   | Integer        | ??         |                         |
+------------------+----------------+------------+-------------------------+
| Role\_Id         | Integer        | Yes        |                         |
+------------------+----------------+------------+-------------------------+
| Id               | Internal Ref   | ??         | Actually an Int         |
+------------------+----------------+------------+-------------------------+

