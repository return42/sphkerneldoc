
.. _API-z8530-dma-status:

================
z8530_dma_status
================

*man z8530_dma_status(9)*

*4.6.0-rc1*

Handle a DMA status exception


Synopsis
========

.. c:function:: void z8530_dma_status( struct z8530_channel * chan )

Arguments
=========

``chan``
    Z8530 channel to process

    A status event occurred on the Z8530. We receive these for two reasons when in DMA mode. Firstly if we finished a packet transfer we get one and kick the next packet out.
    Secondly we may see a DCD change.
