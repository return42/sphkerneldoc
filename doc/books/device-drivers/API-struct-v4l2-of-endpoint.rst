.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-of-endpoint:

=======================
struct v4l2_of_endpoint
=======================

*man struct v4l2_of_endpoint(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
