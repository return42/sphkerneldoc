.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-unpack-xfermask:

===================
ata_unpack_xfermask
===================

*man ata_unpack_xfermask(9)*

*4.6.0-rc5*

Unpack xfer_mask into pio, mwdma and udma masks


Synopsis
========

.. c:function:: void ata_unpack_xfermask( unsigned long xfer_mask, unsigned long * pio_mask, unsigned long * mwdma_mask, unsigned long * udma_mask )

Arguments
=========

``xfer_mask``
    xfer_mask to unpack

``pio_mask``
    resulting pio_mask

``mwdma_mask``
    resulting mwdma_mask

``udma_mask``
    resulting udma_mask


Description
===========

Unpack ``xfer_mask`` into ``pio_mask``, ``mwdma_mask`` and
``udma_mask``. Any NULL distination masks will be ignored.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
