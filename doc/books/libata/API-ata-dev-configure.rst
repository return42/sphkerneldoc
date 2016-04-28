.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-configure:

=================
ata_dev_configure
=================

*man ata_dev_configure(9)*

*4.6.0-rc5*

Configure the specified ATA/ATAPI device


Synopsis
========

.. c:function:: int ata_dev_configure( struct ata_device * dev )

Arguments
=========

``dev``
    Target device to configure


Description
===========

Configure ``dev`` according to ``dev``->id. Generic and low-level driver
specific fixups are also applied.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, -errno otherwise


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
