
.. _API-ata-dev-reread-id:

=================
ata_dev_reread_id
=================

*man ata_dev_reread_id(9)*

*4.6.0-rc1*

Re-read IDENTIFY data


Synopsis
========

.. c:function:: int ata_dev_reread_id( struct ata_device * dev, unsigned int readid_flags )

Arguments
=========

``dev``
    target ATA device

``readid_flags``
    read ID flags


Description
===========

Re-read IDENTIFY page and make sure ``dev`` is still attached to the port.


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, negative errno otherwise
