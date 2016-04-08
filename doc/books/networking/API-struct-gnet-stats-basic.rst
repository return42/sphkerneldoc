
.. _API-struct-gnet-stats-basic:

=======================
struct gnet_stats_basic
=======================

*man struct gnet_stats_basic(9)*

*4.6.0-rc1*

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
