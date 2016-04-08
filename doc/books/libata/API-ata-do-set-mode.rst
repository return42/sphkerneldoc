
.. _API-ata-do-set-mode:

===============
ata_do_set_mode
===============

*man ata_do_set_mode(9)*

*4.6.0-rc1*

Program timings and issue SET FEATURES - XFER


Synopsis
========

.. c:function:: int ata_do_set_mode( struct ata_link * link, struct ata_device ** r_failed_dev )

Arguments
=========

``link``
    link on which timings will be programmed

``r_failed_dev``
    out parameter for failed device


Description
===========

Standard implementation of the function used to tune and set ATA device disk transfer mode (PIO3, UDMA6, etc.). If ``ata_dev_set_mode`` fails, pointer to the failing device is
returned in ``r_failed_dev``.


LOCKING
=======

PCI/etc. bus probe sem.


RETURNS
=======

0 on success, negative errno otherwise
