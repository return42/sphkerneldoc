
.. _API-z8530-rx:

========
z8530_rx
========

*man z8530_rx(9)*

*4.6.0-rc1*

Handle a PIO receive event


Synopsis
========

.. c:function:: void z8530_rx( struct z8530_channel * c )

Arguments
=========

``c``
    Z8530 channel to process


Description
===========

Receive handler for receiving in PIO mode. This is much like the async one but not quite the same or as complex


Note
====

Its intended that this handler can easily be separated from the main code to run realtime. That'll be needed for some machines (eg to ever clock 64kbits on a sparc ;)).

The RT_LOCK macros don't do anything now. Keep the code covered by them as short as possible in all circumstances - clocks cost baud. The interrupt handler is assumed to be atomic
w.r.t. to other code - this is true in the RT case too.

We only cover the sync cases for this. If you want 2Mbit async do it yourself but consider medical assistance first. This non DMA synchronous mode is portable code. The DMA mode
assumes PCI like ISA DMA

Called with the device lock held
