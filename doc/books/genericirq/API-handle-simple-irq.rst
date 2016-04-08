
.. _API-handle-simple-irq:

=================
handle_simple_irq
=================

*man handle_simple_irq(9)*

*4.6.0-rc1*

Simple and software-decoded IRQs.


Synopsis
========

.. c:function:: void handle_simple_irq( struct irq_desc * desc )

Arguments
=========

``desc``
    the interrupt description structure for this irq


Description
===========

Simple interrupts are either sent from a demultiplexing interrupt handler or come from hardware, where no interrupt hardware control is necessary.


Note
====

The caller is expected to handle the ack, clear, mask and unmask issues if necessary.
