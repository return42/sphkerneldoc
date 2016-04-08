
.. _API-ata-dev-configure:

=================
ata_dev_configure
=================

*man ata_dev_configure(9)*

*4.6.0-rc1*

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

Configure ``dev`` according to ``dev``->id. Generic and low-level driver specific fixups are also applied.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, -errno otherwise
