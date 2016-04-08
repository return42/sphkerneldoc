
.. _API-gnet-stats-start-copy:

=====================
gnet_stats_start_copy
=====================

*man gnet_stats_start_copy(9)*

*4.6.0-rc1*

start dumping procedure in compatibility mode


Synopsis
========

.. c:function:: int gnet_stats_start_copy( struct sk_buff * skb, int type, spinlock_t * lock, struct gnet_dump * d )

Arguments
=========

``skb``
    socket buffer to put statistics TLVs into

``type``
    TLV type for top level statistic TLV

``lock``
    statistics lock

``d``
    dumping handle


Description
===========

Initializes the dumping handle, grabs the statistic lock and appends an empty TLV header to the socket buffer for use a container for all other statistic TLVS.

Returns 0 on success or -1 if the room in the socket buffer was not sufficient.
