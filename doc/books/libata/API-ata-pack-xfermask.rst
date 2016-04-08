
.. _API-ata-pack-xfermask:

=================
ata_pack_xfermask
=================

*man ata_pack_xfermask(9)*

*4.6.0-rc1*

Pack pio, mwdma and udma masks into xfer_mask


Synopsis
========

.. c:function:: unsigned long ata_pack_xfermask( unsigned long pio_mask, unsigned long mwdma_mask, unsigned long udma_mask )

Arguments
=========

``pio_mask``
    pio_mask

``mwdma_mask``
    mwdma_mask

``udma_mask``
    udma_mask


Description
===========

Pack ``pio_mask``, ``mwdma_mask`` and ``udma_mask`` into a single unsigned int xfer_mask.


LOCKING
=======

None.


RETURNS
=======

Packed xfer_mask.
