
.. _API-ata-xfer-mode2shift:

===================
ata_xfer_mode2shift
===================

*man ata_xfer_mode2shift(9)*

*4.6.0-rc1*

Find matching xfer_shift for XFER_⋆


Synopsis
========

.. c:function:: int ata_xfer_mode2shift( unsigned long xfer_mode )

Arguments
=========

``xfer_mode``
    XFER_⋆ of interest


Description
===========

Return matching xfer_shift for ``xfer_mode``.


LOCKING
=======

None.


RETURNS
=======

Matching xfer_shift, -1 if no match found.
