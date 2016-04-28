.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-gnet-stats-basic:

=======================
struct gnet_stats_basic
=======================

*man struct gnet_stats_basic(9)*

*4.6.0-rc5*

byte/packet throughput statistics


Synopsis
========

.. code-block:: c

    struct gnet_stats_basic {
      __u64 bytes;
      __u32 packets;
    };


Members
=======

bytes
    number of seen bytes

packets
    number of seen packets


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
