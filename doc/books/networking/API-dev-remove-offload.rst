.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-remove-offload:

==================
dev_remove_offload
==================

*man dev_remove_offload(9)*

*4.6.0-rc5*

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

Remove a packet offload handler that was previously added to the kernel
offload handlers by ``dev_add_offload``. The passed ``offload_type`` is
removed from the kernel lists and can be freed or reused once this
function returns.

This call sleeps to guarantee that no CPU is looking at the packet type
after return.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
