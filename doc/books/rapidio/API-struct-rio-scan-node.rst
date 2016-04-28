.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-scan-node:

====================
struct rio_scan_node
====================

*man struct rio_scan_node(9)*

*4.6.0-rc5*

list node to register RapidIO enumeration and discovery methods with
RapidIO core.


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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
