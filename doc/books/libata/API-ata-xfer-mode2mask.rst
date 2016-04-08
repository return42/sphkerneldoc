
.. _API-ata-xfer-mode2mask:

==================
ata_xfer_mode2mask
==================

*man ata_xfer_mode2mask(9)*

*4.6.0-rc1*

Find matching xfer_mask for XFER_⋆


Synopsis
========

.. c:function:: unsigned long ata_xfer_mode2mask( u8 xfer_mode )

Arguments
=========

``xfer_mode``
    XFER_⋆ of interest


Description
===========

Return matching xfer_mask for ``xfer_mode``.


LOCKING
=======

None.


RETURNS
=======

Matching xfer_mask, 0 if no match found.
