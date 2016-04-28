.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-phys-link-offline:

=====================
ata_phys_link_offline
=====================

*man ata_phys_link_offline(9)*

*4.6.0-rc5*

test whether the given link is offline


Synopsis
========

.. c:function:: bool ata_phys_link_offline( struct ata_link * link )

Arguments
=========

``link``
    ATA link to test


Description
===========

Test whether ``link`` is offline. Note that this function returns 0 if
offline status of ``link`` cannot be obtained, so
ata_link_online(link) != !ata_link_offline(link).


LOCKING
=======

None.


RETURNS
=======

True if the port offline status is available and offline.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
