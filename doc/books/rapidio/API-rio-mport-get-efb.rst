
.. _API-rio-mport-get-efb:

=================
rio_mport_get_efb
=================

*man rio_mport_get_efb(9)*

*4.6.0-rc1*

get pointer to next extended features block


Synopsis
========

.. c:function:: u32 rio_mport_get_efb( struct rio_mport * port, int local, u16 destid, u8 hopcount, u32 from )

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

``from``
    Offset of current Extended Feature block header (if 0 starts from ExtFeaturePtr)
