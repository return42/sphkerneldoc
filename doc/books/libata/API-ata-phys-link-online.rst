
.. _API-ata-phys-link-online:

====================
ata_phys_link_online
====================

*man ata_phys_link_online(9)*

*4.6.0-rc1*

test whether the given link is online


Synopsis
========

.. c:function:: bool ata_phys_link_online( struct ata_link * link )

Arguments
=========

``link``
    ATA link to test


Description
===========

Test whether ``link`` is online. Note that this function returns 0 if online status of ``link`` cannot be obtained, so ata_link_online(link) != !ata_link_offline(link).


LOCKING
=======

None.


RETURNS
=======

True if the port online status is available and online.
