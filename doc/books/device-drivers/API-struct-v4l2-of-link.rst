
.. _API-struct-v4l2-of-link:

===================
struct v4l2_of_link
===================

*man struct v4l2_of_link(9)*

*4.6.0-rc1*

a link between two endpoints


Synopsis
========

.. code-block:: c

    struct v4l2_of_link {
      struct device_node * local_node;
      unsigned int local_port;
      struct device_node * remote_node;
      unsigned int remote_port;
    };


Members
=======

local_node
    pointer to device_node of this endpoint

local_port
    identifier of the port this endpoint belongs to

remote_node
    pointer to device_node of the remote endpoint

remote_port
    identifier of the port the remote endpoint belongs to
