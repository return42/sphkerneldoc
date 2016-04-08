
.. _API-z8530-interrupt:

===============
z8530_interrupt
===============

*man z8530_interrupt(9)*

*4.6.0-rc1*

Handle an interrupt from a Z8530


Synopsis
========

.. c:function:: irqreturn_t z8530_interrupt( int irq, void * dev_id )

Arguments
=========

``irq``
    Interrupt number

``dev_id``
    The Z8530 device that is interrupting.


Description
===========

A Z85[2]30 device has stuck its hand in the air for attention. We scan both the channels on the chip for events and then call the channel specific call backs for each channel that
has events. We have to use callback functions because the two channels can be in different modes.

Locking is done for the handlers. Note that locking is done at the chip level (the 5uS delay issue is per chip not per channel). c->lock for both channels points to dev->lock
