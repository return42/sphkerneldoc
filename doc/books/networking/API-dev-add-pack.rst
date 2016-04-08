
.. _API-dev-add-pack:

============
dev_add_pack
============

*man dev_add_pack(9)*

*4.6.0-rc1*

add packet handler


Synopsis
========

.. c:function:: void dev_add_pack( struct packet_type * pt )

Arguments
=========

``pt``
    packet type declaration


Description
===========

Add a protocol handler to the networking stack. The passed ``packet_type`` is linked into kernel lists and may not be freed until it has been removed from the kernel lists.

This call does not sleep therefore it can not guarantee all CPU's that are in middle of receiving packets will see the new packet type (until the next received packet).
