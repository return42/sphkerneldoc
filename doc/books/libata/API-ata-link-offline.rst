.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-link-offline:

================
ata_link_offline
================

*man ata_link_offline(9)*

*4.6.0-rc5*

test whether the given link is offline


Synopsis
========

.. c:function:: bool ata_link_offline( struct ata_link * link )

Arguments
=========

``link``
    ATA link to test


Description
===========

Test whether ``link`` is offline. This is identical to
``ata_phys_link_offline`` when there's no slave link. When there's a
slave link, this function should only be called on the master link and
will return true if both M/S links are offline.


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
