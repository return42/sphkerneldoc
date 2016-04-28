.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-rio-switch:

=================
struct rio_switch
=================

*man struct rio_switch(9)*

*4.6.0-rc5*

RIO switch info


Synopsis
========

.. code-block:: c

    struct rio_switch {
      struct list_head node;
      u8 * route_table;
      u32 port_ok;
      struct rio_switch_ops * ops;
      spinlock_t lock;
      struct rio_dev * nextdev[0];
    };


Members
=======

node
    Node in global list of switches

route_table
    Copy of switch routing table

port_ok
    Status of each port (one bit per port) - OK=1 or UNINIT=0

ops
    pointer to switch-specific operations

lock
    lock to serialize operations updates

nextdev[0]
    Array of per-port pointers to the next attached device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
