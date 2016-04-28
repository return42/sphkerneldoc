.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-phys-link:

=================
ata_dev_phys_link
=================

*man ata_dev_phys_link(9)*

*4.6.0-rc5*

find physical link for a device


Synopsis
========

.. c:function:: struct ata_link * ata_dev_phys_link( struct ata_device * dev )

Arguments
=========

``dev``
    ATA device to look up physical link for


Description
===========

Look up physical link which ``dev`` is attached to. Note that this is
different from ``dev``->link only when ``dev`` is on slave link. For all
other cases, it's the same as ``dev``->link.


LOCKING
=======

Don't care.


RETURNS
=======

Pointer to the found physical link.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
