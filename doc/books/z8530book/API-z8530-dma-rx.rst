
.. _API-z8530-dma-rx:

============
z8530_dma_rx
============

*man z8530_dma_rx(9)*

*4.6.0-rc1*

Handle a DMA RX event


Synopsis
========

.. c:function:: void z8530_dma_rx( struct z8530_channel * chan )

Arguments
=========

``chan``
    Channel to handle


Description
===========

Non bus mastering DMA interfaces for the Z8x30 devices. This is really pretty PC specific. The DMA mode means that most receive events are handled by the DMA hardware. We get a
kick here only if a frame ended.
