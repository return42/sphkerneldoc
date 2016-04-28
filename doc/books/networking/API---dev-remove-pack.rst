.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-remove-pack:

=================
__dev_remove_pack
=================

*man __dev_remove_pack(9)*

*4.6.0-rc5*

remove packet handler


Synopsis
========

.. c:function:: void __dev_remove_pack( struct packet_type * pt )

Arguments
=========

``pt``
    packet type declaration


Description
===========

Remove a protocol handler that was previously added to the kernel
protocol handlers by ``dev_add_pack``. The passed ``packet_type`` is
removed from the kernel lists and can be freed or reused once this
function returns.

The packet type might still be in use by receivers and must not be freed
until after all the CPU's have gone through a quiescent state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
