.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-link-next:

=============
ata_link_next
=============

*man ata_link_next(9)*

*4.6.0-rc5*

link iteration helper


Synopsis
========

.. c:function:: struct ata_link * ata_link_next( struct ata_link * link, struct ata_port * ap, enum ata_link_iter_mode mode )

Arguments
=========

``link``
    the previous link, NULL to start

``ap``
    ATA port containing links to iterate

``mode``
    iteration mode, one of ATA_LITER_*


LOCKING
=======

Host lock or EH context.


RETURNS
=======

Pointer to the next link.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
