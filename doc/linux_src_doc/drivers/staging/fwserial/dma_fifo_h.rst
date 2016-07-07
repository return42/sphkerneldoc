.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fwserial/dma_fifo.h

.. _`dma_fifo_guard`:

DMA_FIFO_GUARD
==============

.. c:function::  DMA_FIFO_GUARD()

    complies with the streaming DMA API design that can be DMA'd from directly (without additional copying), coupled with an input side that maintains a logically consistent 'apparent' size (ie, bytes in + bytes avail is static for the lifetime of the FIFO).

.. _`dma_fifo_guard.description`:

Description
-----------

DMA output transactions originate on a cache line boundary and can be
variably-sized. DMA output transactions can be retired out-of-order but
the FIFO will only advance the output in the original input sequence.
This means the FIFO will eventually stall if a transaction is never retired.

Chunking the output side into cache line multiples means that some FIFO
memory is unused. For example, if all the avail input has been pended out,
then the in and out markers are re-aligned to the next cache line.
The maximum possible waste is
(cache line alignment - 1) \* (max outstanding dma transactions)
This potential waste requires additional hidden capacity within the FIFO
to be able to accept input while the 'apparent' size has not been reached.

Additional cache lines (ie, guard area) are used to minimize DMA
fragmentation when wrapping at the end of the FIFO. Input is allowed into the
guard area, but the in and out FIFO markers are wrapped when DMA is pended.

.. This file was automatic generated / don't edit.

