
.. _API-ata-dev-set-xfermode:

====================
ata_dev_set_xfermode
====================

*man ata_dev_set_xfermode(9)*

*4.6.0-rc1*

Issue SET FEATURES - XFER MODE command


Synopsis
========

.. c:function:: unsigned int ata_dev_set_xfermode( struct ata_device * dev )

Arguments
=========

``dev``
    Device to which command will be sent


Description
===========

Issue SET FEATURES - XFER MODE command to device ``dev`` on port ``ap``.


LOCKING
=======

PCI/etc. bus probe sem.


RETURNS
=======

0 on success, AC_ERR_⋆ mask otherwise.
