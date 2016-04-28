.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-pack-xfermask:

=================
ata_pack_xfermask
=================

*man ata_pack_xfermask(9)*

*4.6.0-rc5*

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

Pack ``pio_mask``, ``mwdma_mask`` and ``udma_mask`` into a single
unsigned int xfer_mask.


LOCKING
=======

None.


RETURNS
=======

Packed xfer_mask.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
