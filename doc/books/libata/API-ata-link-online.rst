
.. _API-ata-link-online:

===============
ata_link_online
===============

*man ata_link_online(9)*

*4.6.0-rc1*

test whether the given link is online


Synopsis
========

.. c:function:: bool ata_link_online( struct ata_link * link )

Arguments
=========

``link``
    ATA link to test


Description
===========

Test whether ``link`` is online. This is identical to ``ata_phys_link_online`` when there's no slave link. When there's a slave link, this function should only be called on the
master link and will return true if any of M/S links is online.


LOCKING
=======

None.


RETURNS
=======

True if the port online status is available and online.
