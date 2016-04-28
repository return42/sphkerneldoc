.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-subbufs-consumed:

======================
relay_subbufs_consumed
======================

*man relay_subbufs_consumed(9)*

*4.6.0-rc5*

update the buffer's sub-buffers-consumed count


Synopsis
========

.. c:function:: void relay_subbufs_consumed( struct rchan * chan, unsigned int cpu, size_t subbufs_consumed )

Arguments
=========

``chan``
    the channel

``cpu``
    the cpu associated with the channel buffer to update

``subbufs_consumed``
    number of sub-buffers to add to current buf's count


Description
===========

Adds to the channel buffer's consumed sub-buffer count.
subbufs_consumed should be the number of sub-buffers newly consumed,
not the total consumed.

NOTE. Kernel clients don't need to call this function if the channel
mode is 'overwrite'.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
