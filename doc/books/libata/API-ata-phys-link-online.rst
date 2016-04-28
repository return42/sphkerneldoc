.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-phys-link-online:

====================
ata_phys_link_online
====================

*man ata_phys_link_online(9)*

*4.6.0-rc5*

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

Test whether ``link`` is online. Note that this function returns 0 if
online status of ``link`` cannot be obtained, so ata_link_online(link)
!= !ata_link_offline(link).


LOCKING
=======

None.


RETURNS
=======

True if the port online status is available and online.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
