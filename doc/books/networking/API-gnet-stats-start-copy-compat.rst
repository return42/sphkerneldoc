
.. _API-gnet-stats-start-copy-compat:

============================
gnet_stats_start_copy_compat
============================

*man gnet_stats_start_copy_compat(9)*

*4.6.0-rc1*

start dumping procedure in compatibility mode


Synopsis
========

.. c:function:: int gnet_stats_start_copy_compat( struct sk_buff * skb, int type, int tc_stats_type, int xstats_type, spinlock_t * lock, struct gnet_dump * d )

Arguments
=========

``skb``
    socket buffer to put statistics TLVs into

``type``
    TLV type for top level statistic TLV

``tc_stats_type``
    TLV type for backward compatibility struct tc_stats TLV

``xstats_type``
    TLV type for backward compatibility xstats TLV

``lock``
    statistics lock

``d``
    dumping handle


Description
===========

Initializes the dumping handle, grabs the statistic lock and appends an empty TLV header to the socket buffer for use a container for all other statistic TLVS.

The dumping handle is marked to be in backward compatibility mode telling all ``gnet_stats_copy_XXX`` functions to fill a local copy of struct tc_stats.

Returns 0 on success or -1 if the room in the socket buffer was not sufficient.
