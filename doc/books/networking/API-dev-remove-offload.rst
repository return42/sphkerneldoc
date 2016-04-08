
.. _API-dev-remove-offload:

==================
dev_remove_offload
==================

*man dev_remove_offload(9)*

*4.6.0-rc1*

remove packet offload handler


Synopsis
========

.. c:function:: void dev_remove_offload( struct packet_offload * po )

Arguments
=========

``po``
    packet offload declaration


Description
===========

Remove a packet offload handler that was previously added to the kernel offload handlers by ``dev_add_offload``. The passed ``offload_type`` is removed from the kernel lists and
can be freed or reused once this function returns.

This call sleeps to guarantee that no CPU is looking at the packet type after return.
