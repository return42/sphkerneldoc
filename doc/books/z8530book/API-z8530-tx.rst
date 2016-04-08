
.. _API-z8530-tx:

========
z8530_tx
========

*man z8530_tx(9)*

*4.6.0-rc1*

Handle a PIO transmit event


Synopsis
========

.. c:function:: void z8530_tx( struct z8530_channel * c )

Arguments
=========

``c``
    Z8530 channel to process


Description
===========

Z8530 transmit interrupt handler for the PIO mode. The basic idea is to attempt to keep the FIFO fed. We fill as many bytes in as possible, its quite possible that we won't keep up
with the data rate otherwise.
