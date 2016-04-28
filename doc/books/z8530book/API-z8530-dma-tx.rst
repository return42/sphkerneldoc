.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-dma-tx:

============
z8530_dma_tx
============

*man z8530_dma_tx(9)*

*4.6.0-rc5*

Handle a DMA TX event


Synopsis
========

.. c:function:: void z8530_dma_tx( struct z8530_channel * chan )

Arguments
=========

``chan``
    The Z8530 channel to handle


Description
===========

We have received an interrupt while doing DMA transmissions. It
shouldn't happen. Scream loudly if it does.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
