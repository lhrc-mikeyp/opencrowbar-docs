User Guide
==========

This is the (nascent) OpenCrowbar user guide. Please feel free to add
sections and information as needed.

State Image Key
~~~~~~~~~~~~~~~

+--------------+------------------------+-----------------------------------------------------+
| State        | Icon                   | Description                                         |
+==============+========================+=====================================================+
| Ready        | |Ready (image)|        | Updates applied, Stable                             |
+--------------+------------------------+-----------------------------------------------------+
| Error        | |Error (image)|        | Failed, Incomplete transition                       |
+--------------+------------------------+-----------------------------------------------------+
| Blocked      | |Blocked (image)|      | Annealer waiting until all prereq's met             |
+--------------+------------------------+-----------------------------------------------------+
| Idle         | |Idle (image)|         | System not active                                   |
+--------------+------------------------+-----------------------------------------------------+
| Off          | |Off (image)|          | Power is off. No activity possible                  |
+--------------+------------------------+-----------------------------------------------------+
| Proposed     | |Proposed (image)|     | Waiting on user input                               |
+--------------+------------------------+-----------------------------------------------------+
| Reserved     | |Reserved (image)|     | User hold on activity                               |
+--------------+------------------------+-----------------------------------------------------+
| To do        | |TODO (image)|         | All prereq's met but not Annealer not started yet   |
+--------------+------------------------+-----------------------------------------------------+
| Transition   | |Transition (image)|   | Annealer sent work to Jig                           |
+--------------+------------------------+-----------------------------------------------------+

.. |Ready (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/active.png
.. |Error (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/error.png
.. |Blocked (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/blocked.png
.. |Idle (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/active.png
.. |Off (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/active.png
.. |Proposed (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/proposed.png
.. |Reserved (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/reserved.png
.. |TODO (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/todo.png
.. |Transition (image)| image:: https://raw.githubusercontent.com/opencrowbar/core/master/rails/public/images/icons/led/transition.png
