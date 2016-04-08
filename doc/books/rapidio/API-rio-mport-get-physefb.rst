
.. _API-rio-mport-get-physefb:

=====================
rio_mport_get_physefb
=====================

*man rio_mport_get_physefb(9)*

*4.6.0-rc1*

Helper function that returns register offset for Physical Layer Extended Features Block.


Synopsis
========

.. c:function:: u32 rio_mport_get_physefb( struct rio_mport * port, int local, u16 destid, u8 hopcount )

Arguments
=========

``port``
    Master port to issue transaction

``local``
    Indicate a local master port or remote device access

``destid``
    Destination ID of the device

``hopcount``
    Number of switch hops to the device
