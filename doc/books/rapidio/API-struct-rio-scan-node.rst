
.. _API-struct-rio-scan-node:

====================
struct rio_scan_node
====================

*man struct rio_scan_node(9)*

*4.6.0-rc1*

list node to register RapidIO enumeration and discovery methods with RapidIO core.


Synopsis
========

.. code-block:: c

    struct rio_scan_node {
      int mport_id;
      struct list_head node;
      struct rio_scan * ops;
    };


Members
=======

mport_id
    ID of an mport (net) serviced by this enumerator

node
    node in global list of registered enumerators

ops
    RIO enumeration and discovery operations
