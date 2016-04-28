.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-add-offload:

===============
dev_add_offload
===============

*man dev_add_offload(9)*

*4.6.0-rc5*

register offload handlers


Synopsis
========

.. c:function:: void dev_add_offload( struct packet_offload * po )

Arguments
=========

``po``
    protocol offload declaration


Description
===========

Add protocol offload handlers to the networking stack. The passed
``proto_offload`` is linked into kernel lists and may not be freed until
it has been removed from the kernel lists.

This call does not sleep therefore it can not guarantee all CPU's that
are in middle of receiving packets will see the new offload handlers
(until the next received packet).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
