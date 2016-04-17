.. -*- coding: utf-8; mode: rst -*-

=======
visor.h
=======


.. _`palm_ext_connection_info`:

struct palm_ext_connection_info
===============================

.. c:type:: palm_ext_connection_info

    return data from a PALM_GET_EXT_CONNECTION_INFORMATION request


.. _`palm_ext_connection_info.definition`:

Definition
----------

.. code-block:: c

  struct palm_ext_connection_info {
    __u8 num_ports;
    __u8 endpoint_numbers_different;
  };


.. _`palm_ext_connection_info.members`:

Members
-------

:``num_ports``:
    maximum number of functions/connections in use

:``endpoint_numbers_different``:
    will be 1 if in and out endpoints numbers are
    different, otherwise it is 0.  If value is 1, then
    connections.end_point_info is non-zero.  If value is 0, then
    connections.port contains the endpoint number, which is the same for in
    and out.




.. _`palm_ext_connection_info.description`:

Description
-----------

The maximum number of connections currently supported is 2

