
.. _API-ata-set-max-sectors:

===================
ata_set_max_sectors
===================

*man ata_set_max_sectors(9)*

*4.6.0-rc1*

Set max sectors


Synopsis
========

.. c:function:: int ata_set_max_sectors( struct ata_device * dev, u64 new_sectors )

Arguments
=========

``dev``
    target device

``new_sectors``
    new max sectors value to set for the device


Description
===========

Set max sectors of ``dev`` to ``new_sectors``.


RETURNS
=======

0 on success, -EACCES if command is aborted or denied (due to previous non-volatile SET_MAX) by the drive. -EIO on other errors.
