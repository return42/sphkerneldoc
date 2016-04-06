
.. _API-struct-v4l2-of-endpoint:

=======================
struct v4l2_of_endpoint
=======================

*man struct v4l2_of_endpoint(9)*

*4.6.0-rc1*

the endpoint data structure


Synopsis
========

.. code-block:: c

    struct v4l2_of_endpoint {
      struct of_endpoint base;
      enum v4l2_mbus_type bus_type;
      union bus;
      u64 * link_frequencies;
      unsigned int nr_of_link_frequencies;
    };


Members
=======

base
    struct of_endpoint containing port, id, and local of_node

bus_type
    bus type

bus
    bus configuration data structure

link_frequencies
    array of supported link frequencies

nr_of_link_frequencies
    number of elements in link_frequenccies array
