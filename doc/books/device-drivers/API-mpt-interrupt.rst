.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-interrupt:

=============
mpt_interrupt
=============

*man mpt_interrupt(9)*

*4.6.0-rc5*

MPT adapter (IOC) specific interrupt handler.


Synopsis
========

.. c:function:: irqreturn_t mpt_interrupt( int irq, void * bus_id )

Arguments
=========

``irq``
    irq number (not used)

``bus_id``
    bus identifier cookie == pointer to MPT_ADAPTER structure


Description
===========

This routine is registered via the ``request_irq`` kernel API call, and
handles all interrupts generated from a specific MPT adapter (also
referred to as a IO Controller or IOC). This routine must clear the
interrupt from the adapter and does so by reading the reply FIFO.
Multiple replies may be processed per single call to this routine.

This routine handles register-level access of the adapter but dispatches
(calls) a protocol-specific callback routine to handle the
protocol-specific details of the MPT request completion.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
