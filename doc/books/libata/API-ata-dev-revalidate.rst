
.. _API-ata-dev-revalidate:

==================
ata_dev_revalidate
==================

*man ata_dev_revalidate(9)*

*4.6.0-rc1*

Revalidate ATA device


Synopsis
========

.. c:function:: int ata_dev_revalidate( struct ata_device * dev, unsigned int new_class, unsigned int readid_flags )

Arguments
=========

``dev``
    device to revalidate

``new_class``
    new class code

``readid_flags``
    read ID flags


Description
===========

Re-read IDENTIFY page, make sure ``dev`` is still attached to the port and reconfigure it according to the new IDENTIFY page.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, negative errno otherwise
