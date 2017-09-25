.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/serial/visor.h

.. _`palm_ext_connection_info`:

struct palm_ext_connection_info
===============================

.. c:type:: struct palm_ext_connection_info

    return data from a PALM_GET_EXT_CONNECTION_INFORMATION request

.. _`palm_ext_connection_info.definition`:

Definition
----------

.. code-block:: c

    struct palm_ext_connection_info {
        __u8 num_ports;
        __u8 endpoint_numbers_different;
        __le16 reserved1;
        struct {
            __u32 port_function_id;
            __u8 port;
            __u8 end_point_info;
            __le16 reserved;
        } connections[2];
    }

.. _`palm_ext_connection_info.members`:

Members
-------

num_ports
    maximum number of functions/connections in use

endpoint_numbers_different
    will be 1 if in and out endpoints numbers are
    different, otherwise it is 0.  If value is 1, then
    connections.end_point_info is non-zero.  If value is 0, then
    connections.port contains the endpoint number, which is the same for in
    and out.

reserved1
    *undescribed*

port_function_id
    contains the creator id of the application that opened
    this connection.

port
    contains the in/out endpoint number.  Is 0 if in and out endpoint
    numbers are different.

end_point_info
    high nubbe is in endpoint and low nibble will indicate out
    endpoint.  Is 0 if in and out endpoints are the same.

reserved
    *undescribed*

onnections
    *undescribed*

.. _`palm_ext_connection_info.description`:

Description
-----------

The maximum number of connections currently supported is 2

.. This file was automatic generated / don't edit.

