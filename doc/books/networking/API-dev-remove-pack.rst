
.. _API-dev-remove-pack:

===============
dev_remove_pack
===============

*man dev_remove_pack(9)*

*4.6.0-rc1*

remove packet handler


Synopsis
========

.. c:function:: void dev_remove_pack( struct packet_type * pt )

Arguments
=========

``pt``
    packet type declaration


Description
===========

Remove a protocol handler that was previously added to the kernel protocol handlers by ``dev_add_pack``. The passed ``packet_type`` is removed from the kernel lists and can be
freed or reused once this function returns.

This call sleeps to guarantee that no CPU is looking at the packet type after return.
